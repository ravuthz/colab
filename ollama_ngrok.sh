#!/bin/sh

# Download and run the Ollama Linux install script
curl -fsSL https://ollama.com/install.sh | sh > /dev/null 2>&1

# Install requirement packages
pip install aiohttp pyngrok

wget https://raw.githubusercontent.com/ravuthz/colab/master/ollama_ngrok.py
python ./ollama_ngrok.py
