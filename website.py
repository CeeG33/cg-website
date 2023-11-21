from flask import Flask, render_template, request, redirect

app = Flask(__name__)


navigation = {
    "home": {
        "href": "/",
        "caption": "Home"
    },
    
    "summary": {
        "href": "/summary",
        "caption": "Summary"
    },
    
    "projects": {
        "href": "/projects",
        "caption": "Projects"
    },
    
    "about_me": {
        "href": "/about_me",
        "caption": "About Me"
    },
}


@app.route("/")
def home():
    return render_template("home.html", navigation=navigation)


@app.route("/summary")
def summary():
    return render_template("summary.html", navigation=navigation)


@app.route("/projects")
def projects():
    return render_template("projects.html", navigation=navigation)


@app.route("/about_me")
def about_me():
    return render_template("about_me.html", navigation=navigation)