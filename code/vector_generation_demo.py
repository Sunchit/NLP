import spacy

nlp_lg = spacy.load('en_core_web_lg')
nlp_md = spacy.load('en_core_web_md')

word = 'king'
vector_lg = nlp_lg(word).vector
vector_md = nlp_md(word).vector
print(f'Word: \"{word}\"')
print(f'Large model vector shape:  {vector_lg.shape}')
print(f'First 5 dimensions (lg): {vector_lg[:5]}')


print(f'Medium model vector shape:  {vector_md.shape}')
print(f'First 5 dimensions (lg): {vector_md[:5]}')
