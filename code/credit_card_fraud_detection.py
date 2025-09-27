# ==============================================================================
# NLP Vector Algorithm for Credit Card Fraud Detection
# ==============================================================================
# This script provides a conceptual, end-to-end example of using NLP
# vector techniques (Word2Vec) to detect credit card fraud.
#
# Required Libraries:
# pip install gensim scikit-learn numpy
# ==============================================================================

import numpy as np
from gensim.models import Word2Vec
from sklearn.ensemble import RandomForestClassifier

def train_merchant_vectorizer(transaction_sequences, vector_size=50, window=3, min_count=1):
    """
    Trains a Word2Vec model on sequences of merchant transactions.

    Args:
        transaction_sequences (list of list of str): The transaction data.
        vector_size (int): The dimensionality of the merchant vectors.
        window (int): The context window for the Word2Vec model.
        min_count (int): Minimum frequency for a merchant to be included.

    Returns:
        gensim.models.Word2Vec: The trained model.
    """
    print(">>> Step 1: Training a Word2Vec model on transaction sequences...")
    model = Word2Vec(
        sentences=transaction_sequences,
        vector_size=vector_size,
        window=window,
        min_count=min_count,
        workers=4
    )
    print(">>> Word2Vec model training complete.")
    return model

def create_feature_vector(history, new_transaction, amount, model):
    """
    Creates a single feature vector from a user's history and a new transaction.

    Args:
        history (list of str): The user's recent transaction merchants.
        new_transaction (str): The merchant for the new transaction.
        amount (float): The amount of the new transaction.
        model (gensim.models.Word2Vec): The trained merchant vectorizer.

    Returns:
        numpy.ndarray: A concatenated feature vector for the classifier.
    """
    vector_size = model.vector_size

    # Get the vector for the new transaction merchant
    try:
        new_transaction_vec = model.wv[new_transaction]
    except KeyError:
        new_transaction_vec = np.zeros(vector_size) # Use a zero vector if unknown

    # Create the user's average historical behavior vector ("behavioral fingerprint")
    history_vectors = [model.wv[merchant] for merchant in history if merchant in model.wv]

    if not history_vectors:
        behavior_vec = np.zeros(vector_size)
    else:
        behavior_vec = np.mean(history_vectors, axis=0)

    # Combine features: behavior vector, new transaction vector, and normalized amount
    # Normalizing the amount is important for model performance.
    normalized_amount = np.log1p(amount) / 10.0 # Simple log normalization

    return np.concatenate([behavior_vec, new_transaction_vec, [normalized_amount]])

def train_fraud_classifier(X_train, y_train):
    """
    Trains a RandomForestClassifier on the feature vectors.

    Args:
        X_train (list of numpy.ndarray): The training feature vectors.
        y_train (list of int): The training labels (0 = Not Fraud, 1 = Fraud).

    Returns:
        sklearn.ensemble.RandomForestClassifier: The trained fraud classifier.
    """
    print("\n>>> Step 3: Training the Fraud Classifier...")
    classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    classifier.fit(X_train, y_train)
    print(">>> Fraud classifier training complete.")
    return classifier

# ==============================================================================
# Main Execution Block
# ==============================================================================
if __name__ == "__main__":

    # --- Data Simulation ---
    # In a real-world scenario, this would be millions of real transaction histories.
    transaction_data = [
        ['starbucks', 'petrol', 'grocery_store', 'amazon', 'starbucks'],
        ['walmart', 'amazon', 'home_depot', 'petrol'],
        ['movie_theater', 'restaurant', 'uber', 'starbucks'],
        ['grocery_store', 'amazon', 'pharmacy', 'walmart', 'petrol'],
        ['gucci', 'louis_vuitton', 'prada', 'luxury_restaurant'], # Luxury shopper
        ['amazon', 'petrol', 'starbucks', 'walmart']
    ]

    # 1. Train the merchant vectorizer
    merchant_model = train_merchant_vectorizer(transaction_data)

    # 2. Simulate training data for the fraud classifier
    print("\n>>> Step 2: Creating feature vectors for the fraud classifier...")

    # Example 1: Normal transaction for a standard user (Not Fraud)
    history1 = ['starbucks', 'petrol', 'grocery_store', 'amazon']
    features1 = create_feature_vector(history1, 'walmart', 75.0, merchant_model)
    label1 = 0

    # Example 2: Normal transaction for a luxury user (Not Fraud)
    history2 = ['gucci', 'louis_vuitton', 'prada']
    features2 = create_feature_vector(history2, 'luxury_restaurant', 450.0, merchant_model)
    label2 = 0

    # Example 3: FRAUDULENT transaction for a standard user (Fraud)
    # The purchase is completely out of character and has a high amount.
    history3 = ['starbucks', 'petrol', 'grocery_store', 'amazon']
    features3 = create_feature_vector(history3, 'gucci', 2500.0, merchant_model)
    label3 = 1

    # Assemble the training dataset
    X_train_data = [features1, features2, features3]
    y_train_data = [label1, label2, label3]

    # 3. Train the fraud classifier
    fraud_model = train_fraud_classifier(X_train_data, y_train_data)

    # --- Step 4: Test the model on a new, suspicious transaction ---
    print("\n" + "="*40)
    print(">>> Step 4: Testing the Fraud Classifier")
    print("="*40)

    # A standard user suddenly makes a very out-of-character purchase.
    test_user_history = ['starbucks', 'petrol', 'grocery_store', 'amazon']
    test_suspicious_transaction = 'louis_vuitton'
    test_suspicious_amount = 32000.0

    print(f"\nUser History: {test_user_history}")
    print(f"New Transaction: '{test_suspicious_transaction}' for Rupees {test_suspicious_amount}")

    # Create the feature vector for this new event
    test_features = create_feature_vector(
        test_user_history,
        test_suspicious_transaction,
        test_suspicious_amount,
        merchant_model
    )

    # Predict the outcome
    prediction = fraud_model.predict([test_features])
    prediction_proba = fraud_model.predict_proba([test_features])

    print("\n--- Prediction Result ---")
    if prediction[0] == 1:
        fraud_confidence = prediction_proba[0][1] * 100
        print(f"🚨 Prediction: FRAUD DETECTED (Confidence: {fraud_confidence:.2f}%)")
    else:
        not_fraud_confidence = prediction_proba[0][0] * 100
        print(f"✅ Prediction: Transaction is likely NOT FRAUD (Confidence: {not_fraud_confidence:.2f}%)")
    print("="*25)