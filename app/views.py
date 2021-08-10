from app import app
from pytube import YouTube
from flask import render_template, request, session, redirect, url_for, flash

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["url"] = request.form["url"]
        try:
            yt = YouTube(session["url"])
            return render_template("video.html", url=session["url"], yt=yt)
        except Exception:
            flash("Failed to load YouTube video or invalid URL", "danger")
            return redirect(url_for("index"))
    return render_template("index.html")

@app.route('/download', methods=["GET", "POST"])
def download():
    if request.method == "POST":
        yt = YouTube(session["url"])
        itag = request.form["itag"]
        yt.streams.get_by_itag(itag).download("download")
    flash("Your YouTube video has been successfully downloaded", "success")
    return redirect(url_for("index"))