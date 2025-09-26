import spacy

# Load the large English model (with word vectors)
print("Loading spaCy model...")
nlp = spacy.load("en_core_web_lg")

print("=== SIMPLE EMBEDDING DEMO ===\n")

# Simple sentences to compare
sentence1 = "I love pizza"
sentence2 = "Pizza is delicious"
sentence3 = "The weather is sunny"

# Process the sentences
doc1 = nlp(sentence1)
doc2 = nlp(sentence2)
doc3 = nlp(sentence3)

print("Comparing these sentences:")
print(f"1. '{sentence1}'")
print(f"2. '{sentence2}'")
print(f"3. '{sentence3}'")

print("\nSimilarity Results:")
print(f"Pizza in sentence #1 vs Pizza in sentence #2: {doc1.similarity(doc2):.3f}")
print(f"Pizza in sentence #1 vs Weather in sentence #3: {doc1.similarity(doc3):.3f}")
print(f"Pizza in sentence #2 vs Weather in sentence #3: {doc2.similarity(doc3):.3f}")

print("\nWhat this means:")
print("- Higher numbers (closer to 1.0) = more similar")
print("- Lower numbers (closer to 0.0) = less similar")
print("- Pizza sentences should be more similar to each other!")
