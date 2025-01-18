from flask import Flask, render_template, request

# Constants
DEBUG: bool = True

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

    print([file.save(f"./uploads/{file.filename}") for file in request.files.getlist("file")])

    return render_template("result.html")


# Run Server
app.run(
    host="0.0.0.0",
    port=80,
    debug=DEBUG
)
