import spacy
from spacy.language import Language

nlp: Language = spacy.load("en_core_web_sm")


def lemmatize(documents: list[str]) -> list[str]:
    """
    Lemmatizes every token of the documents.
    """

    for i, document in enumerate(documents):
        documents[i] = " ".join([
            token.lemma_ for token in nlp(document)
            
            if not token.is_stop and not
            token.is_punct and not
            token.is_digit
        ])

    return documents
