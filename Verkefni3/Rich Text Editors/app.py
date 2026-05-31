from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/quill", methods=["GET", "POST"])
def quill():
    content = ""
    if request.method == "POST":
        content = request.form.get("quill_html")
    return render_template("quill.html", content=content)

if __name__ == "__main__":
    app.run(debug=True)