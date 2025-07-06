from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle

model = SentenceTransformer('all-MiniLM-L6-v2')
index_file = 'offline_embeddings/faiss_index.bin'
doc_map_file = 'offline_embeddings/doc_map.pkl'

if os.path.exists(index_file):
    with open(index_file, 'rb') as f:
        index = faiss.read_index(faiss.IOReader(f))
    with open(doc_map_file, 'rb') as f:
        doc_map = pickle.load(f)
else:
    index = faiss.IndexFlatL2(384)
    doc_map = []

def embed_text(text):
    return model.encode([text])[0]

def add_document(text, metadata):
    vector = embed_text(text)
    index.add(np.array([vector]))
    doc_map.append(metadata)
    with open(index_file, 'wb') as f:
        faiss.write_index(index, faiss.PyCallbackIOWriter(f.write))
    with open(doc_map_file, 'wb') as f:
        pickle.dump(doc_map, f)

def query_similar(text, top_k=3):
    vector = embed_text(text)
    D, I = index.search(np.array([vector]), top_k)
    return [doc_map[i] for i in I[0] if i < len(doc_map)]

def get_openai_response(query, context):
    return f"OpenAI simulated response based on context:\n{context}"
