"""
This is a simple application for sentence embeddings: semantic search

We have a corpus with various sentences. Then, for a given query sentence,
we want to find the most similar sentence in this corpus.

This script outputs for various queries the top 5 most similar sentences in the corpus.
"""
import time
start = time.time()

import torch

from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Corpus with example sentences
corpus = []
nice = {}

with open("NICE_tks.txt", encoding="utf-8") as fp:
    for line in fp:
        line = line.strip()

        id, text = line.split('\t')
        corpus.append(text)
        nice[text] = id


# Use "convert_to_tensor=True" to keep the tensors on GPU (if available)
print("Embedding corpus...")
corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)
print("Executing query")
# Query sentences:
queries = [
    "Skill in conducting vulnerability scans and recognizing vulnerabilities in information systems and networks",
    "Knowledge of application vulnerabilities.",    	
    "Ensure that AI design and development activities are properly documented and updated.",
    "Knowledge of the operations and processes for incident, problem, and event management.",
]

# Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
top_k = min(5, len(corpus))
for query in queries:
    query_embedding = embedder.encode(query, convert_to_tensor=True)

    # We use cosine-similarity and torch.topk to find the highest 5 scores
    similarity_scores = embedder.similarity(query_embedding, corpus_embeddings)[0]
    scores, indices = torch.topk(similarity_scores, k=top_k)

    print("\n8140 Query:", query)
    print("Top 5 most similar sentences in corpus:")

    for score, idx in zip(scores, indices):
        print(f"NICE ID: {nice[corpus[idx]]} (Score: {score:.4f}) \"{corpus[idx]}\"")

    """
    # Alternatively, we can also use util.semantic_search to perform cosine similarty + topk
    hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=5)
    hits = hits[0]      #Get the hits for the first query
    for hit in hits:
        print(corpus[hit['corpus_id']], "(Score: {:.4f})".format(hit['score']))
    """

print(f"That took {time.time()-start} s")
