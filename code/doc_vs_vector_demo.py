import spacy

nlp_lg = spacy.load('en_core_web_lg')

# Full sentence
doc = nlp_lg("I love pizza")

# Single word
doc_word = nlp_lg("pizza")

print(len(doc))        # 3 tokens
print(len(doc_word))   # 1 token

# Vectors
print(doc[2].vector)       # "pizza" inside the sentence
print(doc_word[0].vector)  # "pizza" as its own input
