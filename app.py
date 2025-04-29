from flask import Flask, render_template, request, jsonify

from basics import finder

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form.get("name")
    summary, profile_pic_url = finder(name=name)
    return jsonify(
        {"summary_and_facts": summary.to_dict(), "photoURL": profile_pic_url}
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
