## Verkefni 4  
- 20% af heildareinkunn
- Viðfangsefni:
  - CRUD aðgerðir með JSON skrá
  - Vinna með API
  - CSS Grids uppsetning (Layout) og PicoCSS 

---

### Verkefnalýsing
 
Útfærðu vefforrit í Flask sem nýtir JSON skrá og API. Notum [Open Trivia Database](https://opentdb.com) / [Trivia API](https://opentdb.com/api_config.php).  Þetta er opin API, hér þarf ekki að skrá sig inn / ekki að sækja svokallað api_key.

Verkefnið gengur út að að útfæra vefforrit sem birtir spurningar, sem fengnar eru í gegnum API [Open Trivia Database](https://opentdb.com), og gefur notanda valkosti um svör (True/False eða Valmöguleikar).  Kerfið heldur utan um rétt / röng svör notanda og tekur saman fjölda réttra svara í lokin.  Aðeins innskráðir notendur geta notað kerfið.  Admin notandi (user:dummy@mail.com, password:123456) býr til almenna notendur (sjá hér að neðan) og getur breytt og eytt þessum upplýsingum sem vistaðar eru í JSON skrá.

1. Á forsíðu (index) skal birta almennar upplýsingar um vefsíðuna / vefkerfið og leiðbeiningar um hvernig skuli nota vefsíðuna.  Þessar upplýsingar eiga að koma úr gagnagrind í app.py skrá **5%**
1. Valmynd skal innihalda hlekki á forsíðu og innskráningu.  Ef almennur notandi er innskráður skal birta útskráningar hlekk, Ef admin notandi er innskráður skal birta admin hlekk og útskráningar hlekk **5%**
1. Admin notandi innskráður:
    - HTML tafla birtir lista allra almennra notenda **5%**
    - Admin getur breytt upplýsingum um valin notanda **15%**
    - Admin getur eytt notanda **10%**
    - Admin getur bætt við nýjum notanda **10%**
    - Upplýsingar vistaðar í JSON skrá **10%**
    - Upplýsingar sem geymdar eru um almennan notanda eru:
      - notendanafn
      - lykilorð
      - email
1. Almennur notandi innskráður:
    - Notandi velur **5%**
      - Fjölda spurninga
      - Flokk spurninga
      - Erfiðleikastig
      - Hvernig svarmöguleikar (True/False eða Valmöguleikar)
    - Kerfi sækir upplýsingar á [Open Trivia Database](https://opentdb.com) eftir forsendum hér að ofan  **5%**
    - Notandi fær spurningar og svarar **15%**
    - Þegar búið er að svara síðustu spurningu kemur yfirlitssíða um árangur **10%**
1. Notaðu eigið CSS Grids fyrir uppsetningu (layout) og Pico CSS fyrir annað einsog hluti (components) sem eiga við. **5%**


#### Að sækja gögn frá API
Hlekkurinn / API endpoint [https://opentdb.com/api.php?amount=3&category=21&difficulty=easy&type=multiple](https://opentdb.com/api.php?amount=3&category=21&difficulty=easy&type=multiple) Skilar 3 spurningum (amount=3) og fjölvalssvörum (type=multiple) við auðveldum (difficulty=easy) íþróttaspurningum (category=21).

Hlekkurinn / API endpoint [https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=boolean](https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=boolean) Skilar 10 spurningum (amount=10) og Satt/Ósatt (type=boolean) við auðveldum (difficulty=easy) tölvuleikjaspurningum (category=15).

Hér er hægt að búa til fleiri API endpoint [Trivia API](https://opentdb.com/api_config.php).

<details>
<summary>Dæmi um gögn:</summary>
<br>
  
```python

{
  "response_code": 0,
  "results": [
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Sports",
      "question": "Who won the UEFA Champions League in 2017?",
      "correct_answer": "Real Madrid C.F.",
      "incorrect_answers": [
        "Atletico Madrid",
        "AS Monaco FC",
        "Juventus F.C."
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Sports",
      "question": "What team did England beat to win in the 1966 World Cup final?",
      "correct_answer": "West Germany",
      "incorrect_answers": [
        "Soviet Union",
        "Portugal",
        "Brazil"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Sports",
      "question": "Which country hosted the 2020 Summer Olympics?",
      "correct_answer": "Japan",
      "incorrect_answers": [
        "China",
        "Australia",
        "Germany"
      ]
    }
  ]
}
```

</details>

<details>
<summary>Flokkar ( kóði bak við flokk ) :</summary>
<br>
Any = sleppum að setja inn parametra nema fjölda spurninga ( amount )<br>
General Knowlege = 9<br>
Books = 10<br>
Film = 11<br>
Music = 12<br>
Musical & Theatres = 13<br>
Television = 14<br>
Videogames  = 15<br>
Boardgames = 16<br>
Science & Nature = 17<br>
Science:Computers = 18<br>
Science:Mathematics = 19<br>
Mythology = 20<br>
Sports = 21<br>
Geography = 22<br>
History = 23<br>
Politics = 24<br>
Art = 25<br>
Celebrities = 26<br>
Animals = 27<br>
Vehicles = 28<br>
Comics = 29<br>
Gadgets = 30<br>
Japanese Anime & Manga = 31<br>
Cartoon & Animation = 32<br>
</details>
---

### Námsmat og skil  
- Gefið er fullt fyrir hvern lið sem er fullnægjandi, hálft ef hann er að hluta til kominn og ekkert ef hann vantar.
- Skilaðu þjappaðri (zip/rar) möppu með öllum skrám (ekki venv) á Innu.
