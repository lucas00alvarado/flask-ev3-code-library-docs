from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/<page>")
def home(page):
    # q = request.args.get("q")
    return render_template(page)


if __name__ == "__main__":
    app.run(debug=True)