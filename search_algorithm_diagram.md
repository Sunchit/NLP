# Mini Semantic Search Engine Algorithm Diagram

## 🎯 High-Level Algorithm Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MINI SEMANTIC SEARCH ENGINE                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   📚 INDEXING   │    │   🔍 SEARCHING  │    │   📊 RANKING    │
│     PHASE       │    │      PHASE      │    │     PHASE       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

---

## 📚 Phase 1: Document Indexing Process

```
INPUT DOCUMENTS
┌─────────────────────────────────────────────────────────────────┐
│ Doc 1: "Machine Learning Basics"                               │
│ "ML is a subset of AI that enables computers to learn..."      │
│                                                                 │
│ Doc 2: "Climate Change Science"                                │
│ "Climate change refers to long-term shifts in temperature..."  │
│                                                                 │
│ Doc 3: "Italian Cooking Traditions"                           │
│ "Italian cuisine emphasizes fresh ingredients and..."          │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                    🧠 SPACY NLP MODEL                          │
│                   (en_core_web_lg)                             │
│                                                                 │
│   Text Processing Pipeline:                                     │
│   ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐                    │
│   │Token│→│ POS │→│Parse│→│ NER │→│Vec  │                    │
│   │ize  │ │Tag  │ │     │ │     │ │tor  │                    │
│   └─────┘ └─────┘ └─────┘ └─────┘ └─────┘                    │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                    VECTOR EMBEDDINGS                           │
│                    (300 dimensions each)                        │
│                                                                 │
│ Doc 1: [0.23, -0.45, 0.67, 0.12, -0.34, ..., 0.89]          │
│ Doc 2: [-0.12, 0.78, -0.23, 0.56, 0.45, ..., -0.67]         │
│ Doc 3: [0.45, 0.23, -0.89, -0.12, 0.67, ..., 0.34]          │
│                                                                 │
│        💾 STORED IN MEMORY FOR FAST ACCESS                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔍 Phase 2: Search Query Processing

```
USER QUERY
┌─────────────────────────────────────────────────────────────────┐
│                "artificial intelligence"                        │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                🧠 SAME NLP MODEL                               │
│                                                                 │
│   Query → Tokens → POS → Parse → NER → Vector                 │
│                                                                 │
│   "artificial intelligence" → [0.34, -0.23, 0.78, ...]       │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                 🎯 SIMILARITY CALCULATION                       │
│                                                                 │
│   Query Vector: [0.34, -0.23, 0.78, 0.45, -0.12, ...]        │
│                                                                 │
│   ╔═══════════════════════════════════════════════════════════╗ │
│   ║              COSINE SIMILARITY FORMULA                   ║ │
│   ║                                                           ║ │
│   ║    similarity = (A · B) / (||A|| × ||B||)               ║ │
│   ║                                                           ║ │
│   ║    Where:                                                 ║ │
│   ║    A = Query vector                                       ║ │
│   ║    B = Document vector                                    ║ │
│   ║    · = Dot product                                        ║ │
│   ║    |||| = Vector magnitude                               ║ │
│   ╚═══════════════════════════════════════════════════════════╝ │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🧮 Detailed Similarity Calculation

```
VECTOR COMPARISON PROCESS
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  Query:    [0.34, -0.23,  0.78,  0.45, -0.12, ...]           │
│             ↓      ↓      ↓      ↓      ↓                      │
│  Doc 1:    [0.23, -0.45,  0.67,  0.12, -0.34, ...]           │
│  Similarity: 0.89 ⭐⭐⭐⭐⭐ (HIGH - ML content)                │
│                                                                 │
│  Query:    [0.34, -0.23,  0.78,  0.45, -0.12, ...]           │
│             ↓      ↓      ↓      ↓      ↓                      │
│  Doc 2:    [-0.12, 0.78, -0.23,  0.56,  0.45, ...]           │
│  Similarity: 0.34 ⭐⭐ (LOW - Climate content)                  │
│                                                                 │
│  Query:    [0.34, -0.23,  0.78,  0.45, -0.12, ...]           │
│             ↓      ↓      ↓      ↓      ↓                      │
│  Doc 3:    [0.45,  0.23, -0.89, -0.12,  0.67, ...]           │
│  Similarity: 0.15 ⭐ (VERY LOW - Cooking content)              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Phase 3: Ranking and Results

```
RANKING ALGORITHM
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  1. Collect all similarity scores                               │
│  2. Filter by minimum threshold (e.g., > 0.5)                  │
│  3. Sort in descending order                                    │
│  4. Take top K results (e.g., top 5)                          │
│  5. Add ranking metadata                                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                     FINAL RESULTS                              │
│                                                                 │
│  🏆 Rank #1 | Similarity: 0.89                                │
│  📖 Title: "Machine Learning Basics"                           │
│  📝 Content: "ML is a subset of AI that enables..."           │
│                                                                 │
│  🥈 Rank #2 | Similarity: 0.76                                │
│  📖 Title: "Neural Networks Guide"                             │
│  📝 Content: "Deep learning uses artificial networks..."       │
│                                                                 │
│  🥉 Rank #3 | Similarity: 0.65                                │
│  📖 Title: "Natural Language Processing"                       │
│  📝 Content: "NLP enables computers to understand..."          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Complete Algorithm Workflow

```
START
  │
  ▼
┌─────────────────┐
│  Load spaCy     │ ← Initialize NLP model
│  Model          │
└─────────────────┘
  │
  ▼
┌─────────────────┐
│  FOR EACH       │ ← Indexing Loop
│  Document:      │
│  ┌─────────────┐│
│  │ Text → Vec  ││ ← Convert to 300D vector
│  │ Store Vec   ││ ← Save to embeddings array
│  │ Store Meta  ││ ← Save document metadata
│  └─────────────┘│
└─────────────────┘
  │
  ▼
┌─────────────────┐
│  Wait for       │ ← Ready for queries
│  User Query     │
└─────────────────┘
  │
  ▼
┌─────────────────┐
│  Query → Vector │ ← Convert query to 300D vector
└─────────────────┘
  │
  ▼
┌─────────────────┐
│  FOR EACH       │ ← Search Loop  
│  Stored Vector: │
│  ┌─────────────┐│
│  │ Calculate   ││ ← Cosine similarity
│  │ Similarity  ││
│  │ Store Score ││ ← Keep similarity score
│  └─────────────┘│
└─────────────────┘
  │
  ▼
┌─────────────────┐
│  Sort by        │ ← Ranking
│  Similarity     │
│  (Desc)         │
└─────────────────┘
  │
  ▼
┌─────────────────┐
│  Return Top K   │ ← Results
│  Results        │
└─────────────────┘
  │
  ▼
END
```

---

## 🧠 Vector Space Visualization

```
3D VECTOR SPACE (Simplified from 300D)
                                    Z
                                    │
                                    │
                              📄ML  │
                                 ╱  │
                                ╱   │
                        Query⭐╱    │
                             ╱     │
                            ╱      │────────────── Y
                           ╱      ╱
                          ╱      ╱
                         ╱   📄Climate
                        ╱   ╱
                       ╱   ╱
                      ╱   ╱
                     ╱   ╱
                 📄Cooking
                   ╱
                  ╱
                 ╱
                X

Explanation:
- Each point represents a document's vector position
- Distance between points = semantic similarity  
- Query⭐ is closest to ML document = highest similarity
- Cooking document is farthest = lowest similarity
```

---

## ⚡ Algorithm Complexity

```
TIME COMPLEXITY ANALYSIS
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  📚 INDEXING PHASE:                                            │
│     • Per document: O(L) where L = text length                │
│     • Total: O(N × L) where N = number of documents           │
│                                                                 │
│  🔍 SEARCH PHASE:                                              │
│     • Query processing: O(Q) where Q = query length           │
│     • Similarity calculation: O(N × D) where D = 300          │
│     • Sorting: O(N log N)                                     │
│     • Total: O(Q + N×D + N log N) ≈ O(N)                     │
│                                                                 │
│  💾 SPACE COMPLEXITY:                                          │
│     • Document storage: O(N × L)                              │
│     • Vector storage: O(N × D) = O(N × 300)                  │
│     • Total: O(N × (L + D))                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🎯 Key Algorithm Features

```
┌─────────────────────────────────────────────────────────────────┐
│                    ALGORITHM STRENGTHS                          │
│                                                                 │
│  ✅ SEMANTIC UNDERSTANDING                                      │
│     • Captures meaning beyond keywords                         │
│     • Handles synonyms automatically                           │
│     • Understands context and relationships                    │
│                                                                 │
│  ✅ MATHEMATICAL PRECISION                                      │
│     • Cosine similarity provides accurate relevance scores     │
│     • Consistent and reproducible results                      │
│     • Quantifiable similarity measurements                     │
│                                                                 │
│  ✅ SCALABLE DESIGN                                            │
│     • Linear search complexity O(N)                           │
│     • Easy to add/remove documents                            │
│     • Memory-efficient vector storage                         │
│                                                                 │
│  ✅ REAL-TIME PERFORMANCE                                      │
│     • Fast query processing (~15ms for 10 docs)              │
│     • Pre-computed embeddings for speed                       │
│     • Efficient similarity calculations                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

This diagram shows how the algorithm transforms human language into mathematical vectors and uses geometry to find semantic similarity! 🎯🧠
