import spacy

print("=== SPACY MODEL COMPARISON ===\n")

# Model specifications table
models = [
    {
        "name": "en_core_web_sm",
        "size": "12.8 MB",
        "vectors": "❌ No word vectors",
        "dimensions": "96",
        "similarity": "⚠️ Limited (uses parser/NER)",
        "speed": "🚀 Fastest",
        "use_case": "Basic NLP, fast processing"
    },
    {
        "name": "en_core_web_md", 
        "size": "50 MB",
        "vectors": "⚡ Some word vectors",
        "dimensions": "300",
        "similarity": "✅ Good",
        "speed": "⚡ Fast",
        "use_case": "Balanced performance"
    },
    {
        "name": "en_core_web_lg",
        "size": "400+ MB", 
        "vectors": "✅ Full word vectors",
        "dimensions": "300",
        "similarity": "🎯 Best",
        "speed": "🐌 Slower",
        "use_case": "Best embeddings & similarity"
    }
]

# Print comparison table
print("┌─────────────────┬──────────┬─────────────────────┬────────────┬──────────────┬───────────┬─────────────────────┐")
print("│ Model           │ Size     │ Word Vectors        │ Dimensions │ Similarity   │ Speed     │ Best Use Case       │")
print("├─────────────────┼──────────┼─────────────────────┼────────────┼──────────────┼───────────┼─────────────────────┤")

for model in models:
    print(f"│ {model['name']:<15} │ {model['size']:<8} │ {model['vectors']:<19} │ {model['dimensions']:<10} │ {model['similarity']:<12} │ {model['speed']:<9} │ {model['use_case']:<19} │")

print("└─────────────────┴──────────┴─────────────────────┴────────────┴──────────────┴───────────┴─────────────────────┘")

print("\n=== WHAT WE'RE USING ===")
print("Current model: en_core_web_lg")
print("Why: Best for semantic similarity and embeddings!")

print("\n=== QUICK FEATURE COMPARISON ===")
features = [
    "Feature",
    "Tokenization", 
    "POS Tagging",
    "Named Entity Recognition",
    "Dependency Parsing", 
    "Word Vectors",
    "Similarity Calculation"
]

sm_features = ["Small", "✅", "✅", "✅", "✅", "❌", "⚠️ Parser-based"]
md_features = ["Medium", "✅", "✅", "✅", "✅", "⚡ Partial", "✅ Good"]
lg_features = ["Large", "✅", "✅", "✅", "✅", "✅ Full", "🎯 Excellent"]

print(f"\n{'Feature':<25} {'Small':<15} {'Medium':<15} {'Large':<15}")
print("-" * 70)
for i in range(1, len(features)):
    print(f"{features[i]:<25} {sm_features[i]:<15} {md_features[i]:<15} {lg_features[i]:<15}")

print("\n=== RECOMMENDATION ===")
print("🎯 For embeddings & similarity: Use en_core_web_lg (what we're using)")
print("⚡ For speed & basic NLP: Use en_core_web_sm") 
print("🔀 For balanced performance: Use en_core_web_md")
