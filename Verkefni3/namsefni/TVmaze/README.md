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


