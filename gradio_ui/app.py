import gradio as gr
import torch
from transformers import T5Tokenizer, TFT5ForConditionalGeneration
import re
import nltk
import random
from datetime import datetime

# Download nltk resources if needed
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Load the fine-tuned model and tokenizer
MODEL_PATH = '../model'

def load_model(model_path):
    try:
        tokenizer = T5Tokenizer.from_pretrained(model_path)
        model = TFT5ForConditionalGeneration.from_pretrained(model_path)
        return model, tokenizer
    except Exception as e:
        print(f"Error loading model: {e}")
        return None, None

model, tokenizer = load_model(MODEL_PATH)

# Initialize chat history
chat_history = []

# History domain keywords for filtering
HISTORY_KEYWORDS = [
    "history", "ancient", "medieval", "century", "war", "empire", "king",
    "queen", "civilization", "revolution", "world war", "dynasty", "emperor",
    "archaeological", "historical", "middle ages", "renaissance", "prehistoric",
    "civil war", "cold war", "rome", "egypt", "greece", "china", "mesopotamia",
    "pharaoh", "caesar", "viking", "ottoman", "byzantine", "mongol", "crusade",
    "independence", "conquest", "colonization", "monarchy", "republic"
]

# Generate chatbot response
def generate_response(user_input, max_length=100):
    input_text = f"question: {user_input}"

    input_ids = tokenizer(input_text, return_tensors='tf').input_ids
    
    outputs = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=0.90,
        temperature=0.6,
        do_sample=True
    )
    
    bot_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return bot_response

# Response formatting for better readability
def format_response(response):
    # Add periods at the end if missing
    if response and not response.endswith(('.', '!', '?')):
        response += '.'
    
    # Capitalize first letter
    if response:
        response = response[0].upper() + response[1:]
    
    return response

# Check if query is history-related
def is_history_related(query):
    return any(keyword.lower() in query.lower() for keyword in HISTORY_KEYWORDS)

# Generate fun historical fact
def get_random_fact():
    facts = [
        "The Ancient Egyptians used moldy bread as a treatment for infections!",
        "The shortest war in history was between Britain and Zanzibar in 1896. It lasted just 38 minutes.",
        "Vikings used a type of soap that made their beards look blonder.",
        "Ancient Romans used crushed mouse brains as toothpaste.",
        "The first recorded use of 'OMG' was in a 1917 letter to Winston Churchill.",
        "Napoleon was once attacked by thousands of rabbits when hunting.",
        "Cleopatra lived closer in time to the invention of the iPhone than to the building of the Great Pyramid.",
        "The ancient Olympics featured a running event where athletes competed in full armor."
    ]
    return random.choice(facts)

# Main chatbot function
def chatbot(message, history):
    if not message.strip():
        return "", history
    
    # Check if question is history-related
    if not is_history_related(message):
        response = "I'm a history chatbot. Please ask me about historical events, figures, or periods. Did you know? " + get_random_fact()
    else:
        try:
            raw_response = generate_response(message)
            response = format_response(raw_response)
        except Exception as e:
            response = f"I'm having trouble answering that historical question. Could you try rephrasing it? (Error: {str(e)})"
    
    return response, history + [[message, response]]

# Custom theme for Gradio
custom_theme = gr.themes.Soft(
    primary_hue="indigo",
    secondary_hue="amber",
    neutral_hue="slate"
).set(
    body_text_color="#333333",
    block_label_text_size="16px",
    block_title_text_size="20px"
)

# Function to provide suggestions for FAQs
def get_suggestion(btn_name):
    suggestions = {
        "Ancient Egypt": "Tell me about the construction of the Great Pyramids.",
        "Roman Empire": "What led to the fall of the Roman Empire?",
        "World Wars": "What were the main causes of World War I?",
        "Renaissance": "How did the Renaissance change Europe?",
        "Notable Figures": "Who was Genghis Khan and what was his impact on history?"
    }
    return suggestions.get(btn_name, "")

# Main Gradio interface
with gr.Blocks(theme=custom_theme) as demo:
    gr.Markdown(
        """
        # Historical Knowledge Chatbot 📚⏳
        
        *Your AI guide to exploring the past!*
        
        Ask questions about historical events, figures, periods, and discoveries from ancient civilizations to modern history.
        """
    )
    
    with gr.Row():
        with gr.Column(scale=3):
            chatbot_interface = gr.Chatbot(
                height=450,
                bubble_full_width=False,
                avatar_images=("https://i.ibb.co/G7J0qYh/user.png", "https://i.ibb.co/XJwZcdm/historian.png"),
                show_copy_button=True
            )
            
            with gr.Row():
                msg = gr.Textbox(
                    placeholder="Ask me about history...",
                    scale=8,
                    show_label=False,
                    container=False
                )
                submit_btn = gr.Button("Ask", variant="primary", scale=1)
            
            with gr.Row():
                clear_btn = gr.Button("Clear Chat", variant="secondary")
                
        with gr.Column(scale=1):
            gr.Markdown("### Popular Topics")
            btn1 = gr.Button("Ancient Egypt")
            btn2 = gr.Button("Roman Empire")
            btn3 = gr.Button("World Wars")
            btn4 = gr.Button("Renaissance")
            btn5 = gr.Button("Notable Figures")
            
            gr.Markdown("### About")
            gr.Markdown(
                """
                This chatbot uses a fine-tuned T5 model trained on historical Q&A data. 
                
                It's designed to answer questions about historical events, figures, and periods.
                
                _Last updated: February 2025_
                """
            )
    
    gr.Markdown("### Examples")
    with gr.Row():
        examples = gr.Examples(
            examples=[
                ["Who was Cleopatra and how did she become ruler of Egypt?"],
                ["How did the Black Death affect medieval Europe?"],
                ["Explain the significance of the Industrial Revolution."],
                ["What were the main causes of the American Civil War?"],
                ["Tell me about ancient Greek democracy."]
            ],
            inputs=msg
        )
    
    # Set up interactions
    submit_btn = gr.Button("Submit")
    submit_btn.click(chatbot, inputs=[msg, chatbot_interface], outputs=[msg, chatbot_interface])
    msg.submit(chatbot, inputs=[msg, chatbot_interface], outputs=[msg, chatbot_interface])
    clear_btn.click(lambda: None, None, chatbot_interface, queue=False)
    
    # Topic button interactions
    for btn in [btn1, btn2, btn3, btn4, btn5]:
        btn.click(
            get_suggestion,
            inputs=btn,
            outputs=msg
        )

# Launch the interface
if __name__ == "__main__":
    print("Starting History Chatbot...")
    demo.launch(share=True, debug=True)