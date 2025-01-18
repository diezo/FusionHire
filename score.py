import os
from github.get_total_stars import get_total_stars
from modules import tfidf_similarity, pdf_extractor
from utils import extract_socials, normalize_modifier

# Weights
GITHUB_STARS_WEIGHT: float = 0.2

# Constants
RESUME_DIR: str = "./resumes"
PREFERENCES_FILE: str = "./preferences"

# Get List of Resumes
resumes: list[str] = [f"{RESUME_DIR}/{file}" for file in os.listdir(RESUME_DIR)]

# Get List of Applicants
applicants: list[str] = [item.replace(RESUME_DIR + "/", "").replace(".pdf", "") for item in resumes]

# Read Preferences
with open(PREFERENCES_FILE, "r", encoding="utf-8") as file:
    preferences: str = file.read().strip()

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

# TODO: Print Scores
[print(f"{applicant}: {round(percentage * 100)}%") for applicant, percentage in zip(applicants, scores)]
