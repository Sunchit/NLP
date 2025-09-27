# Make sure you have installed -> pip install gensim scikit-learn numpy

import numpy as np
from gensim.models import Word2Vec
from sklearn.ensemble import RandomForestClassifier

# --- Part 1: Simulate Financial Text Data & Train Vectorizer ---

# We'll use both transaction narratives and loan purposes as our "language".
# Each list represents a series of financial events or documents.
financial_texts = [
    # Stable, low-risk user
    ['paycheck', 'direct_deposit', 'rent_payment', 'transfer_to_savings', 'grocery_store'],
    # Gig economy worker, but responsible
    ['uber_payment', 'lyft_payment', 'rent_payment', 'transfer_to_savings'],
    # User showing signs of distress
    ['paycheck', 'cash_advance', 'overdraft_fee', 'payday_loan', 'online_gambling'],
    # User making investments
    ['salary_deposit', 'investment_acct_transfer', 'mortgage_payment'],
    # Loan purposes
    ['loan_purpose_home_improvement'],
    ['loan_purpose_debt_consolidation']
]

print(">>> Training a Word2Vec model on financial texts...")
# This model learns the contextual meaning of financial terms.
financial_model = Word2Vec(sentences=financial_texts, vector_size=50, window=2, min_count=1)
print(">>> Model training complete.")

# --- Part 2: Function to Create a "Financial Fingerprint" ---

def get_financial_fingerprint(transaction_history, model):
    """
    Averages the vectors of a user's recent transactions to create a single behavior vector.
    """
    vectors = []
    for item in transaction_history:
        try:
            vectors.append(model.wv[item])
        except KeyError:
            # Ignore terms not in our model's vocabulary
            continue

    if not vectors:
        return np.zeros(model.vector_size) # Return a zero vector if no history

    # Average the vectors to get the "financial fingerprint"
    return np.mean(vectors, axis=0)

# --- Part 3: Train a Simple Credit Risk Classifier ---

print("\n>>> Simulating training data for the risk model...")

# Applicant 1: "Credit Invisible" but responsible (low risk)
history1 = ['paycheck', 'rent_payment', 'transfer_to_savings', 'grocery_store']
fingerprint1 = get_financial_fingerprint(history1, financial_model)
risk_label1 = 0 # Low Risk

# Applicant 2: Stable, good habits (low risk)
history2 = ['salary_deposit', 'investment_acct_transfer', 'mortgage_payment']
fingerprint2 = get_financial_fingerprint(history2, financial_model)
risk_label2 = 0 # Low Risk

# Applicant 3: Showing signs of financial distress (high risk)
history3 = ['paycheck', 'cash_advance', 'overdraft_fee', 'payday_loan']
fingerprint3 = get_financial_fingerprint(history3, financial_model)
risk_label3 = 1 # High Risk

# Prepare the training data
X_train = [fingerprint1, fingerprint2, fingerprint3]
y_train = [risk_label1, risk_label2, risk_label3]

# Create and train the classifier
risk_classifier = RandomForestClassifier(n_estimators=10, random_state=42)
risk_classifier.fit(X_train, y_train)

print(">>> Risk model trained.")

# --- Part 4: Assess a New Applicant ---

print("\n>>> Assessing a new applicant...")

# This applicant has no formal credit history, but their bank data is available.
new_applicant_history = ['paycheck', 'direct_deposit', 'rent_payment', 'transfer_to_savings']
print(f"Applicant's recent activity: {new_applicant_history}")

# Generate their financial fingerprint
new_fingerprint = get_financial_fingerprint(new_applicant_history, financial_model)

# Predict their risk level
predicted_risk = risk_classifier.predict([new_fingerprint])
prediction_proba = risk_classifier.predict_proba([new_fingerprint])


if predicted_risk[0] == 0:
    risk_assessment = "LOW RISK"
    confidence = prediction_proba[0][0]
else:
    risk_assessment = "HIGH RISK"
    confidence = prediction_proba[0][1]

print(f"\nModel Assessment: {risk_assessment} (Confidence: {confidence*100:.2f}%)")
print("This assessment can now be used alongside traditional data to make a final lending decision.")