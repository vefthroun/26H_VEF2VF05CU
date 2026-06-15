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

---

### Flokkun eftir greinum (_genres_)

Til þess að sýna **flokka (genres)** á vefsíðunni þinni þarftu að nýta það að Epguides API skilar ítarlegum lýsigögnum (metadata) um sjónvarpsþætti. Þó að flokkar séu ekki sérstaklega tilgreindir í grunn-töflunni yfir gögn frá epguides.com, þá fylgja þeir oft með í þeim gögnum sem API-ið dregur saman (t.d. frá TVMaze) [3, Conversation].

Hér er hvernig þú útfærir þetta tæknilega:

### 1. Meðhöndlun gagna í bakenda (Python)

Þegar þú færð svar frá API-inu er það á JSON sniði, sem Flask breytir í Python orðasafn (dicts). Flokkar eru yfirleitt geymdir sem **listi af strengjum** (t.d. `['Drama', 'Action', 'Sci-Fi']`) inni í hverjum þætti.

Þú ættir að nota `.get()` aðferðina til að sækja flokkana svo forritið hrynji ekki ef þeir vanta í gögnin.

```python
# Dæmi um hvernig gögnin gætu litið út í 'show' orðasafninu:
# show = {'title': 'The Flash', 'genres': ['Action', 'Drama', 'Sci-Fi'], ...}

# Í rásinni þinni (route):
@app.route('/show/<id>')
def show_details(id):
    # (Sækja gögn úr API hér...)
    show = response.json()
    return render_template('show.html', show=show)
```

### 2. Birting í Jinja2 sniðmáti (HTML)

Inni í `show.html` (eða sambærilegu skjali sem erfir frá `layout.html`) notarðu **`{% for %}` lykkju** til að ítreka í gegnum listann af flokkum og birta þá [45, Conversation].

```html
{% extends "layout.html" %}

{% block content %}
    <h1>{{ show.title }}</h1>

    <div class="genres">
        <strong>Flokkar:</strong>
        {# Athugum hvort genres sé til staðar og sé listi #}
        {% if show.genres %}
            {% for genre in show.genres %}
                <span class="genre-tag">{{ genre }}</span>
            {% endfor %}
        {% else %}
            <span>Engir flokkar skráðir</span>
        {% endif %}
    </div>

    <p>{{ show.summary | safe }}</p>
{% endblock %}
```
<!-- ath betur
### 3. Útlit og hönnun (CSS)
Til að gera flokkana meira áberandi er gott að hanna þá sem litla miða (tags) í `static/style.css` skránni þinni.

```css
.genre-tag {
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 2px 8px;
    margin-right: 5px;
    font-size: 0.9em;
    display: inline-block;
}
```
-->


Hér er dæmi um hvernig þú hantar **`shows.html`** til að birta upplýsingar úr Epguides API, með sérstaka áherslu á að nýta **myndir og lýsingar frá TVMaze**. Sniðmátið notar erfðir til að fylgja útliti vefsins þíns [45, Conversation].

### Dæmi um `shows.html`

```html
{# Erfum grunnútlit frá layout.html #}
{% extends "layout.html" %}

{% block title %}Sjónvarpsþættir úr Epguides{% endblock %}

{% block content %}
    <h1 class="page-title">Vinsælir sjónvarpsþættir</h1>

    <div class="shows-grid">
        {# Ítrum í gegnum listann af þáttum sem Flask sendi #}
        {% for show in shows %}
            <div class="show-card">
                
                {# 1. Birta mynd frá TVMaze #}
                <div class="show-image">
                    {% if show.image %}
                        <img src="{{ show.image }}" alt="Veggspjald fyrir {{ show.title }}" style="width:100%; border-radius: 8px;">
                    {% else %}
                        <div class="no-image">Engin mynd til staðar</div>
                    {% endif %}
                </div>

                <div class="show-info">
                    <h2>{{ show.title }}</h2>
                    <p><strong>Stöð:</strong> {{ show.network }} ({{ show.country }})</p>
                    
                    {# 2. Birta lýsingu frá TVMaze #}
                    {# Við notum |safe síuna því TVMaze skilar oft HTML tögum eins og <p> eða <b> #}
                    <div class="show-summary">
                        {{ show.summary | safe }}
                    </div>

                    <div class="show-meta">
                        <span>Frumsýnt: {{ show.start_date }}</span>
                    </div>

                    {# Hnappur til að vista í TinyDB uppáhaldslistann (Conversation) #}
                    <form action="{{ url_for('add_favorite') }}" method="POST">
                        <input type="hidden" name="show_id" value="{{ show.show_id }}">
                        <input type="hidden" name="title" value="{{ show.title }}">
                        <input type="hidden" name="image" value="{{ show.image }}">
                        <button type="submit" class="btn-fav">Bæta í uppáhald</button>
                    </form>
                </div>
            </div>
        {% endfor %}
    </div>
{% endblock %}
```

### Lykilatriði í þessari útfærslu:

*   **TVMaze Myndir:** Epguides API sameinar gögn þannig að þú færð beina slóð á veggspjöld (show posters) frá TVMaze í gegnum `show.image` lykilinn.
*   **HTML í lýsingum:** TVMaze skilar lýsingum (summaries) með HTML sniði. Jinja2 **hreinsar sjálfkrafa** öll gögn til að verjast öryggisvanda. Þess vegna verður þú að nota **`|safe`** síuna til að lýsingin birtist með réttum málsgreinum og áherslum í stað þess að sýna hráan kóða.
*   **Gagnauppspretta:** Inni í þessu eina orðasafni (dict) ertu að blanda saman gögnum frá **epguides.com** (titill og stöð) og **TVMaze** (myndir og samantektir).
*   **Sveigjanleiki:** Með því að nota `{% if show.image %}` kemurðu í veg fyrir að vefsíðan sýni brotnar myndir ef API-ið vantar mynd fyrir tiltekinn þátt [Conversation].
*   **Skipulag:** Með því að setja þetta í `shows-grid` klasa geturðu notað CSS Flexbox eða Grid til að raða þáttunum hlið við hlið á fallegan hátt [42, Conversation].

Til þess að birta mismunandi gerðir mynda, svo sem **veggspjöld (posters)** eða **kyrrmyndir (stills)**, þarftu að nýta gögnin sem Epguides API sækir frá TVMaze. API-ið flokkar myndirnar eftir því hvort þú ert að skoða upplýsingar um heila þáttaröð, eina seríu eða einstaka þætti.

Hér er hvernig þú nálgast og birtir þessar mismunandi myndgerðir:

### 1. Tegundir mynda í boði

Samkvæmt tæknilýsingu API-ins eru þrjár megingerðir mynda fáanlegar:
*   **Show Posters:** Aðal-veggspjöld fyrir sjónvarpsþáttinn (notað í almennri leit og yfirliti).
*   **Season Posters:** Veggspjöld sem eru sértæk fyrir hverja seríu (season).
*   **Episode Stills:** Kyrrmyndir úr hverjum einstökum þætti.

### 2. Birting í Jinja2 sniðmáti
Í fyrri dæmum okkar notuðum við `show.image` til að birta aðalveggspjaldið [Conversation]. Ef þú ert að birta lista yfir einstaka þætti eða seríur mun orðasafnið (dict) sem API-ið skilar innihalda mismunandi lykla fyrir myndirnar.

**Dæmi um hvernig á að birta kyrrmyndir úr þáttum:**
Ef þú ert að ítra í gegnum lista af þáttum (`episodes`) þá fylgir kyrrmynd oft með hverjum þætti.

```html
{% for episode in episodes %}
    <div class="episode-box">
        <h4>{{ episode.title }} (S{{ episode.season }}E{{ episode.number }})</h4>
        
        {# Birta kyrrmynd (still) ef hún er til staðar #}
        {% if episode.image %}
            <img src="{{ episode.image }}" alt="Kyrrmynd úr {{ episode.title }}" class="episode-still">
        {% else %}
            <p>Engin mynd fáanleg fyrir þennan þátt.</p>
        {% endif %}
        
        <p>{{ episode.summary | safe }}</p>
    </div>
{% endfor %}
```

### 3. Meðhöndlun gagnanna

*   **Heimild gagna:** Allar þessar myndir eru hýstar hjá TVMaze en Epguides API sér um að tengja þær við réttan þátt eða seríu.
*   **Varnir gegn villum:** Mikilvægt er að nota `if` skilyrði í HTML-inu (eins og sýnt er hér að ofan) því API-ið gæti vantað kyrrmyndir fyrir mjög nýja eða gamla þætti [Conversation].
*   **Geymsla í TinyDB:** Ef þú vilt að notendur geti vistað ákveðna kyrrmynd í uppáhald, þarftu að geyma viðeigandi myndaslóð í `db.json` skránni þinni undir nýjum lykli, t.d. `'image_type': 'still'` e'a `'image_type': 'poster'` [5, Conversation].

**Samantekt:** Þú velur myndgerðina með því að kalla á rétta rás (endpoint) í API-inu. Ef þú kallar á `/show/` færðu veggspjöld, en ef þú kallar á `/show/episode/` færðu kyrrmyndir.

---

> Aukaefni sem hægt er að framkvæma ef tími vinnst til

### 4. Geymsla í TinyDB

Ef þú vistar þátt í uppáhald í **TinyDB**, þá vistar þú allan listann af flokkum beint í `db.json` skrána [5, Conversation]. Þar sem TinyDB vinnur með Python orðasöfn og lista bókstaflega, þarftu enga sérstaka vinnslu til að geyma listann.

**Lykilatriði:**
*   **Gagnagerð:** Mundu að flokkar eru listi. Þú getur ekki notað þá beint eins og titil (streng), heldur þarftu að nota lykkju til að birta hvern flokk fyrir sig.
*   **API-svör:** Ef þú notar leitarvél Epguides API eins og við ræddum áður, þá fylgja flokkarnir oft með í hverri niðurstöðu [2, Conversation].
*   **Sjálfgefin gildi:** Alltaf er öruggast að nota `show.get('genres', [])` í bakenda eða `{% if show.genres %}` í sniðmáti til að forðast villur ef gögn vantar.

---

### Tinydb og Epguides samþætting

það er hægt að vista uppáhalds þætti úr Epguides API í TinyDB. Þar sem bæði API-ið skilar gögnum á JSON sniði og TinyDB geymir gögn sem Python orðasöfn (dicts), þá smellpassa þessi kerfi saman [2, 5, Conversation].

Hér er hvernig þú getur útfært þetta:

### 1. Undirbúningur í gagnagrunni
Best er að búa til sérstaka töflu í `db.json` skránni þinni fyrir uppáhalds þætti. Þannig haldast þeir aðskildir frá notendum og almennum spjallpóstum [Conversation].

```python
from tinydb import TinyDB, Query
db = TinyDB('db.json')
fav_table = db.table('favorites')
Fav = Query()
```

### 2. Vista þátt (Insert)
Þegar notandi smellir á „Vista sem uppáhalds“ í viðmótinu, sendir þú upplýsingarnar um þáttinn á bakendann. Þú bætir svo **notanda-ID** úr session-inu við orðasafnið áður en þú vistar það, svo þú vitir hver á þetta uppáhald [20, Conversation].

```python
@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Sækjum gögnin sem API-ið gaf okkur (t.d. úr hidden fields í formi)
    show_data = {
        'user_id': session['user_id'],
        'show_id': request.form.get('show_id'),
        'title': request.form.get('title'),
        'image': request.form.get('image')
    }

    # Athugum fyrst hvort þátturinn sé þegar í uppáhaldi hjá þessum notanda
    existing = fav_table.search((Fav.user_id == session['user_id']) & (Fav.show_id == show_data['show_id']))
    
    if not existing:
        fav_table.insert(show_data) # Vistum í TinyDB
        flash(f"{show_data['title']} hefur verið bætt við uppáhald!")
    
    return redirect(url_for('shows'))
```

### 3. Birta uppáhalds þætti (Filter)

Á prófílsíðunni þinni geturðu svo notað `db.search()` til að sía út og birta aðeins þá þætti sem tengjast þeim notanda sem er innskráður [7, Conversation].

```python
@app.route('/profile')
def profile():
    if 'user_id' in session:
        # Sækjum aðeins uppáhalds þætti þessa notanda
        my_favs = fav_table.search(Fav.user_id == session['user_id'])
        return render_template('profile.html', favorites=my_favs)
    return redirect(url_for('login'))
```

### Kostir þessarar nálgunar:

*   **Gagnageymsla:** TinyDB geymir þetta bókstaflega í `db.json` skránni þinni, svo þættirnir „hverfa“ ekki þótt þú lokir vafranum.
*   **Tenging við TVMaze:** Þar sem þú vistar myndaslóðina og lýsinguna úr API-inu í TinyDB, þarftu ekki að kalla aftur í API-ið í hvert sinn sem notandinn skoðar prófílinn sinn [3, Conversation].
*   **Einföld eyðing:** Ef notandi vill fjarlægja þátt úr uppáhaldi notarðu einfaldlega `fav_table.remove()` með viðeigandi skilyrði.

Með því að sameina **session** (fyrir auðkenningu), **API** (fyrir gögnin) og **TinyDB** (fyrir geymslu) ertu kominn með fullmótað „Show Tracker“ forrit.

Til þess að birta alla uppáhalds þætti sem vistaðir hafa verið í **TinyDB**, þarftu að búa til nýja rás (route) í Flask sem sækir gögnin úr réttri töflu og birtir þau í gegnum sniðmát sem notar erfðir [44, 45, Conversation].

Hér er hvernig þú útfærir þetta:

### 1. Bakendinn: Sækja gögn úr TinyDB

Í Flask rásinni notarðu **`db.table('favorites')`** til að nálgast uppáhaldslistann og **`search()`** aðferðina til að sía þætti sem tilheyra þeim notanda sem er innskráður í gegnum **session** [7, 57, Conversation].

```python
from flask import render_template, session, redirect, url_for
from tinydb import TinyDB, Query

db = TinyDB('db.json')
fav_table = db.table('favorites')
Fav = Query()

@app.route('/my_favorites')
def my_favorites():
    # 1. Athugum hvort notandi sé innskráður með session
    if 'user_id' not in session:
        return redirect(url_for('login')) # Ef ekki, sendum á innskráningu

    # 2. Sækjum aðeins þá þætti þar sem user_id í gagnagrunni passar við session
    # TinyDB skilar lista af orðasöfnum (dictionaries)
    user_favs = fav_table.search(Fav.user_id == session['user_id'])

    # 3. Sendum listann á sniðmátið
    return render_template('favorites.html', shows=user_favs)
```

### 2. Framendinn: Birta gögnin í `favorites.html`

Sniðmátið notar **`{% extends "layout.html" %}`** til að halda samræmdu útliti og **`{% for %}`** lykkju til að ítra í gegnum listann af þáttum [44, 45, Conversation].

```html
{% extends "layout.html" %}

{% block title %}Mínir uppáhalds þættir{% endblock %}

{% block content %}
    <h1>Mínir uppáhalds þættir</h1>

    {% if shows %}
        <div class="favorites-grid">
            {% for show in shows %}
                <div class="show-card">
                    {# Aðgangur að gildum í orðasafni með lyklum #}
                    <h3>{{ show.title }}</h3>
                    
                    {% if show.image %}
                        <img src="{{ show.image }}" alt="{{ show.title }}" width="200">
                    {% endif %}
                    
                    <p><strong>Stöð:</strong> {{ show.network }}</p>
                    
                    {# Hlekkur til að fjarlægja, ef þú vilt útfæra það síðar #}
                    <a href="{{ url_for('remove_favorite', show_id=show.show_id) }}">Fjarlægja</a>
                </div>
            {% endfor %}
        </div>
    {% else %}
        <p>Þú hefur ekki bætt neinum þáttum við í uppáhald ennþá.</p>
        <a href="{{ url_for('shows') }}">Skoða þætti úr API</a>
    {% endif %}
{% endblock %}
```

### Lykilatriði í þessari útfærslu:

*   **Sía eftir notanda:** Með því að nota `Fav.user_id == session['user_id']` tryggirðu að notendur sjái aðeins sína eigin þætti en ekki þætti annarra [7, Conversation].
*   **Gagnageymsla:** TinyDB vistar þessi gögn sem Python orðasöfn í `db.json`, sem gerir það auðvelt að sækja bæði titla og myndir sem komu upprunalega úr **Epguides API** eða **TVMaze** [3, 5, Conversation].
*   **Sjálfvirk hreinsun:** Flask og Jinja2 sjá sjálfkrafa um að **hreinsa (escape)** öll gögn sem birt eru úr gagnagrunninum til að verjast öryggisvandanum.
*   **Dictionary Access:** Inni í sniðmátinu notarðu punkt-málfræði (`show.title`) til að nálgast gildi í orðasafni, sem svarar til þess að nota lykla í Python.

Til að eyða þætti úr uppáhaldi í TinyDB gagnagrunninum þínum þarftu að nota **`db.remove(query)`** skipunina. Til að tryggja öryggi er mikilvægt að eyðingin sé bundin við bæði **ID þáttarins** og **ID notandans** úr session-inu [57, Conversation].

Hér er hvernig þú útfærir þessa rás (route) í Flask:

### 1. Flask rás fyrir eyðingu

Þú býrð til rás sem tekur við auðkenni þáttarins (t.d. `show_id`) og notar samsetta fyrirspurn til að fjarlægja rétta skjalið úr `favorites` töflunni.

```python
from flask import session, redirect, url_for, flash
from tinydb import Query

# Gerum ráð fyrir að fav_table sé þegar skilgreint [Conversation]
Fav = Query()

@app.route('/remove_favorite/<show_id>')
def remove_favorite(show_id):
    # 1. Athuga hvort notandi sé innskráður
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # 2. Eyða þættinum úr töflunni
    # Við tryggjum að notandinn geti bara eytt sínum eigin uppáhaldi [7, Conversation]
    fav_table.remove((Fav.user_id == session['user_id']) & (Fav.show_id == show_id))
    
    # 3. Gefa notanda endurgjöf og senda hann aftur á listann
    flash("Þætti hefur verið eytt úr uppáhaldi.")
    return redirect(url_for('my_favorites'))
```

### 2. Lykilatriði í útfærslunni:

*   **`db.remove(query)`**: Þessi aðferð fjarlægir öll skjöl í TinyDB sem passa við skilyrðin í fyrirspurninni.
*   **Öryggi með Session**: Með því að bæta `Fav.user_id == session['user_id']` við fyrirspurnina kemurðu í veg fyrir að einn notandi geti eytt uppáhaldslistanum hjá öðrum með því að giska á vefslóðina [57, Conversation].
*   **Samsett skilyrði**: Notað er **`&`** merkið til að tengja saman tvö skilyrði í TinyDB fyrirspurninni.
*   **Endurgjöf (Flashing)**: Gott er að nota `flash()` til að staðfesta fyrir notandanum að aðgerðin hafi tekist.

### 3. Hlekkur í HTML sniðmáti

Í `favorites.html` skjalinu þínu (sem við ræddum áðan) myndirðu hafa hlekk sem kallar á þessa rás [39, Conversation]:

```html
<a href="{{ url_for('remove_favorite', show_id=show.show_id) }}" 
   onclick="return confirm('Ertu viss um að þú viljir eyða þessum þætti?')">
   Eyða úr uppáhaldi
</a>
```

Með þessu móti er CRUD virknin (Create, Read, Update, Delete) fyrir uppáhalds þættina orðin fullmótuð í forritinu þínu.

Hönnunin á **`favorites.html`** síðunni byggir á því að taka á móti lista af orðasöfnum (dicts) frá Flask og birta þau á skipulegan hátt með Jinja2 málfræði [44, 45, Conversation]. Þar sem síðan er hluti af stærra kerfi, á hún að nýta erfðir til að viðhalda samræmdu útliti.

Hér er hvernig þú hantar síðuna skref fyrir skref:

### 1. Grunnurinn: Erfðir og blokkir
Eins og aðrar undirsíður í appinu þínu á þessi síða að byrja á því að erfa frá `layout.html`. Þú skilgreinir svo titil síðunnar og aðalinnihaldið inni í viðeigandi blokkum.

```html
{% extends "layout.html" %}

{% block title %}Mínir uppáhalds þættir{% endblock %}

{% block content %}
    <h1>Mínir uppáhalds þættir</h1>
    {# Hér kemur innihaldið #}
{% endblock %}
```

### 2. Meðhöndlun gagna (If/For lykkjur)

Þar sem TinyDB skilar lista af niðurstöðum, eða tómum lista ef ekkert finnst, er mikilvægt að byrja á því að athuga hvort einhverjir þættir séu til staðar [6, 7, Conversation]. Ef svo er, notarðu `{% for %}` lykkju til að ítreka í gegnum hvern þátt.

```html
{% if shows %}
    <div class="favorites-container">
        {% for show in shows %}
            <div class="favorite-card">
                {# Hér birtum við upplýsingar um hvern þátt #}
            </div>
        {% endfor %}
    </div>
{% else %}
    <p>Þú hefur ekki bætt neinum þáttum við í uppáhald ennþá.</p>
    <a href="{{ url_for('shows') }}">Skoða þætti úr API</a>
{% endif %}
```

### 3. Birting á lýsigögnum (Metadata)

Inni í lykkjunni nálgast þú gildin úr hverju orðasafni með punkt-málfræði (t.d. `show.title`), sem er jafngilt því að nota lykla í Python [19, Conversation]. 
*   **Myndir**: Notaðu `<img>` tag með slóðinni sem þú vistaðir úr Epguides/TVMaze API-inu [Conversation].
*   **Texti**: Birtu titil og sjónvarpsstöð (network) [3, Conversation].
*   **Eyðing**: Bættu við hlekk sem notar `url_for` til að kalla á eyðingar-rásina (route) sem við ræddum áðan [39, Conversation].

**Dæmi um innihald kortsins:**
```html
<div class="favorite-card">
    <h3>{{ show.title }}</h3>
    
    {% if show.image %}
        <img src="{{ show.image }}" alt="{{ show.title }}" class="poster">
    {% endif %}

    <p><strong>Stöð:</strong> {{ show.network }}</p>
    
    <div class="actions">
        {# Hlekkur til að eyða úr uppáhaldi #}
        <a href="{{ url_for('remove_favorite', show_id=show.show_id) }}" 
           class="delete-btn"
           onclick="return confirm('Ertu viss?')">
           Fjarlægja
        </a>
    </div>
</div>
```

### Lykilatriði við hönnunina:

*   **Skipulag**: Notaðu CSS (í `static/style.css`) til að láta `.favorites-container` nota Flexbox eða Grid svo þættirnir raðist fallega upp hlið við hlið.
*   **Öryggi**: Mundu að Flask hreinsar (escapes) sjálfkrafa öll gögn, þannig að ef þú birtir lýsingar (summaries) sem innihalda HTML tög frá TVMaze þarftu að nota `{{ show.summary | safe }}` [35, 45, Conversation].
*   **Feedback**: Síðan mun sjálfkrafa sýna flash-skilaboð (eins og „Þætti eytt“) ef þú hefur sett `get_flashed_messages()` inn í `layout.html` grunnskjalið þitt [45, 60, Conversation].
