from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.lowercase import lowercase
from utils.lemmatize import lemmatize
from utils.remove_constants import remove_constants
from scipy.sparse import spmatrix


def compute(documents: list[str], preferences: str) -> list[float]:
    """
    Computes similarity between documents and preferences.
    """

    # Ensure Preferences is a List
    preferences: list[str] = [preferences]

    # Preprocess Documents
    documents: list[str] = lowercase(documents)
    documents: list[str] = lemmatize(documents)  # Remove Stop Words, Digits, Punctuations
    documents: list[str] = remove_constants(documents)  # Remove Constants, Strip Whitespaces

    # Preprocess Preferences
    preferences: list[str] = lowercase(preferences)
    preferences: list[str] = lemmatize(preferences)  # Remove Stop Words, Digits, Punctuations
    preferences: list[str] = remove_constants(preferences)  # Remove Constants, Strip Whitespaces

    # Initialize TF-IDF Vectorizer
    tfidf_vectorizer: TfidfVectorizer = TfidfVectorizer(stop_words="english")

    # Learn Vocabulary & Transform Documents
    documents_matrix: spmatrix = tfidf_vectorizer.fit_transform(documents)
    preferences_matrix: spmatrix = tfidf_vectorizer.transform(preferences)

    # Compute Cosine Similarity
    similarity: list[float] = cosine_similarity(documents_matrix, preferences_matrix).tolist()

    # Return First Element of Each Similarity Score (Because Size of Preferences Array is 1)
    return [score[0] for score in similarity]
