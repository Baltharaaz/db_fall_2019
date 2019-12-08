from flask import Flask, render_template
from data import articles

app = Flask(__name__)
app.debug= True

articles = articles()

@app.route("/")
def homePage():
        return render_template('index.html')

@app.route("/about")
def aboutPage():
        return render_template("about.html")


@app.route("/articles")
def articlesPage():
        return render_template("articles.html", articles = articles)

if __name__ == "__main__":
    app.run()
