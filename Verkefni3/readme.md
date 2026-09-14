## Verkefni 3  

- 20% af heildareinkunn
- Viðfangsefni:
  - API, beiðnir (_requests_) frá [TVmaze API](https://api.tvmaze.com)
  - CRUD aðgerðir með JSON / [TinyDB](https://tinydb.readthedocs.io/en/latest/getting-started.html)
  - Jinja2: Template inheritance, extend layout
  - HTML Form
 
#### JSON API 10%

Í verkefni 3 lærir þú að nýta vefþjónustur (REST APIs) í Flask. Þú munt framkvæma fyrirspurnir gegnum netið, sækja gögn á JSON-sniði, vinna úr þeim í bakenda með Python og birta niðurstöðurnar (t.d. þáttalista, myndir og leitarútkomur) í HTML sniðmátum

* **API / REST**: Samskipti við ytri miðlara gegnum HTTP fyrirspurnir.
* **JSON gögn**: Meðhöndlun á lista- og orðasafnsuppbyggingu (dicts) í Python.
* **Gagnvirk birting**: Birting á gögnum og myndum með Jinja2 sniðmátum og `| safe` síum

#### Útfærðu vefforrit í Flask sem birtir gögn frá [TVmaze API](https://api.tvmaze.com). 

1. Á forsíðu (index) skal birta grunnupplýsingar um 20 random þætti ur _Epguides API_ gagnagrunninum. Birta skal nafn og mynd þáttaraða  **2%**
1. Þegar valin er ein þáttaröð af forsíðu er farið á síðu sem birtir nánari upplýsingar um valda þáttaröð. **3%**
    - nafn þáttaraðar (name)
    - mynd (image/medium)
    - textalýsing þáttaraðar (summary)
    - lengd þáttaraðar (runtime)
    - útgáfudagur þáttaraðar (premiered), íslensk dagsetning
    - dagsetning síðasta þáttar (ended)
    - flokkar þáttaraðar (genres)
1. Í valmynd er hlekkur á forsíðu, alla flokka (má vera í fellivalslista - select field), leitarreitur þar sem hægt er að leita að ákveðinni þáttaröð úr Epguides gagnagrunninum.  **1%**
1. Þegar valin er einn flokkur (genre) úr valmynd birtir kerfið vefsíðu með þáttaröðum sem tilheyra völdum flokki. Sömu upplýsingar og á forsíðu nafn og mynd **2%**
1. Þegar leitað er að þáttaröð er nafn slegið inn í leitarreit og ýtt á hnapp / takka.  Þá fer kerfið á vefsíðu sem birtir helstu upplýsingar um þáttaraðir sem tilheyra nafninu í leitarstregnum ( helstu upplýsingar nafn og mynd ).**2%**

> Notaðu PicoCSS fyrir uppsetningu (_layout_) og Jinja erfðir (_Jinja2: inheritance_)

### Námsefni

- [JSON málskipan](namsefni/README.md)
- [JSON & Python CRUD dæmi](namsefni/pyCrudExamples/README.md)
- [TVmaze API](namsefni/TVmaze/README.md)
- <details>
  <summary>hvað er REST API?</summary>
  <strong>REST API</strong> er útskýrt sem vefþjónusta sem gerir forritum kleift að skiptast á gögnum yfir netið með því að nota staðlaðar HTTP fyrirspurnir og vefslóðir (endpoints).
  <ul>
    </li><li>REST API notar aðgengilegar vefslóðir til að tilgreina hvaða gögn eða úrræði á að sækja, t.d. `/shows/155` til að sækja ákveðinn þátt eða `/search/shows?q=shark` til að leita. 
    </li><li>Samskiptin nota staðlaðar HTTP aðferðir (eins og GET eða POST).
    </li><li> <b>Gagnasnið (JSON)</b>: Svör frá REST API eru oftast send á <b>JSON</b> sniði, sem er létt, skýrt og auðvelt að breyta í Python orðasöfn (dicts) eða lista í bakenda.
    </li><li><b>HTTP</b> Stöðukóðar <i>(Status Codes)</i>: Miðlarinn skilar svörum ásamt stöðukóða sem gefur til kynna hvernig beiðnin gekk, svo sem <b>200 OK</b> (aðgerð tókst), <b>301</b> (tilvísun), <b>404 Not Found</b> (úrræði fannst ekki) eða <b>429 Too Many Requests</b> (farið yfir leyfileg hraðatakmörk).
    </li><li> <b>Færibreytur og samþætting (Embedding)</b>: Hægt er að senda síur eða breytur með vefslóðinni (t.d. `?q=query` eða `?page=1`). 
      Einnig styðja REST API þjónustur (eins og TVMaze með HAL/HATEOAS staðlinum) að innfella tengd gögn í einu kalli með færibreytum eins og `?embed=episodes`.
    </li><li> <b>Öryggi og aðgengi</b>: REST API þjónustur nýta <b>HTTPS</b> fyrir örugg samskipti og eru oft með <b>CORS</b> (Cross-Origin Resource Sharing) virkjað svo hægt sé að kalla í þær beint úr vefforritum.
    </li>
  </ul>
  </details>

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

#### JSON Tinydb 10%

Hér lærir þú að vinna með form, gögn notenda og varanlega gagnageymslu. Þú munt búa til vefforrit sem tekur við inntaki gegnum HTML form, vinnur úr gögnunum í bakenda og framkvæmir CRUD-aðgerðir í TinyDB skráargagnagrunni.

* **HTML Form &amp; Formvinnsla**: Viðtaka og úrvinnsla inntaks frá notanda gegnum `request.form`.
* **CRUD-aðgerðir**: Nýskráning, uppfletting, uppfærsla og eyðing gagna (*Create, Read, Update, Delete*).
* **TinyDB**: Varanleg skráargagnageymsla á JSON-sniði (`db.json`).

1. Notaðu uppsetninguna sem þú hannaðir í 2. verkefni, taktu út orðasöfnin (_dictonaries_) úr appinu og settu innihaldið í JSON skrá.
1. Notaðu TinyDB pakkann til að framkvæma CRUD aðgerðir 
   * Allar færslur og breytingar eru vistaðar í JSON skránni
1. Á forsíðu birtast allir póstar úr json skránni
1. Nýskráning býr til nýjan notanda
1. Notandi getur síðan skráð sig inn á eigin **prófíl**
1. Notendur geta skrifað nýja pósta, breytt eigin póstum eða eytt þeim
1. Prófílsíðan er varin með **session** aðgangsvörn
1. Vefstjóri (admin) getur eytt póstum og notendum 

### Námsefni

- [Tinydb gagnagrunnur](namsefni/Tinydb/README.md)

---

### Námsmat 

Sundurliðun námsmats er í verkefni 3 **í Canvas**

### Verkefnaskil

Skilaðu möppu með öllum skrám verkefnisins í **.zip skrá**  í Canvas (**ath!** ekki skila **venv** möppu).
