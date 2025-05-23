from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
from utils import load_and_chunk_docs, retrieve_relevant_chunks
from fastapi.middleware.cors import CORSMiddleware
from sentence_transformers import SentenceTransformer

app = FastAPI()

origins = [
    "https://localhost:4443",
    "https://localhost",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_ID = "meta-llama/Llama-3.2-3B-Instruct"
model = AutoModelForCausalLM.from_pretrained(MODEL_ID)
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

EMBED_MODEL = "all-MiniLM-L6-v2"
embedder = SentenceTransformer(EMBED_MODEL)

SYSTEM_HEAD = """You are tasked with answering questions regarding the provided documentation.
Answer ONLY with information found in the documentation.
Provide short and clear answers. Use Markdown to answer all the questions.

Documentation:

DOCUMENT_TEXT"""

DOCS_PATH = "docs"
CHUNK_SIZE = 500  # characters

doc_chunks, doc_sources = load_and_chunk_docs(DOCS_PATH, CHUNK_SIZE)
doc_embeddings = embedder.encode(doc_chunks, convert_to_numpy=True)

class ChatHistory(BaseModel):
    messages: list

@app.post("/chat")
def chat(history: ChatHistory):
    user_query = history.messages[-1]["content"] if history.messages else ""
    relevant_chunks = retrieve_relevant_chunks(user_query, doc_chunks, doc_embeddings, embedder, k=3)
    print(f"Relevant chunks: {relevant_chunks}")
    context = "\n\n".join(relevant_chunks)
    system_message = {"role": "system", "content": history.messages[0]['content'] + SYSTEM_HEAD.replace("DOCUMENT_TEXT", context)}
    full_history = [system_message] + history.messages[1:]
    print(f"Full history: {full_history}")
    chat_template = tokenizer.apply_chat_template(full_history, tokenize=False)
    inputs = tokenizer(chat_template, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=1024, do_sample=True, temperature=0.7, top_p=0.9, top_k=50)
    answer = tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
    return {"answer": answer}