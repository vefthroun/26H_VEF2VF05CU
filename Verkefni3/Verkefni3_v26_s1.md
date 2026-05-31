## Verkefni 3  
- 20% af heildareinkunn
- Viðfangsefni:
  - CRUD aðgerðir með JSON / [TinyDB](https://tinydb.readthedocs.io/en/latest/getting-started.html)
  - API, requests
  - Jinja2: Template inheritance, Include
  - HTML Form
  - Uppsetning (_Layout_) 

---

### Verkefnalýsing
 
Útfærðu vefforrit í Flask sem nýtir JSON skrá og API. Notum [TVMaze API](https://www.tvmaze.com/api)

1. Á forsíðu (index) skal birta grunnupplýsingar um 20 random þætti ur _TVMaze API_ gagnagrunninum. Birta skal nafn og mynd þáttaraða  **20%**
1. Þegar valin er ein þáttaröð af forsíðu er farið á síðu sem birtir nánari upplýsingar um valda þáttaröð. **20%**
    - nafn þáttaraðar (name)
    - mynd (image/medium)
    - textalýsing þáttaraðar (summary)
    - lengd þáttaraðar (runtime)
    - útgáfudagur þáttaraðar (premiered), íslensk dagsetning
    - dagsetning síðasta þáttar (ended)
    - flokkar þáttaraðar (genres)
1. Í valmynd er hlekkur á forsíðu, alla flokka (má vera í fellivalslista - select field), Um mig og leitarreitur þar sem hægt er að leita að ákveðinni þáttaröð úr TVMaze gagnagrunninum.  **10%**
1. Þegar valin er einn flokkur (genre) úr valmynd birtir kerfið vefsíðu með þáttaröðum sem tilheyra völdum flokki. Sömu upplýsingar og á forsíðu nafn og mynd **15%**
1. Þegar leitað er að þáttaröð er nafn slegið inn í leitarreit og ýtt á hnapp / takka.  Þá fer kerfið á vefsíðu sem birtir helstu upplýsingar um þáttaraðir sem tilheyra nafninu í leitarstregnum ( helstu upplýsingar nafn og mynd ).**15%**
1. Hægt er að uppfæra upplýsingar (edit) í Um mig (_profile_), gögn eru skráð og sótt í JSON skrá, notum TinyDB til að höndla þetta. **10%**
1. Notaðu eigið CSS Grids fyrir uppsetningu (layout) og Pico CSS / NEW.CSS / .... **5%**
1. Notið erfðir (Jinja2:inheritance) og include (nav og footer) á vefsíðum. **5%**


#### Að sækja gögn frá API
Hlekkurinn / API endpoint [https://api.tvmaze.com/shows](https://api.tvmaze.com/shows) skilar upplýsingum um 250 fyrstu þáttarraðir í API gagnasettinu.  Til að fá næstu 250 þætti þarftu að bæta við skilyrðinu / flagginu ?page=1 fyrir aftan shows eða [https://api.tvmaze.com/shows?page=1](https://api.tvmaze.com/shows?page=1) og svo framvegis 

Hlekkurinn / API endpoint [https://api.tvmaze.com/shows/155](https://api.tvmaze.com/shows/155) skilar okkur upplýsingum um þáttaröð eftir id:  Í þessu tilviki þáttaröðina Beauty & the Beast sem hefur id = 155. 

Hér er dæmi um leit á TVMaze API.<br>
Leit að þætti eftir nafni, ekki nákvæm leit (fuzzy).  Hér er leitað eftir strengnum shark: [https://api.tvmaze.com/search/shows?q=shark](https://api.tvmaze.com/search/shows?q=shark)<br>

<details>
<summary>Dæmi um gögn - upplýsingar um eina þáttaröð:</summary>
<br>
  
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

</details>

---

### Námsmat og skil  
- Gefið er fullt fyrir hvern lið sem er fullnægjandi, hálft ef hann er að hluta til kominn og ekkert ef hann vantar.
- Skilaðu þjappaðri (zip/rar) möppu með öllum skrám (ekki venv) á Innu.
