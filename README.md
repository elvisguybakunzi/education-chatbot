# Historical Knowledge Chatbot

A specialized chatbot built using the T5 transformer model, fine-tuned on historical Q&A data to provide accurate and informative responses about various historical topics, figures, and events.

### **[Watch The Demo Video](https://www.youtube.com/watch?v=ejDmbRCJPOQ)**

[https://www.youtube.com/watch?v=ejDmbRCJPOQ](https://www.youtube.com/watch?v=ejDmbRCJPOQ)

## 📌 Overview

The Historical Knowledge Chatbot is an AI-powered conversational agent designed to help users explore historical topics through natural language interaction. The chatbot can answer questions about a wide range of historical subjects, including ancient civilizations, significant events, notable figures, and cultural developments throughout human history.

## ✨ Features

- **Domain-Specific Knowledge**: Trained specifically on historical data to provide accurate responses
- **Interactive UI**: User-friendly Gradio interface with chat history and example suggestions
- **Topic Filtering**: Intelligently recognizes history-related queries
- **Contextual Responses**: Generates informative and coherent answers to historical questions
- **Educational Tool**: Perfect for students, educators, history enthusiasts, and curious minds

## 🛠️ Technologies Used

- **Model Architecture**: T5 Transformer
- **Training Framework**: TensorFlow
- **User Interface**: Gradio
- **Natural Language Processing**: NLTK, Transformers
- **Evaluation Metrics**: BLEU, ROUGE, Custom Accuracy

## 🚀 Getting Started

### Prerequisites

```bash
pip install transformers tensorflow gradio nltk rouge-score datasets langdetect
```

### Installation and Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/elvisguybakunzi/education-chatbot
   cd education-chatbot
   ```

2. Download the trained model:
   - The model is on google drive
   - There is bash file to help download the model
   
   Run the following command to download the model:
   ```sh
   bash download_model.sh
   ```

3. Run the Gradio UI:
   ```bash
   # first enter the gradio_ui directory
   cd gradio_ui
   # run the Gradio UI
   python app.py
   ```

4. Access the chatbot interface at `http://127.0.0.1:7860`

## 📊 Model Training

The chatbot was trained on a dataset of 20,000 historical question-answer pairs. The training process involved:

1. **Data Collection**: Historical Q&A pairs from various sources
2. **Preprocessing**: Formatting inputs as "question: {text}" and targets as direct answers
3. **Fine-tuning**: Using the T5-small base model with custom hyperparameters
4. **Evaluation**: Testing on a held-out dataset with BLEU, ROUGE, and exact match metrics

## 📝 Sample Interactions

```
User: Who was Cleopatra?
Bot: Cleopatra VII was the last active ruler of the Ptolemaic Kingdom of Egypt. She was known for her intelligence, charm, and political alliances with Julius Caesar and Mark Antony of Rome.

User: What caused World War I?
Bot: World War I was triggered by the assassination of Archduke Franz Ferdinand but had deeper causes including nationalism, imperialism, militarism, and complex alliances between European powers that escalated a regional conflict into a global war.
```

## 📈 Performance Metrics

- **BLEU Score**: 0.42
- **ROUGE-L Score**: 0.64
- **Exact Match Accuracy**: 0.18

## 🔍 Limitations

- The chatbot's knowledge is limited to the historical data it was trained on
- It may occasionally give simplified answers to complex historical questions
- The model works best with clearly formulated questions about well-documented historical topics

## 🔮 Future Improvements

- Incorporate a larger and more diverse historical dataset
- Implement a retrieval-augmented generation approach for more accurate responses
- Add multilingual support for questions in different languages
- Improve the handling of controversial or debated historical topics

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- The Hugging Face team for their Transformers library
- The Gradio team for their easy-to-use UI framework
- All contributors to the historical dataset used for training

## 👥 Contact

For questions or feedback about this project, please contact:
- Email: e.bakunzi@alustudent.com