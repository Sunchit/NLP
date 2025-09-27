"""
🤖 SIMPLE RAG DEMO FOR STUDENTS
=====================================

What is RAG?
- R: Retrieval (Find relevant information)
- A: Augmented (Add it to your question) 
- G: Generation (Create a smart answer)

Think of it like having a smart assistant that:
1. Searches through books to find relevant pages
2. Reads those pages to understand the context
3. Gives you an answer based on what it found

This demo uses simple Python libraries that students can understand!
"""

import json
from datetime import datetime
from typing import List, Dict   

class StudentRAG:
    """A SIMPLE RAG system that students can understand"""
    
    def __init__(self):
        print("🚀 Starting Simple RAG System...")
        print("=" * 50)
        
        # Our "database" - just a list of documents
        self.knowledge_base = []
        self.document_count = 0
        
        print("✅ RAG System Ready!")
        print("📚 Knowledge Base: Empty (ready to add documents)")
        print()
    
    def add_document(self, title: str, content: str, category: str = "general"):
        """Add a document to our knowledge base"""
        doc_id = self.document_count
        
        document = {
            "id": doc_id,
            "title": title,
            "content": content,
            "category": category,
            "added_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "word_count": len(content.split())
        }
        
        self.knowledge_base.append(document)
        self.document_count += 1
        
        print(f"📄 Added: '{title}' ({len(content.split())} words)")
        return doc_id
    
    def simple_search(self, query: str, max_results: int = 3) -> List[Dict]:
        """
        SIMPLE search - just look for matching words!
        Real RAG systems use embeddings, but this helps students understand the concept.
        """
        print(f"🔍 Searching for: '{query}'")
        print("-" * 30)
        
        # Convert query to lowercase words
        query_words = query.lower().split()
        results = []
        
        # Check each document
        for doc in self.knowledge_base:
            # Count how many query words appear in the document
            doc_text = (doc["title"] + " " + doc["content"]).lower()
            
            matches = 0
            matched_words = []
            
            for word in query_words:
                if word in doc_text:
                    matches += 1
                    matched_words.append(word)
            
            # Calculate simple relevance score
            relevance = matches / len(query_words) if query_words else 0
            
            if matches > 0:  # Only include documents with at least one match
                results.append({
                    "document": doc,
                    "relevance_score": relevance,
                    "matched_words": matched_words,
                    "match_count": matches
                })
        
        # Sort by relevance (highest first)
        results.sort(key=lambda x: x["relevance_score"], reverse=True)
        
        # Show search results
        print(f"📊 Found {len(results)} relevant documents:")
        for i, result in enumerate(results[:max_results], 1):
            doc = result["document"]
            score = result["relevance_score"]
            matches = result["matched_words"]
            
            print(f"  {i}. '{doc['title']}' (Score: {score:.2f})")
            print(f"     Category: {doc['category']}")
            print(f"     Matched words: {', '.join(matches)}")
            print(f"     Preview: {doc['content'][:100]}...")
            print()
        
        return results[:max_results]
    
    def generate_answer(self, query: str, search_results: List[Dict]) -> str:
        """
        Generate an answer based on retrieved documents.
        This is simplified - real systems use AI models like GPT!
        """
        if not search_results:
            return "❌ Sorry, I couldn't find any relevant information in my knowledge base."
        
        print("🧠 Generating answer from retrieved documents...")
        print("-" * 40)
        
        # Combine information from top documents
        answer_parts = []
        sources_used = []
        
        for result in search_results:
            doc = result["document"]
            content = doc["content"]
            
            # Extract relevant sentences (simple approach)
            sentences = content.split('. ')
            relevant_sentences = []
            
            query_words = query.lower().split()
            
            for sentence in sentences:
                sentence_lower = sentence.lower()
                # If sentence contains query words, it's probably relevant
                if any(word in sentence_lower for word in query_words):
                    relevant_sentences.append(sentence.strip())
            
            if relevant_sentences:
                # Take the first relevant sentence from each document
                answer_parts.append(relevant_sentences[0])
                sources_used.append(doc["title"])
        
        # Combine into a coherent answer
        if answer_parts:
            answer = "Based on my knowledge base: " + " ".join(answer_parts)
            if not answer.endswith('.'):
                answer += "."
            
            # Add sources
            answer += f"\n\n📚 Sources: {', '.join(sources_used)}"
        else:
            answer = "I found relevant documents but couldn't extract a specific answer. Please try rephrasing your question."
        
        return answer
    
    def ask_question(self, question: str) -> Dict:
        """
        Complete RAG pipeline: Search + Generate Answer
        This is the main function that students will use!
        """
        print("🎯 RAG PIPELINE STARTING")
        print("=" * 50)
        print(f"❓ Question: {question}")
        print()
        
        # Step 1: RETRIEVAL - Find relevant documents
        print("STEP 1: 🔍 RETRIEVAL")
        search_results = self.simple_search(question, max_results=3)
        
        if not search_results:
            return {
                "question": question,
                "answer": "No relevant documents found.",
                "sources": [],
                "success": False
            }
        
        print()
        
        # Step 2: AUGMENTATION - Prepare context
        print("STEP 2: 📝 AUGMENTATION")
        print("Preparing context from retrieved documents...")
        context_docs = [result["document"] for result in search_results]
        print(f"✅ Using {len(context_docs)} documents as context")
        print()
        
        # Step 3: GENERATION - Create answer
        print("STEP 3: 🤖 GENERATION")
        answer = self.generate_answer(question, search_results)
        
        print("✅ Answer generated!")
        print()
        print("🎉 FINAL RESULT:")
        print("-" * 20)
        print(answer)
        print()
        
        return {
            "question": question,
            "answer": answer,
            "sources": [doc["title"] for doc in context_docs],
            "search_results": search_results,
            "success": True
        }
    
    def show_knowledge_base(self):
        """Display all documents in the knowledge base"""
        print("📚 KNOWLEDGE BASE CONTENTS")
        print("=" * 40)
        
        if not self.knowledge_base:
            print("❌ Knowledge base is empty!")
            return
        
        for doc in self.knowledge_base:
            print(f"📄 ID: {doc['id']}")
            print(f"   Title: {doc['title']}")
            print(f"   Category: {doc['category']}")
            print(f"   Words: {doc['word_count']}")
            print(f"   Added: {doc['added_at']}")
            print(f"   Content: {doc['content'][:100]}...")
            print()

def create_student_knowledge_base():
    """Create a simple knowledge base with topics students can relate to"""
    
    rag = StudentRAG()
    
    print("📚 Building Student Knowledge Base...")
    print("=" * 50)
    
    # Add documents about topics students might ask about
    documents = [
        {
            "title": "What is Python?",
            "content": "Python is a programming language that is easy to learn and powerful to use. It was created by Guido van Rossum in 1991. Python is great for beginners because its syntax is simple and readable. You can use Python for web development, data science, artificial intelligence, and automation. Many companies like Google, Netflix, and Instagram use Python.",
            "category": "programming"
        },
        {
            "title": "How Machine Learning Works",
            "content": "Machine learning is a way to teach computers to learn patterns from data without explicitly programming every rule. Instead of writing specific instructions, we show the computer lots of examples and let it figure out the patterns. For example, to teach a computer to recognize cats in photos, we show it thousands of cat pictures and it learns what features make a cat.",
            "category": "AI"
        },
        {
            "title": "What are Vector Embeddings?",
            "content": "Vector embeddings are a way to convert words, sentences, or any text into numbers that computers can understand. Think of it like translating human language into math. Similar words get similar numbers. For example, 'king' and 'queen' would have similar vector embeddings because they are both royal titles. This helps computers understand meaning and relationships between words.",
            "category": "AI"
        },
        {
            "title": "Climate Change Basics",
            "content": "Climate change refers to long-term changes in Earth's weather patterns and temperatures. The main cause is human activities that release greenhouse gases like carbon dioxide into the atmosphere. These gases trap heat from the sun, making Earth warmer. This leads to melting ice caps, rising sea levels, and more extreme weather events like hurricanes and droughts.",
            "category": "science"
        },
        {
            "title": "How the Internet Works",
            "content": "The internet is a global network of connected computers that can share information. When you visit a website, your computer sends a request through your internet provider to servers around the world. These servers store website data and send it back to your computer. The data travels through cables, fiber optics, and wireless signals to reach you in seconds.",
            "category": "technology"
        },
        {
            "title": "Photosynthesis Explained",
            "content": "Photosynthesis is how plants make their own food using sunlight, water, and carbon dioxide from the air. Plants have special cells called chloroplasts that contain chlorophyll, which captures sunlight. The plant combines the sunlight energy with water from roots and carbon dioxide from air to create glucose (sugar) for energy and oxygen as a byproduct.",
            "category": "biology"
        },
        {
            "title": "Social Media and Mental Health",
            "content": "Social media can affect mental health in both positive and negative ways. Positive effects include staying connected with friends and finding supportive communities. Negative effects can include comparison with others, cyberbullying, and addiction to likes and comments. It's important to use social media mindfully and take breaks when needed.",
            "category": "health"
        },
        {
            "title": "Study Tips for Students",
            "content": "Effective studying involves several strategies. First, create a quiet study space free from distractions. Use active learning techniques like summarizing information in your own words or teaching concepts to someone else. Take regular breaks using the Pomodoro technique (25 minutes study, 5 minute break). Practice spaced repetition by reviewing material multiple times over several days.",
            "category": "education"
        }
    ]
    
    # Add all documents to the knowledge base
    for doc in documents:
        rag.add_document(doc["title"], doc["content"], doc["category"])
    
    print(f"\n✅ Knowledge base created with {len(documents)} documents!")
    print("🎓 Ready for student questions!")
    return rag

def run_student_demo():
    """Run an interactive demo perfect for students"""
    
    print("🎓 WELCOME TO RAG FOR STUDENTS!")
    print("=" * 60)
    print("This demo shows how AI systems like ChatGPT find and use information")
    print("to answer your questions. Let's see how it works step by step!")
    print()
    
    # Create the knowledge base
    rag = create_student_knowledge_base()
    
    # Show what's in our knowledge base
    print("\n" + "="*60)
    rag.show_knowledge_base()
    
    # Pre-defined questions to demonstrate
    sample_questions = [
        "What is Python programming?",
        "How does machine learning work?", 
        "What causes climate change?",
        "How do plants make food?",
        "How can I study better?"
    ]
    
    print("\n" + "="*60)
    print("🚀 DEMO: Let's try some sample questions!")
    print("="*60)
    
    for i, question in enumerate(sample_questions, 1):
        print(f"\n🎯 DEMO QUESTION {i}: {question}")
        print("="*80)
        
        result = rag.ask_question(question)
        
        input("\n⏸️  Press Enter to continue to next question...")
        print("\n" + "="*80)
    
    # Interactive mode for students to ask their own questions
    print("\n🎮 YOUR TURN! Ask your own questions!")
    print("="*60)
    print("Try asking about:")
    print("- Programming (Python, coding)")
    print("- Science (climate, biology, technology)")  
    print("- AI and machine learning")
    print("- Study tips")
    print("- Or anything else in the knowledge base!")
    print("\nType 'quit' when you're done.")
    print("-"*60)
    
    while True:
        try:
            user_question = input("\n🤔 Your question: ").strip()
            
            if user_question.lower() in ['quit', 'exit', 'q', 'done']:
                break
                
            if not user_question:
                print("Please enter a question!")
                continue
            
            print("\n" + "="*80)
            result = rag.ask_question(user_question)
            print("="*80)
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please try asking your question differently.")
    
    print("\n🎉 Thanks for trying the Student RAG Demo!")
    print("Now you understand how AI systems retrieve and use information!")
    print("🚀 This is the same basic process used by ChatGPT, Google, and other AI tools!")

if __name__ == "__main__":
    run_student_demo()
