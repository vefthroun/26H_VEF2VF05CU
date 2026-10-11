**Flask** er léttur Python veframmi (*web framework*) sem er byggður á litlum kjarna og hannaður til að vera skýr (*explicit*) og sveigjanlegur.

### 1\. Hvernig Flask virkar í Python

* **WSGI Forrit:** Þegar forrit er stofnað með `app = Flask(__name__)` býr Flask til WSGI vefforrit sem tekur á móti HTTP beiðnum frá vafranum og skilar svörum til baka.
* **Rásun (** **Routing** **):** Flask notar skreytinguna `@app.route('/...')` til að tengja tilteknar vefslóðir (*URL*) við Python birtingarföll (*view functions*). Þegar notandi opnar slóðina keyrir Flask viðkomandi fall og skilar niðurstöðunni (venjulega HTML eða JSON) til vafrans[2][4].
* **Beiðnir og svör:** Flask heldur utan um innkomandi gögn í gegnum `request` hlutinn (t.d. formgögn úr `request.form` eða færibreytur úr `request.args`).

---

### 2\. Samspilið við Werkzeug, Jinja og aðrar viðbætur

Flask byggir í grunninn á tveimur megin stoðum sem sjá um sitt hvoran hlutann:

* **Werkzeug (HTTP &amp; WSGI grunnurinn):**
  * Werkzeug sér um allt neðra lagið: samskipti við vefþjóninn, rásun slóða (*URL routing*), meðhöndlun á HTTP beiðnum/svörum, kökum, session-kökum og skráarupphali.
* **Jinja (Sniðmátsvél /** **Template Engine** **):**
  * Í stað þess að skrifa hráan HTML-texta inni í Python-kóðanum notar Flask **Jinja** til að birta dinamískar HTML síður.
  * Flask leitar sjálfgefið að `.html` skrám í **templates/** möppunni.
  * Jinja býður upp á örugga dulkóðun á HTML (*auto-escaping*) til að koma í veg fyrir öryggisgalla, sniðmátsarf (*template inheritance* með `{% extends %}`) og breytilega birtingu á Python gögnum.

---

### 3\. Dæmigert verkefnisskipulag

Í dæmigerðu Flask verkefni er verkaskiptingunni skipt þannig upp:

```
verkefni/
├── app.py           # Python bakendinn: routes, rökfræði og request-vinnsla
├── static/          # Kyrrstæðar skrár: CSS stílsíður, myndir, JavaScript
└── templates/       # HTML sniðmát sem Jinja þýðir (t.d. index.html, layout.html)

```

Flask er vísindalega kallað „ör-vinnurammi“ (*microframework*) vegna þess að það þvingar forritara ekki til að nota tiltekna gagnagrunna eða möppuskipulag. Ef þörf er á viðbótarvirkni (eins og gagnagrunnstengingu, auðkenningu eða formstaðfestingum) er auðvelt að bæta við viðeigandi Python pökkum eða Flask-viðbótum (*extensions*).

Hér er lítið dæmi sem sýnir hvernig **[suspicious link removed]** notar `render_template()` til að senda gögn (strengi, lista og orðasöfn) yfir í Jinja2 sniðmát í **templates/** möppunni[1].

---

### 1\. Bakendakóðinn: `app.py`

Flask leitar sjálfgefið að HTML sniðmátum í `templates/` möppunni sem er staðsett við hliðina á Python skránni. Gögnin eru send sem lykilorðafæribreytur (*keyword arguments*) inn í `render_template()`:

```Python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # 1. Búum til nokkrar mismunandi gerðir af Python gögnum
    notandanafn = "Jón"
    áfangar = ["FORR2FA", "VEFÞ2VF", "VESM2VT"]
    notendaupplysingar = {"skoli": "Tækniskólinn", "onn": "Haust 2026"}
    
    # 2. Sendum gögnin yfir í templates/index.html
    # Vinstra megin við '=' er heitið sem Jinja notar, hægra megin er Python breytan
    return render_template(
        'index.html', 
        user=notandanafn, 
        courses=áfangar, 
        info=notendaupplysingar
    )

if __name__ == '__main__':
    app(debug=True)

```

---

### 2\. Framendakóðinn: `templates/index.html`

Í HTML skránni eru Python breyturnar birtar með slaufusvigum `{{ ... }}` og Jinja lykkjum `{% for ... %}`[2]:

```HTML

    {# 1. Birting á streng (user) #}
    <h1>Velkomin(n), {{ user }}!</h1>

    {# 2. Birting á gildum úr orðasafni (info) með punktatáknun eða lyklum #}
    <p><strong>Skóli:</strong> {{ info.skoli }} ({{ info['onn'] }})</p>

    {# 3. Ítrun í gegnum lista (courses) með Jinja for-lykkju #}
    <h3>Áfangar á þessari önn:</h3>
    <ul>
    {% for afangi in courses %}
        <li>{{ afangi }}</li>
    {% endfor %}
    </ul>

```

---

### Hvernig þetta virkar:

* **Möppuskipulag:** Flask leitar sjálfkrafa í möppunni `templates/` að skránni `index.html`.
* **Gagnasending:** Heitin sem þú gefur í `render_template(user=..., courses=..., info=...)` verða að breytum inni í Jinja2 sniðmátinu.
* **Sjálfvirk öryggishreinsun:** Jinja2 hreinsar textann sjálfkrafa (*auto-escaping*) til að koma í veg fyrir öryggisgalla (eins og XSS-árásir) ef textinn inniheldur óæskilegan HTML-kóða.

---

#### Uppsetning vefþróunarsvæðis

- [How to build a Virtual Environment](how-to-build-venv/README.md)

---

### Routing

#### Sýnidæmi
1. [Flask uppsetning og Halló heimur](synidaemi/halloheimur.md)
1. [Static Routing](synidaemi/staticRoutes.py) 
1. [Static files](synidaemi/staticFiles.py)
1. [Error Handling](synidaemi/errorHandlingStatusCodes.py)
1. [url_for fallið](https://github.com/vefthroun/26H_VEF2VF05CU/blob/main/Verkefni1/namsefni/urlfor.py)
1. [Basic Data structure](synidaemi/datastructures.py)

#### Vefgreinar

1. [Quick start: Flask Routing](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
1. [The Art of Routing in Flask](https://hackersandslackers.com/flask-routes)
1. [The HTTP Protocol](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)

---

### Jinja templates

#### Sýnidæmi
1. [hlekkir og static](synidaemi/1-static.py)
1. [breytur og dictionary](synidaemi/2-breyta_og_dictionary.py)
1. [for in lykkja með lista](synidaemi/3-listi.py)
1. [for in lykkja með dictionary](synidaemi/4-dictionary_lykkja.py)

#### Vefgreinar
1. [Jinja](https://jinja.palletsprojects.com/en/3.0.x/templates/) 
1. [What is Jinja2?](https://python-web.teclado.com/section07/lectures/03_what_is_jinja2/)
1. [Variables & dictionary](https://youtu.be/pJ8V51XJuf0?list=PLXmMXHVSvS-ABlT4k4eS3YPJSnPUozw04) (video)
1. [Primer on Jinja Templating](https://realpython.com/primer-on-jinja-templating/)

---

### Dynamic Routes

### Kóðasýnidæmi

1. [Dynamic Routing](dynamic_routes/dynamic_routes.py)
1. [include í Jinja2](dynamic_routes/include.py)
1. [Listi með dictionaries, if/else og forlykkja í Jinja2](dynamic_routes/listi_dictionaries.py)
1. [Listi með dictionaries, forlykkja með if og include í Jinja2](dynamic_routes/include_forloop.py)
1. [Listi af tuples, forlykkja með if/else í Jinja2](dynamic_routes/listi_tuples.py)

---

### URL routing

- [Understanding URL Routing in Flask](https://www.sitepoint.com/flask-url-routing/)

### Jinja 

1. [Rendering Pages in Flask Using Jinja](https://hackersandslackers.com/flask-jinja-templates) 
1. [Jinja templates](https://realpython.com/primer-on-jinja-templating/)
2. [Base template & Nav bar](https://python-web.teclado.com/section12/lectures/03_base_template_and_nav_bar/)
1. [Loops & inheritance](https://youtu.be/APh3jdVryF0?list=PLXmMXHVSvS-ABlT4k4eS3YPJSnPUozw04) (video)
   
### CSS

- [Pico CSS](https://picocss.com/) 
