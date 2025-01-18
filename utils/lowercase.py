def lowercase(documents: list[str]) -> list[str]:
    """
    Lowercases and strips all the documents.
    """

    for i, document in enumerate(documents): documents[i] = document.lower().strip()
    return documents
