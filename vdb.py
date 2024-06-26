from vector_store import VectorStore
import numpy as np

# Instantiate
vector_store = VectorStore()

# Get some sentences

sentences = [
    "Goku and Vegeta are rivals.",
    "Luffy will become the pirate king.",
    "Naruto is the 7th Hokage.",
]


# Vocab creation and tokenization
vocabulary = set()

for sentence in sentences:
    tokens = sentence.lower().split()
    vocabulary.update(tokens)

# Assign indices to vocab words
word_to_index = {word: i for i, word in enumerate(vocabulary)}

# Vectorization
sentence_vectors = {}  # An empty dictionary to store the senteces

for sentence in sentences:
    tokens = sentence.lower().split()
    vector = np.zeros(len(vocabulary))
    for token in tokens:
        vector[word_to_index[token]] += 1
    sentence_vectors[sentence] = vector

# Store in VectorStore
for sentence, vector in sentence_vectors.items():
    vector_store.add_vector(sentence, vector)

# Similarity search
query_sentence = str(input("Enter the query sentence : "))
query_vector = np.zeros(len(vocabulary))
query_tokens = query_sentence.lower().split()
for token in query_tokens:
    if token in word_to_index:
        query_vector[word_to_index[token]] += 1

similar_sentences = vector_store.find_similar_vectors(query_vector=query_vector, num_results=2)

print(f"Query_sentence : {query_sentence}")
print(f"Similar sentences : ")
for sentence, similarity in similar_sentences:
    print(f"{sentence} : Similarity : {similarity:.4f}")