import os
from github.get_total_stars import get_total_stars
from modules import tfidf_similarity, pdf_extractor
from utils import extract_socials, normalize_modifier

# Constant Weights
GITHUB_STARS_WEIGHT: float = 0.2


def score(
        resumes: list[str],
        applicants: list[str],
        preferences: str,
        top_k: int | None = None
    ) -> list[tuple[str, float]]:

    """
    Returns Top-K Applicants best fit for the job.
    """

    # Read Resumes
    documents: list[str] = [pdf_extractor.extract(resumes) for resumes in resumes]

    # Compute TF-IDF Scores
    tfidf_scores: list[float] = tfidf_similarity.compute(
        documents=documents,
        preferences=preferences
    )

    # Normalize Similarity Scores
    total_score: float = sum(tfidf_scores)
    scores: list[float] = [score / total_score for score in tfidf_scores]

    # Scrape GitHub Data
    github_stars: list[int] = [
        get_total_stars(extract_socials.github_username(
            resume=resume
        )) for resume in resumes
    ]

    # Normalize GitHub Stars
    total_stars: int = sum(github_stars)
    if total_stars != 0:  # Avoid Division by Zero
        github_stars: list[float] = [star / total_stars for star in github_stars]

    # Add GitHub Weights to Scores
    scores: list[float] = [(
        normalize_modifier.modify(score, github_stars[i], GITHUB_STARS_WEIGHT)
    ) for i, score in enumerate(scores)]

    # Zip and Sort Results
    zipped_results: list[tuple[str, float]] = list(zip(applicants, scores))
    zipped_results.sort(key=lambda x: x[1], reverse=True)

    # Return Top-K/All Results
    return [
        (applicant, (score * 100)) for (applicant, score) in (
            zipped_results[:top_k] if top_k is not None else zipped_results
        )
    ]



if __name__ == "__main__":
    RESUME_DIR: str = "./resumes"
    PREFERENCES_FILE: str = "./preferences"

    # Read Resumes, Applicants and Preferences
    resumes: list[str] = [f"{RESUME_DIR}/{file}" for file in os.listdir(RESUME_DIR)]
    applicants: list[str] = [item.replace(RESUME_DIR + "/", "").replace(".pdf", "") for item in resumes]
    with open(PREFERENCES_FILE, "r", encoding="utf-8") as file: preferences: str = file.read().strip()

    # Calculate Scores
    scores = score(
        resumes=resumes,
        applicants=applicants,
        preferences=preferences,
        top_k=3  # Top-K Applicants
    )

    # Print Scores
    [print(f"{applicant}: {round(score)}%") for applicant, score in scores]
