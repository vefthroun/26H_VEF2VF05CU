# Skipulag Flask-apps

```text
verkefni-4/                  # rót appsins á þjóninum
├── app.py
├── data/
│   └── db.json              # TinyDB býr til skrána ef hún er ekki til
└── content/
    ├── blog.py
    ├── api.py
    ├── templates/           # HTML-sniðmát, ef þeirra er þörf
    └── static/              # CSS, JavaScript og myndir, ef þeirra er þörf
```

`blog.py` og `api.py` skilgreina hvort sitt _Flask Blueprint_. `app.py`
skráir þau í appið og opnar TinyDB-gagnagrunninn fyrir `blog.py`.
`api.py` sækir gögn frá TVMaze og notar ekki gagnagrunninn. Með Python 3
þarf **ekki** `__init__.py` í `content` fyrir þetta skipulag.

### Hvað er Blueprint?

Blueprint er leið til að flokka slóðir og aðra virkni í aðskildar einingar.
Það er ekki sjálfstætt Flask-app: `app.py` tengir hvert Blueprint við appið
með `register_blueprint`. Þannig verður slóðin `/` í `blog.py` að
upphafssíðu appsins, en `/shows` í `api.py` verður `/api/shows` vegna
`url_prefix="/api"`. Slóðirnar `/api` og `/api/` vísa einnig á sömu
virkni. Báðar einingarnar geta notað stillingar appsins í
gegnum `current_app`.

### app.py

```python
from pathlib import Path

from flask import Flask
from tinydb import TinyDB

from content.blog import blog
from content.api import api

BASE_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    template_folder="content/templates",
    static_folder="content/static",
)

app.extensions["db"] = TinyDB(
    BASE_DIR / "data/db.json",
    indent=2,
    encoding="utf-8",
    ensure_ascii=False,
)

app.register_blueprint(blog)
app.register_blueprint(api, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
```

### content/blog.py

Einföld upphafssíða sem notar gagnagrunninn:

```python
from flask import Blueprint, current_app

blog = Blueprint("blog", __name__)


@blog.route("/")
def index():
    posts = current_app.extensions["db"].table("posts").all()
    return f"Fjöldi færslna: {len(posts)}"
```

### content/api.py

Einföld leið sem sækir lista af þáttum frá TVMaze og skilar honum á JSON-sniði:

```python
import requests
from flask import Blueprint, current_app, jsonify

api = Blueprint("api", __name__)

'''
/api
/api/
/api/shows
Þessar þrjár línur tengja sama fallið við þrjár slóðir. Þar sem Blueprint-ið er skráð með url_prefix="/api" 
Allar kalla þær á sama fallið, shows():
'''

@api.route("")
@api.route("/")
@api.route("/shows")
def shows():
    try:
        response = requests.get("https://api.tvmaze.com/shows", timeout=10)
        response.raise_for_status()
        shows_data = response.json()
    except (requests.RequestException, ValueError):
        current_app.logger.exception("Ekki tókst að sækja gögn frá TVMaze")
        return jsonify(error="Ekki tókst að sækja gögn frá TVMaze"), 502

    return jsonify(shows_data)
```

### Keyrsla

Setjið Flask, TinyDB og Requests upp í sýndarumhverfi, til dæmis með
`python -m pip install flask tinydb requests`. Keyrið síðan `python app.py`
úr verkefnismöppunni. Upphafssíðan er á `/` og TVMaze-gögnin á `/api`,
`/api/` og `/api/shows`.
Gagnagrunnurinn byrjar tómur; bæta þarf færslum í `posts`-töfluna áður en
þær birtast. `data`-mappan þarf að vera til og ferlið þarf skrifheimild í hana.

`debug=True` er aðeins ætlað til þróunar, ekki á opinberum þjónustuþjóni.
TinyDB hentar ekki þegar margar vinnslur þurfa að skrifa samtímis í sömu skrá.
