## Verkefni 2 
- 10% af heildareinkunn
- Viðfangsefni: 
   1. List með Dict
   1. Dynamic routing 
   1. Jinja2: include,  if-statement og for-loop
   1. 404 Error route

---

### Verkefnalýsing 
Útfærðu lítinn vef sem heldur utan um vörulista (Pizzur) með Flask. Notaðu lista með dictionaries (vörulistinn) sem gagnagrind (datastructure).  Hér fyrir neðan er gagnagrind sem þú getur notað en þú mátt búa til þína eigin.  Hér eru [myndir](https://github.com/vefthroun/Vefforritun1/tree/main/Verkefni2/img) sem þú getur notað.

1. Vefurinn er hlutaður niður með **include** í Jinja2; nav (valmynd), footer (höfundur verkefnis) og vörulista. **10%**
1. Valmynd inniheldur hlekki á forsíðu og **3** flokka úr gagnagrind kjöt / sterk / vegan.  **10%**
1. Forsíða birtir vörulistann snyrtilega þar sem fram þarf að koma nafn vöru, verð og mynd. Notandi þarf að geta valið eina vöru til að fá nánari upplýsingar um valda vöru ( næsti liður ).  Sýndu einnig heildarfjölda vara á síðunni. **20%**
1. Vörusíða ( undirsíða ) inniheldur; nafn, verð, álegg (`<ul>`), flokk og mynd.  Notaðu `div` til að halda utan um valda vöru. **25%**
1. Flokkur (undirsíða). Ef notandi velur t.d. hlekkinn **vegan** úr valmynd þá birtist vefsíða einungis með Pizzum úr þeim flokki. **25%**
1. Settu upp 404 error route og viðeigandi html vefsíðu sem er birt ef upp kemur 404 villa **5%** 
1. Notaðu [New.css]([https://new.css/](https://new.css/)) safnið fyrir uppsetningu og framsetningu á vef, eigið safn eða hvað sem þú vilt nota. **5%**

Engin harðkóðun!

#### data

```python
# Dæmi dictionary í list.

menu =  [
        {
            "id": 0,
            "nafn": "El Peppó Xtra",
            "mynd": "pizza0.JPG",
            "verd":1600,
            "álegg":["Xtra pepperóni", "Xtra ostur", "Xtra Sósa"],
            "flokkur":"kjöt"
        },
        {
            "id": 1,
            "nafn": "El Vegó",
            "mynd": "pizza1.JPG",
            "verd":1400,
            "álegg":["Paprika", "Laukur", "Ananas"],
            "flokkur":"vegan"
        },
        {
            "id": 2,
            "nafn": "Pizza MOI",
            "mynd": "pizza2.JPG",
            "verd":2000,
            "álegg":["Banani", "Ananas", "Lárviðarlauf"],
            "flokkur":"vegan"
        },
        {
            "id": 3,
            "nafn": "El Logos",
            "mynd": "pizza3.JPG",
            "verd":1500,
            "álegg":["Spicy Pepperoni", "Chilli Pepper", "Hot Sauce", "Laukur"],
            "flokkur":"sterk"
        },
                {
            "id": 4,
            "nafn": "Pizza Domo",
            "mynd": "pizza4.JPG",
            "verd":2500,
            "álegg":["Nautahakk", "Paprika", "Laukur"],
            "flokkur":"kjöt"
        },
        {
            "id": 5,
            "nafn": "El Grande",
            "mynd": "pizza5.JPG",
            "verd":3000,
            "álegg":["Pepperoni", "Skinka", "Nautahakk", "Paprika", "Laukur"],
            "flokkur":"kjöt"
        }
    ]

```

**Punktar**
-  Notaðu `id` úr gagnagrind fyrir url í dynamic route
-  dæmi um hlekk með _**url_for**_ `<a href="{{ url_for('flokkur', fl='vegan') }}" ` á dýnamískt route  `@app.route('/flokkur/<fl>')`
-  Þú gætir þurft að breyta streng í heiltölu t.d. id = int("3")  # breytum "3" í 3 með int()

---

### Námsmat og skil 
Gefið er fullt fyrir hvern lið sem er fullnægjandi, hálft ef hann er að hluta til kominn og ekkert ef hann vantar. Skilaðu möppu með öllum skrám (ekki venv möppu) á Innu.

