"""
This is a simple application for sentence embeddings: semantic search

We have a corpus with various sentences. Then, for a given query sentence,
we want to find the most similar sentence in this corpus.

This script outputs for various queries the top 5 most similar sentences in the corpus.
"""
import time
start = time.time()



NICE_corpus = []
NICE_text_to_ids = {}

with open("NICE_tasks.txt", encoding="utf-8") as fp:
    for line in fp:
        line = line.strip()

        id, text = line.split('\t')
        NICE_corpus.append(text)
        NICE_text_to_ids[text] = id

# Query sentences:
DOD_corpus = []
DOD_text_to_ids = {}
with open("DOD_8140_ksats.txt", encoding="utf-8") as fp:
    for line in fp:
        line = line.strip()
        print(line)
        id, text = line.split('\t')
        DOD_corpus.append(text)
        DOD_text_to_ids[text] = id

# Use "convert_to_tensor=True" to keep the tensors on GPU (if available)
import torch

from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding NICE tasks...")
corpus_embeddings = embedder.encode(NICE_corpus, convert_to_tensor=True)


# Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
top_k = min(5, len(NICE_corpus))
for ksat in DOD_corpus:
    query_embedding = embedder.encode(ksat, convert_to_tensor=True)

    # We use cosine-similarity and torch.topk to find the highest 5 scores
    similarity_scores = embedder.similarity(query_embedding, corpus_embeddings)[0]
    scores, indices = torch.topk(similarity_scores, k=top_k)

    print(f"\n8140 KSAT #{DOD_text_to_ids[ksat]}: {ksat}")
    print("Top 5 most similar CISA NICE tasks:")

    for score, idx in zip(scores, indices):
        print(f"NICE ID: {NICE_text_to_ids[NICE_corpus[idx]]} (Score: {score:.4f}) \"{NICE_corpus[idx]}\"")

    """
    # Alternatively, we can also use util.semantic_search to perform cosine similarty + topk
    hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=5)
    hits = hits[0]      #Get the hits for the first query
    for hit in hits:
        print(corpus[hit['corpus_id']], "(Score: {:.4f})".format(hit['score']))
    """

print(f"That took {time.time()-start} s")
