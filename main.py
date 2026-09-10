from flask import Flask, render_template, send_from_directory
import os

app = Flask(
    __name__,
    template_folder="pages",
    static_folder="css",
    static_url_path="/css"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculadora")
def calculadora():
    return render_template("calculadora.html")


@app.route("/result")
def result():
    return render_template("result.html")


@app.route("/favicon.png")
def favicon():
    caminho = os.path.dirname(os.path.abspath(__file__))

    return send_from_directory(
        caminho,
        "favicon.png",
        mimetype="image/png"
    )


@app.route("/js/<path:filename>")
def javascript(filename):
    caminho = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "js"
    )

    return send_from_directory(caminho, filename)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )