import os

def load_docs_text(docs_folder="docs"):
    """Load and concatenate all markdown files in the given docs folder."""
    docs_text = []
    for filename in os.listdir(docs_folder):
        if filename.endswith(".md"):
            with open(os.path.join(docs_folder, filename), "r", encoding="utf-8") as f:
                docs_text.append(f.read())
    return "\n\n".join(docs_text)
