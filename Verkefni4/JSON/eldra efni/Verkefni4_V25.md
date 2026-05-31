## Verkefni 4  
- 20% af heildareinkunn
- Viðfangsefni:
  - CRUD aðgerðir með JSON skrá
  - Vinna með API
  - CSS Grids uppsetning (Layout) og PicoCSS 

---

### Verkefnalýsing
 
Útfærðu vefforrit í Flask sem nýtir JSON skrá og API. Notum [The Movie Database API](https://www.themoviedb.org/) / [Getting started](https://developer.themoviedb.org/docs/getting-started) / [API reference](https://developer.themoviedb.org/reference/intro/getting-started). Nemendur þurfa að skrá sig inn á síðuna (register) og sækja um API key, [leiðbeiningar](JSON/join_TMDB/README.md). Það kostar ekkert að skrá sig (ekki setja inn persónuupplýsingar).

1. Á forsíðu (index) skal birta grunnupplýsingar um 20 random bíómyndir frá _The Movie Database API_. Birta skal nafn (original_title) og mynd (backdrop_path) bíómyndar. Svona birtir þú [mynd](https://developer.themoviedb.org/docs/image-basics)  **20%**
1. Ef valin er ein bíómynd af forsíðu er farið á undirsíðu sem birtir nánari upplýsingar um valda bíómynd. **30%**
    - nafn bíómyndar (original_title)
    - mynd 
    - textalýsing bíómyndar (overview)
    - lengd bíómyndar (runtime)
    - útgáfudagur bíómyndar (release_date), íslensk dagsetning
    - helstu leikarar (ekki allir)
    - trailer (youtube) sem spilast á sömu síðu
1. Í valmynd er hlekkur á forsíðu, Um mig og leitarreitur þar sem hægt er að leita að ákveðinni bíómynd úr TMDB gagnagrunninum. Sýnidæmi [leit í Weather API](https://www.youtube.com/watch?v=jQjjqEjZK58). **20%**
1. Hægt er að uppfæra upplýsingar (edit) í Um mig (_profile_), gögn eru skráð og sótt í JSON skrá. **20%**
1. Notaðu eigið CSS Grids fyrir uppsetningu (layout) og Pico CSS fyrir annað einsog hluti (components) sem eiga við. **10%**

<!--
1. Helstu leikarar og hlekkir á undirsíðu til að fá nánari upplýsingar
-->


#### Að sækja gögn frá API
Hlekkurinn / API endpoint [https://api.themoviedb.org/3/discover/movie?api_key=???](https://api.themoviedb.org/3/discover/movie?api_key=???) skilar upplýsingum um 20 myndir á fyrstu síðu ( page ) af 500.  Til að fá næstu 20 myndir eða myndir af síðu 2 þaftu að bæta við skilyrðinu / flagginu &page=2 fyrir aftan api_key eða [https://api.themoviedb.org/3/discover/movie?api_key=???&page=2](https://api.themoviedb.org/3/discover/movie?api_key=???&page=2) 

Hlekkurinn / API endpoint [https://api.themoviedb.org/3/movie/550?api_key=???](https://api.themoviedb.org/3/movie/550?api_key=???) skilar okkur upplýsingum um bíómynd eftir id:  Í þessu tilviki bíómyndin The Fight Club sem hefur id = 550.  Í staðinn fyrir ??? setur þú þinn API key.

Hér eru fleiri dæmi með [TMDB endpoints](JSON/tmdb_endpoints.md).<br><br>
Leikarar, leikstjórar, framleiðendur ákveðinnar myndar: https://api.themoviedb.org/3/movie/{id}/credits?api_key={þinn_lykill}<br>
Trailerar:  https://api.themoviedb.org/3/movie/{id}/videos?api_key={þinn_lykill}<br>
Leit eftir nafni: https://api.themoviedb.org/3/search/movie?api_key={þinn_lykill}&query={leitarstrengur}<br>

<details>
<summary>Dæmi um gögn</summary>
<br>
  
```python

{
  "adult": false,
  "backdrop_path": "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
  "belongs_to_collection": null,
  "budget": 63000000,
  "genres": [
    {
      "id": 18,
      "name": "Drama"
    }
  ],
  "homepage": "",
  "id": 550,
  "imdb_id": "tt0137523",
  "original_language": "en",
  "original_title": "Fight Club",
  "overview": "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
  "popularity": 0.5,
  "poster_path": null,
  "production_companies": [
    {
      "id": 508,
      "logo_path": "/7PzJdsLGlR7oW4J0J5Xcd0pHGRg.png",
      "name": "Regency Enterprises",
      "origin_country": "US"
    },
    {
      "id": 711,
      "logo_path": null,
      "name": "Fox 2000 Pictures",
      "origin_country": ""
    },
    {
      "id": 20555,
      "logo_path": null,
      "name": "Taurus Film",
      "origin_country": ""
    },
    {
      "id": 54050,
      "logo_path": null,
      "name": "Linson Films",
      "origin_country": ""
    },
    {
      "id": 54051,
      "logo_path": null,
      "name": "Atman Entertainment",
      "origin_country": ""
    },
    {
      "id": 54052,
      "logo_path": null,
      "name": "Knickerbocker Films",
      "origin_country": ""
    },
    {
      "id": 25,
      "logo_path": "/qZCc1lty5FzX30aOCVRBLzaVmcp.png",
      "name": "20th Century Fox",
      "origin_country": "US"
    }
  ],
  "production_countries": [
    {
      "iso_3166_1": "US",
      "name": "United States of America"
    }
  ],
  "release_date": "1999-10-12",
  "revenue": 100853753,
  "runtime": 139,
  "spoken_languages": [
    {
      "iso_639_1": "en",
      "name": "English"
    }
  ],
  "status": "Released",
  "tagline": "How much can you know about yourself if you've never been in a fight?",
  "title": "Fight Club",
  "video": false,
  "vote_average": 7.8,
  "vote_count": 3439
}
```

</details>

---

### Námsmat og skil  
- Gefið er fullt fyrir hvern lið sem er fullnægjandi, hálft ef hann er að hluta til kominn og ekkert ef hann vantar.
- Skilaðu þjappaðri (zip/rar) möppu með öllum skrám (ekki venv) á Innu.