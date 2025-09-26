import spacy

nlp_md = spacy.load('en_core_web_md')
nlp_lg = spacy.load('en_core_web_lg')

word = 'king'
vector_md = nlp_md(word).vector
vector_lg = nlp_lg(word).vector

print(f'Word: \"{word}\"')
print(f'Medium model vector shape: {vector_md.shape}')
print(f'Large model vector shape:  {vector_lg.shape}')
print(f'First 5 dimensions (md): {vector_md[:5]}')
print(f'First 5 dimensions (lg): {vector_lg[:5]}')
