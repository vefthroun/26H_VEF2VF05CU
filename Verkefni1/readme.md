## Verkefni 1 

- 15% af heildareinkunn
- Viðfangsefni: 
   1. [Uppsetning á vinnuumverfi ( templates og static möppur ) / VENV](namsefni/how-to-build-venv)
   1. Python gagnagrindur ( list og dict )
   1. Static / Dynamic Routing
   1. Static files: CSS og myndir
   1. Jinja2: templates, include,  if-statement og for-loop
   1. url_for
   1. 404 Error route

---

### Verkefnalýsing 

Útfærðu vef sem sýnir hvenær jólasveinarnir koma til byggða, vefurinn er byggður upp með Flask. Notaðu lista með dictionaries sem gagnagrind (datastructure).  

* Hér fyrir neðan er gagnagrind (jolahyski) sem þú getur notað.  
* Hér eru [myndir af jólaveinunum](vinnugogn/) í **.zip** skrá sem þú getur notað.

1. Í **layout.html** er vefurinn er hlutaður niður í Jinja; **10%**
   1. include **nav** (valmynd)
   1. include**footer** (höfundur verkefnis og myndefnis). 
   1. Innihald vefsins kemur með færibreytu í **&lt;main>**
1. **Valmynd (nav)** inniheldur hlekk á forsíðu og **4** hlekki sem eru 'flokkur' úr gagnagrind **Þjófar / Betlarar / Perrar / Mannætur**.  Notaðu [url_for](namsefni/urlfor.py) fyrir hlekkina  **10%**
1. **Forsíðan** birtir myndirnar af jólahyskinu  þar sem kemur fram nafn Jólasveins,  komudagur og mynd. Notandi þarf að geta valið einn af þeim til að fá nánari upplýsingar um hann (næsti liður).  Notaðu [url_for](namsefni/urlfor.py) til að birta myndir  **20%**
1. Síða um jólasvein ( undirsíða ) inniheldur; nafn, persónulýsingu, hegðun, flokk og mynd. **25%**
1. Flokkur (undirsíða). Ef notandi velur t.d. hlekkinn **Þjófar** úr valmynd þá birtist vefsíða einungis með jólasveinum úr þeim flokki. **25%**
1. Settu upp 404 error route og viðeigandi html vefsíðu sem er birt ef upp kemur 404 villa **5%** 
1. Notaðu [Pico css](https://picocss.com/) safnið fyrir uppsetningu og framsetningu á vef, eigið safn eða hvað sem þú vilt nota. **5%**

> Engin harðkóðun!

#### Skráarskipulag
- Templateskrár sem í grunninn byggir á HTML geymast í möppu sem nefnist `templates`.
- Stílsíður (CSS), myndir, JavaScript og önnur `binary` skjöl fara í möppu sem nefnist `static`.
- Gögn eru ýmist vistuð í lista, dictionary, skrám eða gagnagrunna. Innihald (gögn) eiga aldrei að vera skrifuð beint í html!

#### Gagnagrind

```python
# Dæmi um lista [] með {} söfnum (dictionaries) .

jolahyski =  [
    {
        "id": 1,
        "nafn": "Stekkjarstaur",
        "personulysing": "Haltrar og er stífur í knjánum vegna staurfóta. Sækir í fjárhúsin til að reyna að sjúga mjólk úr ánum.",
        "komudagur": "12. desember",
        "hegðun": "Perrar",
        "mynd": "mynd-1.jpg"
    },
    {
        "id": 2,
        "nafn": "Giljagaur",
        "personulysing": "Felur sig í giljum og laumast í fjósin til að fleyta froðuna ofan af mjólkurfötunum.",
        "komudagur": "13. desember",
        "hegðun": "Þjófar",
        "mynd": "mynd-2.jpg"
    },
    {
        "id": 3,
        "nafn": "Stúfur",
        "personulysing": "Einkar lágvaxinn og stuttur. Stalst í eldhúsin til að skafa og borða matarleifar af pönnunum.",
        "komudagur": "14. desember",
        "hegðun": "Þjófar",
        "mynd": "mynd-3.jpg"
    },
    {
        "id": 4,
        "nafn": "Þvörusleikir",
        "personulysing": "Langur og mjór, stelst til að sleikja þvörurnar í von um að finna bragðgott skaf.",
        "komudagur": "15. desember",
        "hegðun": "Þjófar",
        "mynd": "mynd-4.jpg"
    },
    {
        "id": 5,
        "nafn": "Pottaskefill",
        "personulysing": "Skafar og borðar leifar og skófir innan úr pottunum sem ekki hafði verið búið að þrífa.",
        "komudagur": "16. desember",
        "hegðun": "Þjófar",
        "mynd": "mynd-5.jpg"
    },
    {
        "id": 6,
        "nafn": "Askasleikir",
        "personulysing": "Felur sig undir rúmum og þreif askana þegar þeir voru settir á gólfið til að sleikja þá að innan.",
        "komudagur": "17. desember",
        "hegðun": "Betlarar",
        "mynd": "mynd-6.jpg"
    },
    {
        "id": 7,
        "nafn": "Hurðaskellir",
        "personulysing": "Hávaðasamur og stríðinn, skellir hurðum harkalega á nóttunni til að vekja og trufla fólk.",
        "komudagur": "18. desember",
        "hegðun": "Perrar",
        "mynd": "mynd-7.jpg"
    },
    {
        "id": 8,
        "nafn": "Skyrgámur",
        "personulysing": "Mikill matgæðingur sem brýst inn í búrin og gámar í sig skyr úr skyrkerunum.",
        "komudagur": "19. desember",
        "hegðun": "Þjófar",
        "mynd": "mynd-8.jpg"
    },
    {
        "id": 9,
        "nafn": "Bjúgnakrækir",
        "personulysing": "Klifrar upp í rjáfr og sperrur í eldhúsum til að krækja sér í reykt bjúgu.",
        "komudagur": "20. desember",
        "hegðun": "Þjófar",
        "mynd": "mynd-9.jpg"
    },
    {
        "id": 10,
        "nafn": "Gluggagægir",
        "personulysing": "Óskaplega forvitinn og gægist inn um glugga til að leita að dót eða mat og til að gretta sig.",
        "komudagur": "21. desember",
        "hegðun": "Perrar",
        "mynd": "mynd-10.jpg"
    },
    {
        "id": 11,
        "nafn": "Gáttaþefur",
        "personulysing": "Með stórt nef og næmt lyktarskyn, snuðrar í gáttum til að finna ilminn af laufabrauði og kökum.",
        "komudagur": "22. desember",
        "hegðun": "Betlarar",
        "mynd": "mynd-11.jpg"
    },
    {
        "id": 12,
        "nafn": "Ketkrókur",
        "personulysing": "Útsjónarsamur og notar staf með krók til að krækja sér í hangikjöt upp um strompinn.",
        "komudagur": "23. desember",
        "hegðun": "Þjófar",
        "mynd": "mynd-12.jpg"
    },
    {
        "id": 13,
        "nafn": "Kertasníkir",
        "personulysing": "Eltir börnin til að sníkja eða stela tólgarkertum sem voru björt og bragðgóð.",
        "komudagur": "24. desember",
        "hegðun": "Betlarar",
        "mynd": "mynd-13.jpg"
    },
    {
        "id": 14,
        "nafn": "Grýla",
        "personulysing": "Grimm og ófrýnileg tröllskessa sem safnar óþekkum börnum í pokann sinn til að borða þau.",
        "komudagur": "um jólin, fer eftir eftirspurn",
        "hegðun": "Mannætur",
        "mynd": "mynd-14.jpg"
    },
    {
        "id": 15,
        "nafn": "Leppalúði",
        "personulysing": "Latur gamall tröllkarl, eiginmaður Grýlu og faðir jólasveinanna.",
        "komudagur": "ekki, hann nennir ekki að koma til mannabyggða",
        "hegðun": "Betlarar",
        "mynd": "mynd-15.jpg"
    },
    {
        "id": 16,
        "nafn": "Jólakötturinn",
        "personulysing": "Ógnvekjandi og stór heimilisköttur Grýlu sem etur þau börn sem fá enga nýja flík fyrir jólin.",
        "komudagur": "á jóladag",
        "hegðun": "Mannætur",
        "mynd": "mynd-16.jpg"
    }
]

```

#### Punktar

-  Notaðu `id` úr gagnagrind fyrir url í dynamic route
-  dæmi um hlekk með _**url_for**_ `<a href="{{ url_for('flokkur', hegdun='Þjófar') }}" ` á dýnamískt route  `@app.route('/flokkur/<hegdun>')`
-  Þú gætir þurft að breyta streng í heiltölu t.d. id = int("3")  # breytum "3" í 3 með int()

---

### [Námsefni](namsefni/README.md)

---

### Námsmat 

Sundurliðun námsmats er í verkefni 1 **í Canvas**

### Verkefnaskil

Skilaðu möppu með öllum skrám verkefnisins í **.zip skrá**  í Canvas 

* Athugið að skila **ekki** Python vinnuumhverfinu sem er **venv** mappan.