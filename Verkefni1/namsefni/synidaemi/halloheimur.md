### Uppsetning á Flask með VENV 
[Flask tutorial in VS Code](https://code.visualstudio.com/docs/python/tutorial-flask).

### Halló heimur 
 
```python
# import Flask class in Python
from flask import Flask

# Create app, that hosts the application. Don't worry about that __name__ object, it's just a convention.
app = Flask(__name__)

# route() maps what you type in the browser (the url) to a Python function.
# @app.route() (@ er decorator í python) bindur fallið index() við URL. 
# Whenever a browser requests a URL, the associated function is called and the return value is sent back to the browser
@app.route('/')
def index():
    # fallið skilar hér streng sem er sendur til biðlara (e. client) í vafra.
    return "<h1>Hello, World!</h1>"  # Við getum blandað html og texta.

# This starts the web app 
if __name__ == '__main__':
    # run, starts a built-in development server
    app.run(debug=True, use_reloader=True)   
            # debug=True. debug er nytsamlegt í vefþróun, gefur skýrari villuskilaboð.
            # use_reloader. use_reloader=True þýðir að þú þarft ekki að endurkeyra python skrá stöðugt þegar þú gerir kóðabreytingar. 
     
# Keyrðu python skránna í terminal og skoðaðu url í vafra (localhost), en með Flask kemur web server sem vð getum notað
```

## Skýring

```python
from flask import Flask, render_template

app = Flask(__name__)
```

Þessi kóði er grunnurinn að því að setja upp vefforrit í Flask. Hér er stutt útskýring á því hvað hver lína gerir:

*   **`from flask import Flask, render_template`**: Hér er verið að flytja inn (e. import) nauðsynlega íhluti úr Flask safninu. 
    *   **`Flask`** er klasinn sem er notaður til að búa til sjálft vefforritið.
    *   **`render_template`** er fall sem er notað til að sýna (e. render) HTML-skrár fyrir notandann í vafranum.
*   **`app = Flask(__name__)`**: Þessi lína býr til nýtt tilvik (e. instance) af Flask klasanum. 
    *   Breytan **`__name__`** er notuð svo Flask viti hvar það á að leita að auðlindum, eins og HTML-sniðmátum í `templates` möppunni og kyrrstæðum skrám (e. static files) eins og CSS í `static` möppunni.

Þetta er fyrsta skrefið í að búa til lágmarksvefforrit þar sem breytan `app` verður miðpunktur forritsins þíns.

---

```python
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True) 
```

Þessi kóðabútur er notaður til að ræsa Flask-vefþjóninn beint úr Python-skránni þinni. Hér er stutt útskýring á því hvað hver hluti gerir:

*   **`if __name__ == '__main__':`**: Þetta er hefðbundin Python-leið til að tryggja að kóðinn keyri aðeins ef skráin er ræst beint (t.d. með skipuninni `python skráarnafn.py`). Ef skráin væri flutt inn (e. import) í aðra skrá sem eining, myndi vefþjóninn ekki ræsast sjálfkrafa.
*   **`app.run(...)`**: Þetta ræsir innbyggðan þróunarvefþjón Flask, sem er hannaður til að prófa forritið á meðan á smíði stendur.
*   **`debug=True`**: Þetta virkjar **villuleitarham** (e. debug mode). Það hefur tvo mikilvæga kosti í för með sér:
    1.  Vefþjónninn fylgist með breytingum á kóðanum þínum og **endurræsir sig sjálfkrafa** þegar þú vistar skrána.
    2.  Ef villa kemur upp í kóðanum birtist gagnvirkur villuleitari beint í vafranum sem hjálpar þér að greina vandamálið.
*   **`use_reloader=True`**: Þessi skipun stýrir því sérstaklega að vefþjóninn endurræsi sig þegar kóða er breytt. Þótt `debug=True` virki þetta yfirleitt sjálfkrafa, þá er þetta tiltekið hér til að tryggja að sú virkni sé virk.

**Mikilvæg athugasemd:** Samkvæmt heimildum ætti aldrei að nota villuleitarhaminn (`debug=True`) í raunverulegu vinnsluumhverfi (e. production) þar sem hann getur skapað öryggishættu með því að leyfa keyrslu á kóða beint úr vafra.

## verkefni 2


#### Nánari skýringar

- [Quick Start](https://flask.palletsprojects.com/en/2.3.x/quickstart/)
- Decorators[`@app.route('/')`](decorators.md) 
- Flask API documentation [`Flask(__name__)`](https://flask.palletsprojects.com/en/2.2.x/api/#flask.Flask)
- Python documentation [`__main__`](https://docs.python.org/3/library/__main__.html)
- Stack Overflow [`if __name__ == '__main__':`](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)


---

Ef þú færð eftirfarandi skilaboð í Windows:

```
C:\vef31> venv\scripts\activate
venv\scripts\activate : File C:\vef31\venv\scripts\Activate.ps1 cannot be loaded because running scripts is disabled
on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170. 
```
**Lausn:** Í powershell (run as admin)
`set-executionpolicy remotesigned`

---

<!--
#### Ef við viljum sleppa `app.run` í kóðanum

- Stillum umhverfisbreytu í terminal: `$env:FLASK_APP = "app.py"`
- Keyrum app í terminal: `flask run` 

-->
