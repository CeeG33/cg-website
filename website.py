from flask import Flask, render_template

app = Flask(__name__)


navigation = {
    "home": {"href": "/", "caption": "Home", "icon": "#home"},
    "summary": {"href": "/summary", "caption": "Summary", "icon": "#summary"},
    "projects": {"href": "/projects", "caption": "Projects", "icon": "#projects"},
    "about_me": {"href": "/about_me", "caption": "About Me", "icon": "#about_me"},
}


@app.route("/")
def home():
    """Renders the home page using the home.html file."""
    return render_template("home.html", navigation=navigation)


@app.route("/summary")
def summary():
    """Renders the summary page using the summary.html file."""
    return render_template("summary.html", navigation=navigation)


@app.route("/projects")
def projects():
    """Renders the projects page using the projects.html file."""
    return render_template("projects.html", navigation=navigation)


@app.route("/about_me")
def about_me():
    """Renders the about me page using the about_me.html file."""
    return render_template("about_me.html", navigation=navigation)


if __name__ == "__main__":
    app.run()