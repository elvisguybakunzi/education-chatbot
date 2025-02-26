#!/bin/bash

# Install gdown if not installed
pip install gdown

# Download model.zip from Google Drive
gdown --id 1jbscUpoGT4gE7sE6NQbZIL_U1aZ2-w7Y -O model.zip

# Extract model.zip
unzip model.zip

# Remove model.zip
rm model.zip

echo "✅ Model folder downloaded and extracted successfully!"
