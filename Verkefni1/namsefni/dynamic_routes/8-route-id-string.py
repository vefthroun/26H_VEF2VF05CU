# Flytjum inn Flask-hluti sem þarf til að búa til vefapp, sýna síðu og skila 404-villu.
from flask import Flask, abort, render_template_string

# Búum til Flask-forritið.
app = Flask(__name__)

# vorur er [listi] með {söfnum}. Í hverju safni er vara sem hefur auðkenni, heiti og verð.
vorur = [
    {"id": 1, "nafn": "Epli", "verd": 150},
    {"id": 2, "nafn": "Brauð", "verd": 500},
    {"id": 3, "nafn": "Mjólk", "verd": 250},
]

# Forsíðuslóðin / birtir lista yfir vörur sem hægt er að velja.
@app.route('/')
def index():
    # Geymum titil síðunnar svo hægt sé að nota hann í HTML-sniðmátinu.
    title='Vöruval'

    # Búum til forsíðuna; hver tengill vísar á vörusíðu með auðkenni vörunnar.
    # title=title sendir titilinn inn í sniðmátið og return skilar síðunni til vafrans.

    return render_template_string(
        """
        <!doctype html>
        <html lang="is">
          <head><title>{{ title }}</title></head>
          <body>
            <h1>{{ title }}</h1>
            <ul>
                <li><a href=/vara/1>Epli</a></li>
                <li><a href=/vara/2>Brauð</a></li>
                <li><a href=/vara/3>Mjólk</a></li>
          </body>
        </html>
        """, 
        title=title
    )
# Athugið að '/vara/1' er strengur
# rásin tekur við auðkenni vöru og breytir í heiltölu

@app.route("/vara/<int:id>")
def vara(id):
    # Leitum að vöru með auðkenni sem passar við auðkennið úr slóðinni.
    valin_vara = next((item for item in vorur if item["id"] == id), None)

    # Ef engin vara finnst er skilað 404-villu, villuskilaboð eru útskýrð í errorHandlingStaturCode.py
    if valin_vara is None:
        abort(404) 
        
    # Setjum saman HTML-síðu og sendum valda vöru inn sem jinja sniðmátið.
    return render_template_string(
        """
        <!doctype html>
        <html lang="is">
          <head><title>{{ vara.nafn }}</title></head>
          <body>
            <h1>{{ vara.nafn }}</h1>
            <p>Verð: {{ vara.verd }} kr.</p>
            <p><a href="/">Til baka</a></p>
          </body>
        </html>
        """,
        vara=valin_vara
    )
# Ræsum vefþjóninn aðeins þegar skráin er keyrð beint.
if __name__ == "__main__":
    # Kveikjum á villuleitarham meðan forritið er í þróun.
    app.run(debug=True)
