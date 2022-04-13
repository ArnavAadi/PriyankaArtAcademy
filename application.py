from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def home():
    return render_template("index.html",)

@application.route("/about-us")
def about_us():
    return render_template("about-us.html",)

@application.route("/gallery")
def gallery():
    return render_template("gallery.html",)


if __name__ == "__main__":
    application.run(debug=True)
