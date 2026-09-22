### Að sækja gögn frá API

- Hlekkurinn / API endpoint [https://api.tvmaze.com/shows](https://api.tvmaze.com/shows) 
    - skilar upplýsingum um 250 fyrstu þáttarraðir í API gagnasettinu.  Til að fá næstu 250 þætti þarftu að bæta við skilyrðinu / flagginu ?page=1 fyrir aftan shows eða [https://api.tvmaze.com/shows?page=1](https://api.tvmaze.com/shows?page=1) og svo framvegis 
- Hlekkurinn / API endpoint [https://api.tvmaze.com/shows/155](https://api.tvmaze.com/shows/155) 
    - skilar okkur upplýsingum um þáttaröð eftir id:  Í þessu tilviki þáttaröðina Beauty & the Beast sem hefur id = 155. 
- Hér er dæmi um leit á TVMaze API.
    - Leit að þætti eftir nafni, ekki nákvæm leit (fuzzy).  Hér er leitað eftir strengnum shark: [https://api.tvmaze.com/search/shows?q=shark](https://api.tvmaze.com/search/shows?q=shark)

### Dæmi um gögn - upplýsingar um eina þáttaröð:
  
```python
{
  "id": 155,
  "url": "https://www.tvmaze.com/shows/155/beauty-the-beast",
  "name": "Beauty & the Beast",
  "type": "Scripted",
  "language": "English",
  "genres": [
    "Action",
    "Romance",
    "Science-Fiction"
  ],
  "status": "Ended",
  "runtime": 60,
  "averageRuntime": 60,
  "premiered": "2012-10-11",
  "ended": "2016-09-15",
  "officialSite": "http://www.cwtv.com/shows/beauty-and-the-beast",
  "schedule": {
    "time": "21:00",
    "days": [
      "Thursday"
    ]
  },
  "rating": {
    "average": 7.4
  },
  "weight": 97,
  "network": {
    "id": 5,
    "name": "The CW",
    "country": {
      "name": "United States",
      "code": "US",
      "timezone": "America/New_York"
    },
    "officialSite": "https://www.cwtv.com/"
  },
  "webChannel": null,
  "dvdCountry": null,
  "externals": {
    "tvrage": 30717,
    "thetvdb": 258959,
    "imdb": "tt2193041"
  },
  "image": {
    "medium": "https://static.tvmaze.com/uploads/images/medium_portrait/0/2128.jpg",
    "original": "https://static.tvmaze.com/uploads/images/original_untouched/0/2128.jpg"
  },
  "summary": "Detective Catherine Chandler is a smart, no-nonsense homicide detective. When she was a teenager, she witnessed the murder of her mother at the hands of two gunmen and herself was saved by someone – or something. Years have passed and while investigating a murder, Catherine discovers a clue that leads her to Vincent Keller, who was reportedly killed in 2002. Catherine learns that Vincent is actually still alive and that it was he who saved her many years before. For mysterious reasons that have forced him to live outside of traditional society, Vincent has been in hiding for the past 10 years to guard his secret – when he is enraged, he becomes a terrifying beast, unable to control his super-strength and heightened senses.",
  "updated": 1729753783,
  "_links": {
    "self": {
      "href": "https://api.tvmaze.com/shows/155"
    },
    "previousepisode": {
      "href": "https://api.tvmaze.com/episodes/905489",
      "name": "Au Revoir"
    }
  }
}
```

---

### Sækja og birta gögn frá TVMaze API

Þessi hluti útskýrir hvernig miðlarinn (Flask) kallar í TVMaze API, fær JSON svar og sendir það áfram í HTML sniðmát (templates).

#### 1. Bakendinn: Flask rás (Route)
Í Flask er notað `requests` safnið til að sækja gögnin. API-ið skilar JSON sem Flask breytir í Python lista eða orðasafn (dictionary). Gögnin eru svo send í sniðmátið með `render_template()`.

```python
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Sækjum lista yfir þætti frá TVMaze API
    response = requests.get("https://api.tvmaze.com/shows")
    
    # Breytum JSON svarinu í Python gögn
    shows_data = response.json()
    
    # Sendum gögnin á index.html sniðmátið
    return render_template('index.html', shows=shows_data)
```

#### 2. Grunnútlit: `layout.html`
Við notum Jinja erfðir til að halda samræmdu útliti. `layout.html` inniheldur grunninn og `{% block content %}` segir til um hvar undirsíður eiga að birtast.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Sjónvarpsþættir</title>
</head>
<body>
    <nav>
        <a href="/">Heim</a>
    </nav>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>Gögn frá TVMaze API</p>
    </footer>
</body>
</html>
```

#### 3. Undirsíða: `index.html`
Þessi síða erfir frá `layout.html` og notar `{% for %}` lykkju til að ítra í gegnum listann af þáttum sem kom úr API-inu.

```html
{% extends "layout.html" %}

{% block content %}
    <h1>Vinsælir þættir</h1>
    
    {% for show in shows %}
        <div>
            <h2>{{ show.name }}</h2>
            
            {% if show.image %}
                <img src="{{ show.image.medium }}" alt="{{ show.name }}">
            {% endif %}
            
            <p><strong>Tegund:</strong> {{ show.genres | join(', ') }}</p>
            <p>{{ show.summary | safe }}</p>
            <hr>
        </div>
    {% endfor %}
{% endblock %}
```

### Lykilatriði:
*   **JSON sjálfvirkni**: Flask og TVMaze vinna bæði með JSON snið sem er auðvelt að varpa yfir í Python orðasöfn.
*   **Jinja2 Erfðir**: Með því að nota `{% extends %}` þurfum við ekki að endurtaka HTML kóða fyrir valmyndir eða fót (footer) á hverri síðu.
*   **HTML Escaping**: Jinja2 hreinsar sjálfkrafa gögn úr API-inu til að verja síðuna gegn árásum, nema við notum `| safe` síuna (filter) fyrir gögn sem innihalda HTML merki (eins og `summary` úr TVMaze).

---

Hér er yfirlit yfir helstu endapunkta (endpoints) **TVmaze API**. Grunnvefslóðin (root URL) fyrir öll köll er `https://api.tvmaze.com`.

---

### 1. Sjónvarpsþættir (Shows)
* **Aðalupplýsingar um þátt (Show Main Information)**:
  `GET /shows/:id`
  * *Dæmi:* `https://api.tvmaze.com/shows/1`
* **Listi yfir alla þætti (Show Episode List)**:
  `GET /shows/:id/episodes`
  * *Dæmi:* `https://api.tvmaze.com/shows/1/episodes`
* **Listi yfir árstíðir (Show Seasons)**:
  `GET /shows/:id/seasons`
  * *Dæmi:* `https://api.tvmaze.com/shows/1/seasons`
* **Aðalleikarar (Show Cast)**:
  `GET /shows/:id/cast`
  * *Dæmi:* `https://api.tvmaze.com/shows/1/cast`
* **Tæknifólk / Starfslið (Show Crew)**:
  `GET /shows/:id/crew`
  * *Dæmi:* `https://api.tvmaze.com/shows/1/crew`
* **Aukaheiti (Show AKAs)**:
  `GET /shows/:id/akas`
  * *Dæmi:* `https://api.tvmaze.com/shows/1/akas`
* **Myndir (Show Images)**:
  `GET /shows/:id/images`
  * *Dæmi:* `https://api.tvmaze.com/shows/1/images`
* **Einn ákveðinn þáttur eftir seríu- og þáttanúmeri (Episode by Number)**:
  `GET /shows/:id/episodebynumber?season=:season&number=:number`
  * *Dæmi:* `https://api.tvmaze.com/shows/1/episodebynumber?season=1&number=1`
* **Þættir eftir loftunardegi (Episodes by Date)**:
  `GET /shows/:id/episodesbydate?date=:date`
  * *Dæmi:* `https://api.tvmaze.com/shows/1/episodesbydate?date=2013-07-01`
* **Heildarlisti yfir þætti með síðutali (Show Index)**:
  `GET /shows?page=:num`
  * *Dæmi:* `https://api.tvmaze.com/shows?page=1`

---

### 2. Stakir þættir (Episodes)
* **Aðalupplýsingar um stakan þátt (Episode Main Information)**:
  `GET /episodes/:id`
  * *Dæmi:* `https://api.tvmaze.com/episodes/1`
* **Gestaleikarar í þátti (Episode Guest Cast)**:
  `GET /episodes/:id/guestcast`
  * *Dæmi:* `https://api.tvmaze.com/episodes/1/guestcast`
* **Gestatæknifólk í þátti (Episode Guest Crew)**:
  `GET /episodes/:id/guestcrew`
  * *Dæmi:* `https://api.tvmaze.com/episodes/1/guestcrew`

---

### 3. Árstíðir (Seasons)
* **Þættir innan ákveðinnar árstíðar (Season Episodes)**:
  `GET /seasons/:id/episodes`
  * *Dæmi:* `https://api.tvmaze.com/seasons/1/episodes`

---

### 4. Leit (Search)
* **Almenn leit að þætti (Show Search - fuzzy search)**:
  `GET /search/shows?q=:query`
  * *Dæmi:* `https://api.tvmaze.com/search/shows?q=girls`
* **Einstök leit að þætti (Show Single Search)**:
  `GET /singlesearch/shows?q=:query`
  * *Dæmi:* `https://api.tvmaze.com/singlesearch/shows?q=girls`
* **Fletta upp þætti eftir IMDB / TVDB ID (Show Lookup)**:
  `GET /lookup/shows?imdb=:id` eða `GET /lookup/shows?thetvdb=:id`
* **Leit að leikurum eða fólki (People Search)**:
  `GET /search/people?q=:query`
  * *Dæmi:* `https://api.tvmaze.com/search/people?q=lauren`

---

### 5. Fólk og leikarar (People)
* **Aðalupplýsingar um persónu / leikara (Person Main Information)**:
  `GET /people/:id`
  * *Dæmi:* `https://api.tvmaze.com/people/1`
* **Leikferill persónu (Person Cast Credits)**:
  `GET /people/:id/castcredits`
  * *Dæmi:* `https://api.tvmaze.com/people/1/castcredits`

---

### 6. Samþætting gagna í einu kalli (Embedding)
Margar af þessum slóðum styðja `embed` breytuna til að draga inn tengd gögn (t.d. leikara eða þáttalista) í sama svari án þess að gera mörg köll:
* `https://api.tvmaze.com/shows/1?embed=cast`
* `https://api.tvmaze.com/shows/1?embed=episodes`
* `https://api.tvmaze.com/shows/1?embed[]=episodes&embed[]=cast`

💡 Viltu að ég sýni þér dæmi um hvernig á að útfæra tiltekna rás í Flask (t.d. fyrir leikara/cast eða árstíðir) og birta gögnin í Jinja2 sniðmáti?

---

### Listi yfir kvikmyndagreinar _(Genres)_

The specific genres actively used and supported by the **TVmaze** database include:

* Action
* Anime
* Adventure
* Children
* Comedy
* Crime
* DIY
* Drama
* Espionage
* Family
* Fantasy
* Food
* History
* Horror
* Legal
* Medical
* Music
* Mystery
* Nature
* Romance
* Science-Fiction
* Sports
* Supernatural
* Thriller
* Travel
* War
* Western

---

### Hvernig á að sækja þátt úr þáttaröð

Í vefsíðu sem sýnir þætti í þáttaröð þá getur notandi smellt á hlekk sem vísar á einstakann þátt á rásinni:
`/episode/<show_id>/<season_number>/<episode_number>` 

### Skref-fyrir-skref útskýring á breytunum:

#### 1. Sótt **ID fyrir þáttaröðina (Show ID)**:
`{{ ep['_links']['show']['href'].split('/')[-1] }}`
* **`ep['_links']['show']['href']`**: TVMaze API styðst við HAL/HATEOAS staðalinn og skilar tenglum í eigninni `_links`. Þetta gefur fulla vefslóð á þáttaröðina, t.d. `"https://api.tvmaze.com/shows/155"`.
* **`.split('/')`**: Þetta er Python strengjaaðferð sem skiptir slóðinni upp í lista af strengjum miðað við skástrikin (`/`). Niðurstaðan verður t.d. `['https:', '', 'api.tvmaze.com', 'shows', '155']`.
* **`[-1]`**: Vísar í **síðasta stakið** í listanum, sem er auðkenni þáttaraðarinnar (ID-talan, t.d. `155`). Þetta er gagnleg tækni þegar `ep` hluturinn geymir ekki `show_id` sem stakan reit.

#### 2. Sótt **seríunúmer (Season)**:
`{{ ep['season'] }}`
* Nálgast númer árstíðarinnar/seríunnar úr orðasafni þáttarins (t.d. `1`).

#### 3. Sótt **þáttanúmer (Number)**:
`{{ ep['number'] }}`
* Nálgast númer þáttarins innan þeirrar seríu (t.d. `3`).

#### 4. Sýnilegur texti hlekksins:
`{{ ep['number'] }} - {{ ep['name'] }}`
* Birtir þáttanúmerið og heiti þáttarins á síðunni fyrir notandann, t.d. **`3 - Baelor`**.

---

### Dæmi um útkomu í HTML:
Ef þátturinn er 3. þáttur í 1. seríu af þáttaröð með ID `155` sem heitir *"Baelor"*, mun Jinja2 þýða kóðann yfir í eftirfarandi HTML:

```html
<li>
    Episode: <a href="/episode/155/1/3">3 - Baelor</a>
</li>
```

Þessi slóð passar svo við Flask rás í bakendanum sem tæki t.d. við breytunum svona: `@app.route('/episode/<int:show_id>/<int:season>/<int:number>')`.
