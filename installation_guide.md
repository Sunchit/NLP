# Vector Embeddings Installation Guide

## Prerequisites and Setup Instructions

### 1. Python Installation

#### For macOS:
```bash
# Check if Python is already installed
python3 --version

# If not installed, install using Homebrew (recommended)
# First install Homebrew if you don't have it:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Then install Python
brew install python
```

#### For Windows:
```bash
# Download Python from https://www.python.org/downloads/
# Make sure to check "Add Python to PATH" during installation
# Verify installation:
python --version
```

#### For Linux (Ubuntu/Debian):
```bash
# Update package list
sudo apt update

# Install Python 3 and pip
sudo apt install python3 python3-pip

# Verify installation
python3 --version
pip3 --version
```

### 2. spaCy Installation

#### Install spaCy library:
```bash
# Using pip3 (recommended for most systems)
pip3 install spacy

# Alternative: using pip (if pip3 is not available)
pip install spacy
```

### 3. Download spaCy Language Models

#### Small English Model (12.8 MB):
```bash
# Good for basic NLP tasks, but no word vectors for similarity
python3 -m spacy download en_core_web_sm
```

#### Large English Model (400+ MB) - **Recommended for embeddings**:
```bash
# Includes pre-trained word vectors for better similarity calculations
python3 -m spacy download en_core_web_lg
```

#### Medium English Model (50 MB) - Alternative option:
```bash
# Balance between size and features
python3 -m spacy download en_core_web_md
```

### 4. Verify Installation

Create a test file `test_installation.py`:
```python
import spacy

# Test if spaCy is installed
print("spaCy version:", spacy.__version__)

# Test small model
try:
    nlp_sm = spacy.load("en_core_web_sm")
    print("✅ Small model (en_core_web_sm) loaded successfully")
except OSError:
    print("❌ Small model not found. Run: python3 -m spacy download en_core_web_sm")

# Test large model
try:
    nlp_lg = spacy.load("en_core_web_lg")
    print("✅ Large model (en_core_web_lg) loaded successfully")
    
    # Test word vectors
    doc = nlp_lg("test")
    if doc.vector.any():
        print("✅ Word vectors are available")
    else:
        print("⚠️ Word vectors not available")
        
except OSError:
    print("❌ Large model not found. Run: python3 -m spacy download en_core_web_lg")
```

Run the test:
```bash
python3 test_installation.py
```

### 5. Common Issues and Solutions

#### Issue: "pip not found" or "pip3 not found"
**Solution:**
```bash
# For macOS/Linux
python3 -m pip install spacy

# For Windows
python -m pip install spacy
```

#### Issue: "Permission denied" during installation
**Solution:**
```bash
# Install in user directory (recommended)
pip3 install --user spacy

# Or use sudo (not recommended)
sudo pip3 install spacy
```

#### Issue: "Command not found: python3"
**Solution:**
- On some systems, use `python` instead of `python3`
- Make sure Python is added to your system PATH

#### Issue: Large model download fails
**Solution:**
```bash
# Try downloading with specific version
python3 -m spacy download en_core_web_lg==3.8.0

# Or download manually and install
# Visit: https://github.com/explosion/spacy-models/releases
```

### 6. Additional Dependencies (Optional)

For advanced features, you might want to install:
```bash
# For visualization
pip3 install matplotlib plotly

# For data manipulation
pip3 install pandas numpy

# For machine learning
pip3 install scikit-learn

# For Jupyter notebooks
pip3 install jupyter
```

### 7. Model Comparison

| Model | Size | Features | Best For |
|-------|------|----------|----------|
| `en_core_web_sm` | 12.8 MB | Basic NLP, no word vectors | Fast processing, limited similarity |
| `en_core_web_md` | ~50 MB | Some word vectors | Balanced performance |
| `en_core_web_lg` | 400+ MB | Full word vectors | Best similarity calculations |

### 8. Next Steps

After successful installation:
1. Run the `spacy_embeddings_demo.py` script
2. Experiment with different sentences
3. Try building your own embedding applications
4. Explore other spaCy models for different languages

### 9. Troubleshooting Resources

- **spaCy Documentation**: https://spacy.io/usage
- **Model Downloads**: https://spacy.io/models
- **GitHub Issues**: https://github.com/explosion/spaCy/issues
- **Community Forum**: https://github.com/explosion/spaCy/discussions

---

*Last updated: September 2025*
*Compatible with spaCy v3.8+*
