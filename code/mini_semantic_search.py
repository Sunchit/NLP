"""
Mini Semantic Search Engine
===========================

A simple semantic search engine that demonstrates:
1. Document indexing with vector embeddings
2. Semantic similarity search
3. Ranking and result presentation
4. Interactive search interface

This shows how modern search engines work under the hood!
"""

import spacy
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict, Tuple
import json
import time
from datetime import datetime

class MiniSemanticSearch:
    def __init__(self, model_name="en_core_web_lg"):
        """Initialize the search engine"""
        print(f"🚀 Initializing Mini Semantic Search Engine...")
        print(f"📦 Loading {model_name} model...")
        
        self.nlp = spacy.load(model_name)
        self.documents = []
        self.embeddings = []
        self.index = {}  # Document metadata
        
        print("✅ Search engine ready!")
    
    def add_document(self, doc_id: str, title: str, content: str, metadata: Dict = None):
        """Add a document to the search index"""
        if metadata is None:
            metadata = {}
        
        # Combine title and content for better search
        full_text = f"{title}. {content}"
        
        # Create embedding
        doc = self.nlp(full_text)
        embedding = doc.vector
        
        # Store document
        doc_info = {
            "id": doc_id,
            "title": title,
            "content": content,
            "full_text": full_text,
            "metadata": metadata,
            "indexed_at": datetime.now().isoformat(),
            "word_count": len(content.split())
        }
        
        self.documents.append(doc_info)
        self.embeddings.append(embedding)
        self.index[doc_id] = len(self.documents) - 1
        
        print(f"📄 Indexed: '{title}' (ID: {doc_id})")
    
    def search(self, query: str, top_k: int = 5, min_similarity: float = 0.5) -> List[Dict]:
        """Search for documents similar to the query"""
        if not self.documents:
            return []
        
        print(f"\n🔍 Searching for: '{query}'")
        start_time = time.time()
        
        # Create query embedding
        query_doc = self.nlp(query)
        query_embedding = query_doc.vector.reshape(1, -1)
        
        # Calculate similarities
        results = []
        for i, doc_embedding in enumerate(self.embeddings):
            doc_emb = doc_embedding.reshape(1, -1)
            similarity = cosine_similarity(query_embedding, doc_emb)[0][0]
            
            if similarity >= min_similarity:
                doc_info = self.documents[i].copy()
                doc_info["similarity"] = similarity
                doc_info["rank"] = 0  # Will be set after sorting
                results.append(doc_info)
        
        # Sort by similarity
        results.sort(key=lambda x: x["similarity"], reverse=True)
        
        # Add ranking
        for i, result in enumerate(results[:top_k]):
            result["rank"] = i + 1
        
        search_time = time.time() - start_time
        
        print(f"⏱️  Search completed in {search_time*1000:.2f}ms")
        print(f"📊 Found {len(results)} results (showing top {min(top_k, len(results))})")
        
        return results[:top_k]
    
    def display_results(self, results: List[Dict], show_content: bool = True):
        """Display search results in a formatted way"""
        if not results:
            print("❌ No results found!")
            return
        
        print(f"\n{'='*60}")
        print(f"🎯 SEARCH RESULTS ({len(results)} found)")
        print(f"{'='*60}")
        
        for result in results:
            print(f"\n🏆 Rank #{result['rank']} | Similarity: {result['similarity']:.3f}")
            print(f"📖 Title: {result['title']}")
            print(f"🆔 ID: {result['id']}")
            
            if show_content:
                # Show first 150 characters of content
                content_preview = result['content'][:150]
                if len(result['content']) > 150:
                    content_preview += "..."
                print(f"📝 Content: {content_preview}")
            
            if result['metadata']:
                print(f"🏷️  Tags: {result['metadata']}")
            
            print(f"📊 Words: {result['word_count']}")
            print("-" * 40)
    
    def get_stats(self) -> Dict:
        """Get search engine statistics"""
        return {
            "total_documents": len(self.documents),
            "total_words": sum(doc["word_count"] for doc in self.documents),
            "model_used": "en_core_web_lg",
            "vector_dimensions": len(self.embeddings[0]) if self.embeddings else 0,
            "index_size_mb": len(str(self.documents)) / (1024 * 1024)
        }
    
    def export_index(self, filename: str):
        """Export the search index to a JSON file"""
        export_data = {
            "documents": self.documents,
            "stats": self.get_stats(),
            "exported_at": datetime.now().isoformat()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Index exported to {filename}")

def create_sample_documents() -> List[Dict]:
    """Create a sample document collection for testing"""
    return [
        {
            "id": "tech001",
            "title": "Introduction to Machine Learning",
            "content": "Machine learning is a subset of artificial intelligence that enables computers to learn and improve from experience without being explicitly programmed. It uses algorithms to analyze data, identify patterns, and make predictions or decisions.",
            "metadata": {"category": "technology", "difficulty": "beginner", "tags": ["AI", "ML", "algorithms"]}
        },
        {
            "id": "tech002", 
            "title": "Deep Learning and Neural Networks",
            "content": "Deep learning uses artificial neural networks with multiple layers to model and understand complex patterns in data. It has revolutionized fields like computer vision, natural language processing, and speech recognition.",
            "metadata": {"category": "technology", "difficulty": "advanced", "tags": ["deep learning", "neural networks", "AI"]}
        },
        {
            "id": "sci001",
            "title": "The Science of Climate Change",
            "content": "Climate change refers to long-term shifts in global temperatures and weather patterns. Human activities, particularly burning fossil fuels, have increased greenhouse gas concentrations, leading to global warming and environmental impacts.",
            "metadata": {"category": "science", "difficulty": "intermediate", "tags": ["climate", "environment", "global warming"]}
        },
        {
            "id": "sci002",
            "title": "Photosynthesis in Plants",
            "content": "Photosynthesis is the process by which plants use sunlight, carbon dioxide, and water to produce glucose and oxygen. This process is essential for life on Earth as it produces the oxygen we breathe and forms the foundation of food chains.",
            "metadata": {"category": "science", "difficulty": "beginner", "tags": ["biology", "plants", "oxygen"]}
        },
        {
            "id": "hist001",
            "title": "The Renaissance Period",
            "content": "The Renaissance was a period of European cultural, artistic, political and economic rebirth following the Middle Ages. Lasting from the 14th to 17th century, it marked a renewed interest in classical learning, art, and humanism.",
            "metadata": {"category": "history", "difficulty": "intermediate", "tags": ["Europe", "art", "culture"]}
        },
        {
            "id": "tech003",
            "title": "Quantum Computing Fundamentals", 
            "content": "Quantum computing harnesses quantum mechanical phenomena like superposition and entanglement to process information. Unlike classical bits, quantum bits (qubits) can exist in multiple states simultaneously, potentially solving complex problems exponentially faster.",
            "metadata": {"category": "technology", "difficulty": "advanced", "tags": ["quantum", "computing", "physics"]}
        },
        {
            "id": "lang001",
            "title": "Natural Language Processing",
            "content": "Natural Language Processing (NLP) is a field of AI that focuses on enabling computers to understand, interpret, and generate human language. It combines computational linguistics with machine learning to process text and speech data.",
            "metadata": {"category": "technology", "difficulty": "intermediate", "tags": ["NLP", "linguistics", "text processing"]}
        },
        {
            "id": "cook001",
            "title": "The Art of Italian Cuisine",
            "content": "Italian cuisine is known for its regional diversity, fresh ingredients, and simple preparation methods. From pasta and pizza to risotto and gelato, Italian food emphasizes quality ingredients and traditional cooking techniques passed down through generations.",
            "metadata": {"category": "food", "difficulty": "beginner", "tags": ["Italian", "cooking", "traditional"]}
        },
        {
            "id": "space001",
            "title": "Exploring Mars: The Red Planet",
            "content": "Mars, the fourth planet from the Sun, has been a focus of space exploration due to its potential for past or present life. Recent missions have discovered evidence of ancient water flows and continue to search for signs of microbial life.",
            "metadata": {"category": "science", "difficulty": "intermediate", "tags": ["space", "Mars", "exploration"]}
        },
        {
            "id": "health001",
            "title": "Benefits of Regular Exercise",
            "content": "Regular physical exercise provides numerous health benefits including improved cardiovascular health, stronger bones and muscles, better mental health, and increased longevity. The WHO recommends at least 150 minutes of moderate exercise per week.",
            "metadata": {"category": "health", "difficulty": "beginner", "tags": ["fitness", "health", "wellness"]}
        }
    ]

def run_demo():
    """Run the semantic search engine demo"""
    print("=" * 70)
    print("🎯 MINI SEMANTIC SEARCH ENGINE DEMO")
    print("=" * 70)
    
    # Initialize search engine
    search_engine = MiniSemanticSearch()
    
    # Load sample documents
    print(f"\n📚 Loading sample documents...")
    documents = create_sample_documents()
    
    for doc in documents:
        search_engine.add_document(
            doc["id"],
            doc["title"], 
            doc["content"],
            doc["metadata"]
        )
    
    # Show statistics
    stats = search_engine.get_stats()
    print(f"\n📊 Search Engine Statistics:")
    print(f"   Documents: {stats['total_documents']}")
    print(f"   Total words: {stats['total_words']:,}")
    print(f"   Vector dimensions: {stats['vector_dimensions']}")
    print(f"   Index size: {stats['index_size_mb']:.2f} MB")
    
    # Sample searches
    sample_queries = [
        "artificial intelligence and machine learning",
        "how do plants make oxygen",
        "space exploration and planets", 
        "cooking traditional food",
        "health benefits of exercise",
        "quantum computers and physics",
        "climate change and environment"
    ]
    
    print(f"\n🔍 Running sample searches...")
    print("=" * 70)
    
    for i, query in enumerate(sample_queries, 1):
        print(f"\n[SEARCH {i}/{len(sample_queries)}]")
        results = search_engine.search(query, top_k=3)
        search_engine.display_results(results, show_content=False)
        
        if i < len(sample_queries):
            input("\n⏯️  Press Enter for next search...")
    
    # Interactive search
    print(f"\n🎮 INTERACTIVE SEARCH MODE")
    print("Enter your own search queries! (type 'quit' to exit)")
    print("=" * 70)
    
    while True:
        try:
            query = input("\n🔍 Search query: ").strip()
            
            if query.lower() in ['quit', 'exit', 'q']:
                break
                
            if not query:
                continue
            
            results = search_engine.search(query, top_k=5)
            search_engine.display_results(results)
            
        except KeyboardInterrupt:
            break
    
    # Export option
    export_choice = input("\n💾 Export search index? (y/n): ").strip().lower()
    if export_choice == 'y':
        search_engine.export_index("search_index.json")
    
    print("\n🎉 Thanks for trying the Mini Semantic Search Engine!")

def quick_search_test():
    """Quick test function for development"""
    search_engine = MiniSemanticSearch()
    
    # Add just a few documents for quick testing
    search_engine.add_document("1", "AI Basics", "Artificial intelligence and machine learning concepts")
    search_engine.add_document("2", "Plant Biology", "How plants perform photosynthesis using sunlight")
    search_engine.add_document("3", "Space Science", "Mars exploration and planetary research")
    
    # Test search
    results = search_engine.search("artificial intelligence", top_k=2)
    search_engine.display_results(results)

if __name__ == "__main__":
    # Run full demo
    run_demo()
    
    # Uncomment for quick testing:
    # quick_search_test()
