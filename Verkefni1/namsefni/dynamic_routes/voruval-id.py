from flask import Flask, abort, render_template_string
from pprint import pprint

app = Flask(__name__)

vorur = [
    {"id": 1, "nafn": "Epli", "verd": 150},
    {"id": 2, "nafn": "Brauð", "verd": 500},
    {"id": 3, "nafn": "Mjólk", "verd": 250},
]

@app.route("/vara/<int:id>")
def vara(id):
    # finnum vöruna eftir id 
    voruval = next((item for item in vorur if item["id"] == id), None)
    if voruval is None:
        abort(404)
    return render_template_string(
        """
        <!doctype html>
        <html lang="is">
          <head><title>{{ vara.nafn }}</title></head>
          <body>
            <h1>{{ vara.nafn }}</h1>
            <p>Verð: {{ vara.verd }} kr.</p>
          </body>
        </html>
        """, vara=voruval 
    )
if __name__ == "__main__":
    app.run(debug=True)
