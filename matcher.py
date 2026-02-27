from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from faq_data import faqs
from preprocessor import preprocess

# -------------------------------------------------------
# Step 1: Extract and preprocess all FAQ questions
# -------------------------------------------------------

# Pull out raw questions from the FAQ list
faq_questions = [faq["question"] for faq in faqs]

# Preprocess every FAQ question (clean, stem, remove stopwords)
preprocessed_faq_questions = [preprocess(q) for q in faq_questions]

# -------------------------------------------------------
# Step 2: Build the TF-IDF matrix from FAQ questions
# -------------------------------------------------------

# TfidfVectorizer converts text into numerical vectors
vectorizer = TfidfVectorizer()

# Fit the vectorizer on our FAQ questions and transform them into vectors
# This creates a matrix where each row = one FAQ question as numbers
faq_matrix = vectorizer.fit_transform(preprocessed_faq_questions)


# -------------------------------------------------------
# Step 3: The matching function
# -------------------------------------------------------

def get_best_answer(user_input, threshold=0.2):
    """
    Takes the user's raw input question and returns the best matching answer.

    Parameters:
        user_input (str)  : The raw question typed by the user
        threshold  (float): Minimum similarity score to accept a match (0 to 1)

    Returns:
        str: The best matching answer, or a fallback message if no match found
    """

    # Preprocess the user's input the same way we did for FAQ questions
    cleaned_input = preprocess(user_input)

    # Transform the user input into a TF-IDF vector using the SAME vectorizer
    # (important — must use the same vectorizer that was fit on FAQ questions)
    input_vector = vectorizer.transform([cleaned_input])

    # Calculate cosine similarity between user input and ALL FAQ questions
    similarity_scores = cosine_similarity(input_vector, faq_matrix)

    # similarity_scores is a 2D array, flatten it to a simple list
    scores = similarity_scores.flatten()

    # Find the index of the highest similarity score
    best_index = scores.argmax()
    best_score = scores[best_index]

    # If the best score is below our threshold, we couldn't find a good match
    if best_score < threshold:
        return "I'm sorry, I don't have an answer for that. Try asking something related to Artificial Intelligence!"

    # Otherwise return the answer that corresponds to the best matching question
    return faqs[best_index]["answer"]


# -------------------------------------------------------
# Quick test (only runs when you execute this file directly)
# -------------------------------------------------------
if __name__ == "__main__":
    test_questions = [
        "What is AI?",
        "How does deep learning work?",
        "Tell me about chatbots",
        "What is pizza?",          # should trigger fallback
        "Which languages are used in AI?",
    ]

    print("=" * 55)
    print("Matcher Test")
    print("=" * 55)
    for q in test_questions:
        answer = get_best_answer(q)
        print(f"Q: {q}")
        print(f"A: {answer}")
        print()