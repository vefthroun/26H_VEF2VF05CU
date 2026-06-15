# Epguides API

- https://epguides-api.readthedocs.io/en/latest/

Til að bæta sjónvarpsþáttasíðu við núverandi vefuppsetningu þína þarftu að nýta **Epguides API** til að sækja gögnin og **Flask** til að birta þau í gegnum sniðmát sem erfir frá `layout.html`.

Hér er hvernig þú getur útfært þetta:

### 1. Sækja gögn úr Epguides API
Epguides API er ókeypis REST þjónusta sem krefst ekki API-lykils. Þú getur notað Python-safnið `requests` til að sækja JSON gögn um þætti. Þar sem þú vilt aðeins birta 20 þætti geturðu notað skurð (e. slicing) í Python á listann sem API-ið skilar.

**Dæmi um Flask rás (route):**

```python
import requests
from flask import render_template

@app.route('/shows')
def shows():
    # Sækjum gögn frá Epguides API (þetta er dæmi um slóð)
    response = requests.get('https://epguides.frecar.no/shows/')
    all_shows = response.json()
    
    # Veljum aðeins fyrstu 20 þættina úr listanum
    top_20_shows = all_shows[:20]
    
    return render_template('shows.html', shows=top_20_shows)
```

### 2. Hanna shows.html með erfðum
Til að síðan passi inn í vefinn þinn á hún að nota `{% extends "layout.html" %}` eins og við ræddum áður [Conversation]. API-ið gefur þér gögn eins og titil, sjónvarpsstöð (network) og myndir frá TVMaze.

**Dæmi um shows.html:**
```html
{% extends "layout.html" %}

{% block title %}20 Vinsælir Þættir{% endblock %}

{% block content %}
    <h1>Sjónvarpsþættir</h1>
    <div class="shows-container">
        {% for show in shows %}
            <div class="show-card">
                <h3>{{ show.title }}</h3>
                <p><strong>Stöð:</strong> {{ show.network }}</p>
                <p><strong>Land:</strong> {{ show.country }}</p>
                {# Ef API-ið gefur myndaslóð er hún birt hér #}
                {% if show.image %}
                    <img src="{{ show.image }}" alt="{{ show.title }}" style="width:200px;">
                {% endif %}
            </div>
        {% endfor %}
    </div>
{% endblock %}
```

### 3. Samþætting við núverandi kerfi
*   **Navigation:** Bættu hlekk á nýju síðuna í `nav` hlutann í `layout.html` með því að nota `url_for('shows')` [39, Conversation].
*   **Gagnageymsla:** Ef þú vilt vista upplýsingar um uppáhalds þættina þína gætirðu notað **TinyDB** til að geyma þá í `db.json` skrá.
*   **Öryggi:** Flask sér sjálfkrafa um að **hreinsa (escape)** öll gögn sem koma úr API-inu áður en þau eru birt í Jinja2 sniðmátinu til að verjast öryggisvandanum.

**Af hverju þessi leið?**
Með því að nota API-ið beint þarftu ekki að skrá gögnin handvirkt í gagnagrunn. Með því að nota `render_template` og Jinja2 lykkjur (`{% for ... %}`) geturðu birt mikið magn af gögnum á skipulegan hátt með lágmarks kóðun.

---

Til þess að nota leitarvél **Epguides API** þarftu ekki sérstakan API-lykil, þar sem þjónustan er ókeypis og krefst engrar auðkenningar. Samkvæmt heimildum býður API-ið upp á tvær meginleiðir til að leita að sjónvarpsþáttum:

1.  **Hefðbundin leit (Search Shows):** Þessi virkni gerir þér kleift að finna sjónvarpsþætti eftir **titli** og skilar niðurstöðum samstundis. Hún er tilvalin til að nálgast lýsigögn (metadata) fyrir þúsundir þáttaraða.
2.  **Gervigreindardrifin leit (AI-Powered Search):** Hægt er að nota náttúrulegt mál til að leita að sértækum upplýsingum, svo sem „finale episodes“ (lokaþættir), til að fá nákvæmari niðurstöður.

### Framkvæmd leitarinnar:
Þar sem þetta er **REST API** fer leitin fram í gegnum HTTP-beiðnir (yfirleitt GET beiðnir). Eins og við ræddum í fyrra dæmi um að sækja 20 þætti, myndir þú nota Python `requests` safnið til að senda leitina á viðeigandi enda punkt (endpoint) sem tilgreindur er í tækniskjölun API-ins [1, 3, Conversation].

**Gögnin sem leitin skilar:**
Þegar þú leitar færðu gögn úr mörgum áttum í einum JSON pakka:
*   **Frá epguides.com:** Titill, sjónvarpsstöð, land og dagsetningar.
*   **Frá TVMaze:** Samantektir á þáttum og myndir (póstar og kyrrmyndir).
*   **Frá IMDB:** ID-númer til að geta tengt gögnin við IMDB gagnagrunninn.

Ef þú vilt samþætta þetta við Flask forritið þitt sem við höfum verið að vinna með, geturðu búið til nýja rás (route) þar sem notandi slær inn leitarorð í HTML form, og bakendinn sendir það orð áfram í Epguides API-ið til að birta niðurstöðurnar á undirsíðu sem notar `layout.html` [31, 44, Conversation].

Til að útfæra leitarform í Flask sem notar Epguides API þarftu að búa til HTML form sem sendir leitarorð á bakendann, þar sem Flask notar `requests` safnið til að spyrja API-ið og birta svo niðurstöðurnar [2, 50, Conversation].

Hér er skref-fyrir-skref útfærsla:

### 1. Búa til leitarformið (HTML)
Best er að setja leitarformið í `layout.html` svo það sé alltaf aðgengilegt, eða á sérstaka leitarsíðu. Við notum `GET` aðferðina fyrir leit svo notendur geti deilt niðurstöðunum með vefslóð.

```html
<form action="{{ url_for('search') }}" method="GET">
    <input type="text" name="q" placeholder="Leita að þætti..." required>
    <button type="submit">Leita</button>
</form>
```

### 2. Flask rásin (Route)
Í bakendanum notum við `request.args.get('q')` til að ná í leitarorðið úr vefslóðinni og sendum það áfram á Epguides API-ið. Epguides API krefst engrar auðkenningar, sem gerir þetta mjög einfalt.

```python
import requests
from flask import render_template, request

@app.route('/search')
def search():
    # 1. Sækjum leitarorðið úr forminu (?q=eitthvað)
    query = request.args.get('q')
    
    if query:
        # 2. Köllum í Epguides API leitarvélina
        # Ath: Endapunkturinn fyrir leit er yfirleitt /search/show?q=
        api_url = f"https://epguides.frecar.no/search/show?q={query}"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            results = response.json()
        else:
            results = []
    else:
        results = []

    return render_template('search_results.html', shows=results, query=query)
```

### 3. Birta niðurstöður (`search_results.html`)
Þessi síða erfir frá `layout.html` og birtir gögnin sem API-ið skilar, eins og titil, stöð og myndir frá TVMaze [3, 45, Conversation].

```html
{% extends "layout.html" %}

{% block title %}Leitarnrstöður: {{ query }}{% endblock %}

{% block content %}
    <h1>Leitarniðurstöður fyrir "{{ query }}"</h1>
    
    {% if shows %}
        <div class="results-grid">
            {% for show in shows %}
                <div class="show-card">
                    <h3>{{ show.title }}</h3>
                    <p><strong>Stöð:</strong> {{ show.network }}</p>
                    {% if show.image %}
                        <img src="{{ show.image }}" alt="{{ show.title }}" width="150">
                    {% endif %}
                </div>
            {% endfor %}
        </div>
    {% else %}
        <p>Engir þættir fundust með þessu nafni.</p>
    {% endif %}
{% endblock %}
```

### Af hverju þessi aðferð?
*   **Enginn API lykill:** Epguides API er opið og ókeypis, svo þú getur byrjað strax að gera beiðnir.
*   **Öryggi:** Flask og Jinja2 sjá sjálfkrafa um að **hreinsa (escape)** leitarorðið og gögnin úr API-inu áður en þau eru birt, sem verndar gegn sprautuhótunum (injection attacks).
*   **Notendavænt:** Með því að nota `request.args` (GET) getur notandinn notað „Back“ hnappinn í vafranum og farið aftur í leitarniðurstöðurnar án þess að fá villuboð um að senda þurfi formgögn aftur.

Til að birta myndir og lýsingar (summaries) frá TVMaze í gegnum Epguides API þarftu að nýta þau gögn sem API-ið skilar sjálfkrafa í JSON svari sínu. Þar sem TVMaze veitir lýsingar á þáttum og myndir (svo sem veggspjöld og kyrrmyndir), eru þessar upplýsingar aðgengilegar sem lyklar í þeim orðasöfnum (dicts) sem þú færð til baka.

Hér er hvernig þú útfærir þetta í Jinja2 sniðmátinu þínu:

### 1. Birting á lýsingu (Summary)
Lýsingar frá TVMaze innihalda oft HTML-tög (eins og `<p>` eða `<b>`). Flask og Jinja2 **hreinsa (escape)** öll gögn sjálfkrafa til að tryggja öryggi. Til að lýsingin birtist rétt en ekki sem hrár texti með tögum, þarftu að nota **`|safe`** síuna.

```html
<div class="show-summary">
    <h4>Um þáttinn:</h4>
    {# Notum |safe svo HTML tög frá TVMaze virki rétt #}
    {{ show.summary | safe }}
</div>
```
---

### 2. Birting á myndum (Images)
Myndirnar koma sem vefslóðir (URL). Þú setur þær í `src` eigindi `<img>` tagsins. Gott er að nota `if` skilyrði til að athuga hvort mynd sé til staðar áður en reynt er að birta hana [45, Conversation].

```html
{% if show.image %}
    <div class="show-poster">
        <img src="{{ show.image }}" alt="Veggspjald fyrir {{ show.title }}" style="max-width: 200px;">
    </div>
{% else %}
    <p>Engin mynd fáanleg.</p>
{% endif %}
```

### 3. Heildardæmi í `search_results.html`
Hér er hvernig þetta lítur út þegar þú vinnur með listann af niðurstöðum sem við ræddum áðan [Conversation]:

```html
{% extends "layout.html" %}

{% block content %}
    <h1>Leitarniðurstöður</h1>
    <div class="results">
        {% for show in shows %}
            <div class="show-item">
                <h2>{{ show.title }}</h2>
                
                {# Mynd frá TVMaze #}
                {% if show.image %}
                    <img src="{{ show.image }}" alt="{{ show.title }}">
                {% endif %}
                
                {# Lýsing frá TVMaze #}
                <div class="description">
                    {{ show.summary | safe }}
                </div>
                
                <p><strong>Frumsýnt:</strong> {{ show.start_date }}</p>
            </div>
            <hr>
        {% endfor %}
    </div>
{% endblock %}
```

### Mikilvæg atriði:
*   **Gagnauppspretta:** Epguides API sameinar gögn frá mörgum stöðum; titlar koma frá epguides.com en lýsingar og myndir eru sóttar beint frá TVMaze.
*   **Öryggi:** Þótt þú notir `|safe` fyrir lýsinguna, þá er það óhætt í þessu tilfelli þar sem gögnin koma frá traustum API-endapunkti, en almennt ættirðu að fara varlega með þá síu á gögn sem notendur slá inn sjálfir.
*   **Snið gagna:** Þar sem TinyDB og API-ið skila báðir gögnum sem Python orðasöfnum (dicts), er málfræðin í Jinja2 sú sama fyrir bæði (`show.lykill` eða `show['lykill']`) [4, 19, Conversation].