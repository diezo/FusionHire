from flask import Flask, render_template, request
import uuid
import shutil
import os
import json
from screener.screener import screen

# Constants
DEBUG: bool = True
UPLOAD_DIR: bool = "./uploads"
DEFAULT_APPLICANTS_TOP_K: int = 3

# Remove Uploads
print("Removing uploads...")
for each in os.listdir(UPLOAD_DIR):
    try: os.remove(f"{UPLOAD_DIR}/{each}") if os.path.isfile(each) else shutil.rmtree(f"{UPLOAD_DIR}/{each}")
    except: print(f"Failed to remove: {UPLOAD_DIR}/{each}")

print()

# Initialize Flask App
app: Flask = Flask(__name__, template_folder="templates")


@app.get("/")
def home() -> None:
    """
    Serves the home page.
    """

    return render_template("home.html")


@app.post("/screen")
def screen_route() -> None:
    """
    Screens resumes and returns the results.
    """

    # Get Form Data
    preferences: str = request.form.get("preferences").strip()
    top_k: int = 0

    try: top_k: int = int(request.form.get("top_k", "").strip())
    except ValueError: pass

    # Create Unique Uploads Sub-Dir
    uploads_subdir: str = str(uuid.uuid4())  # Generate UUID
    os.mkdir(f"{UPLOAD_DIR}/{uploads_subdir}")  # Create Directory

    resumes: list[str] = []
    applicants: list[str] = []

    # Save Each File in Uploads Sub-Directory
    for file in request.files.getlist("file"):
        resume: str = f"{UPLOAD_DIR}/{uploads_subdir}/{file.filename}"  # Path Includes 'Uploads Sub-Directory'

        resumes.append(resume)  # Record Resume Path
        applicants.append(file.filename.rsplit(".", maxsplit=1)[0])  # Record Applicant

        file.save(resume)

    # Compute Results
    results: list[tuple[str, float]] = screen(
        resumes=resumes,
        applicants=applicants,
        preferences=preferences,
        top_k=top_k if top_k > 0 else DEFAULT_APPLICANTS_TOP_K  # Top-K: User-Defined or Default
    )

    # Round-off Scores
    results: list[tuple[str, float]] = [(applicant, round(score, 2)) for applicant, score in results]

    # Delete Uploads Sub-Directory
    shutil.rmtree(f"{UPLOAD_DIR}/{uploads_subdir}")

    # Render Results Template
    return render_template("result.html", results=json.dumps(results))


# Run Server
app.run(
    host="0.0.0.0",
    port=80,
    debug=DEBUG
)
