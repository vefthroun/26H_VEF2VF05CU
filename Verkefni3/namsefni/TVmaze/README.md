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
*   **HTML Escaping**: Jinja2 hreinsar sjálfkrafa gögn úr API-inu til að verja síðuna gegn árásum, nema við notum `| safe` sýuna (filter) fyrir gögn sem innihalda HTML merki (eins og `summary` úr TVMaze).
