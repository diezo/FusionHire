import os
from screener.screener import screen

default_prefs: str = "Python Django Flask FastAPI SQL NoSQL PostgreSQL MySQL MongoDB Data Structures and Algorithms REST APIs GraphQL Git Docker AWS Azure Google Cloud Jupyter Notebooks Machine Learning Deep Learning Pandas NumPy TensorFlow Keras PyTorch Data Science Web Scraping BeautifulSoup Selenium Unit Testing PyTest CI/CD TDD Agile Scrum Version Control Linux Bash Scripting Virtual Environments Flask APIs Socket Programming Queueing Systems Cloud Deployment APIs Integration Software Design Patterns Security Best Practices Data Visualization Plotly Matplotlib Seaborn OAuth JWT"
preferences: str = input("Preferences [Default]: ").strip()

if preferences == "":
    print("Using default preferences")
    preferences = default_prefs

print()

selected: list[tuple[str, float]] = screen(
    resumes=[f"./inputs/{each}" for each in os.listdir("inputs")],
    applicants=[f"{each.replace('.pdf', '')}" for each in os.listdir("inputs")],
    preferences=preferences,
    top_k=3
)

for candidate, score in selected:
    print(f"{candidate}: {score}")
