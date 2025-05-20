# FandulHubAI

This project demonstrates how to load and interact with a Large Language Model (LLM) using Hugging Face's `transformers` library in a Jupyter Notebook or via a REST API server. The example uses the Llama-3.2-3B-Instruct model and provides code and instructions for setting up prompts and running chat-based interactions.

## Features
- Load and use the Llama-3.2-3B-Instruct model from Hugging Face
- Example of prompt engineering for documentation Q&A
- Step-by-step code in a Jupyter Notebook
- REST API server for chat-based interaction

## Requirements
Install the required Python packages:

```
pip install -r requirement.txt
```

## Usage

### Jupyter Notebook
1. Open `LLM.ipynb` in Jupyter Notebook or VS Code.
2. Follow the notebook cells to load the model, set up prompts, and interact with the LLM.

### REST API Server
1. Start the FastAPI server:
   ```
   uvicorn api:app --reload
   ```
2. Interact with the API using `curl` or any HTTP client. Example:
   ```
   curl -X POST "http://127.0.0.1:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"messages": [{"role": "system", "content": "You are..."}, {"role": "user", "content": "Hello!"}]}'
   ```

## Dependencies
- transformers
- torch
- tensorflow >= 2.0
- sentencepiece
- fastapi
- uvicorn

## License
Specify your license here (e.g., MIT, Apache 2.0, etc.)

---
Feel free to update this README with more details about your project, usage examples, or contribution guidelines.
