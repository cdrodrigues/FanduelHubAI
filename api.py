from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer

app = FastAPI()

MODEL_ID = "meta-llama/Llama-3.2-3B-Instruct"
model = AutoModelForCausalLM.from_pretrained(MODEL_ID)
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

SYSTEM_HEAD = """You are tasked with answering questions regarding the provided documentation.
Answer ONLY with information found in the documentation.
Provide short and clear answers. Use Markdown to answer all the questions.

Documentation:

DOCUMENT_TEXT"""

document_text = "Our new applications currently utilize the updated DevXP Branching strategy, ... (your full doc here) ..."

class ChatHistory(BaseModel):
    messages: list  # List of {"role": ..., "content": ...}

@app.post("/chat")
def chat(history: ChatHistory):
    chat_template = tokenizer.apply_chat_template(history.messages, tokenize=False)
    inputs = tokenizer(chat_template, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=128)
    answer = tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
    return {"answer": answer}