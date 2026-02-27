import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download required NLTK data (only runs once)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)

# Initialize the stemmer and stopwords list
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))


def preprocess(text):
    """
    Takes a raw string and returns a cleaned, stemmed version.
    
    Steps:
    1. Lowercase the text
    2. Remove punctuation
    3. Tokenize into individual words
    4. Remove stopwords
    5. Stem each word to its root form
    """

    # Step 1: Lowercase
    text = text.lower()

    # Step 2: Remove punctuation (e.g. "?" "!" "," etc.)
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Step 3: Tokenize — split text into a list of words
    tokens = nltk.word_tokenize(text)

    # Step 4: Remove stopwords — filter out common filler words
    tokens = [word for word in tokens if word not in stop_words]

    # Step 5: Stem — reduce each word to its base/root form
    tokens = [stemmer.stem(word) for word in tokens]

    # Join tokens back into a single cleaned string
    return ' '.join(tokens)


# ----------------------------
# Quick test (only runs when you execute this file directly)
# ----------------------------
if __name__ == "__main__":
    test_sentences = [
        "What is Artificial Intelligence??",
        "what's AI?",
        "Tell me about artificial intelligence!",
        "How does machine learning work?",
    ]

    print("=" * 50)
    print("Preprocessor Test")
    print("=" * 50)
    for sentence in test_sentences:
        cleaned = preprocess(sentence)
        print(f"  Original : {sentence}")
        print(f"  Cleaned  : {cleaned}")
        print()