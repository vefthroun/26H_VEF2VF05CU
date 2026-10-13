# Ferlið í app.py

### 1. Innflutningur

`from flask import Flask, render_template`

**render_template()** fallið ræsir Jinja sniðmátsvélina sem fylgir Flask umhverfinu. 
Jinja skiptir {{ ... }} blokkum út fyrir samsvarandi gildi, byggt á þeim röksemdum 
sem gefnar eru í render_template() kallinu. Sérstökum HTML stöfum er sjálfkrafa 
breytt (escaped) til að koma í veg fyrir XSS árásir. 

### 2. Frumstilling forrits

**__name__** breytan er sérstök Python breyta. Hún fær gildið **"__main__"** þegar skriftan er keyrð beint. 

Þegar skriftan er flutt inn sem eining (module), fær **__name__** nafn einingarinnar. 
Flask notar þetta til að vita hvar á að leita að auðlindum eins og sniðmátum (templates) og kyrrstæðum skrám (static files).  

`app = Flask(__name__)`

### 3. @ Skreytingar og birtingarföll (View Functions)

Skreyting (_decorator_) í Python er fall sem tekur annað fall og útvíkkar virkni þess án þess að breyta því beinlínis. 

Í Flask er `@app.route()` skreyting sem segir forritinu hvaða vefslóð (URL) á að ræsa fallið okkar. Þessi skreyting tengir vefslóðina "/" (rót síðunnar) við index() fallið.

```python
@app.route('/') 
def index(): 
```

Þetta er birtingarfall (view function). Það ber ábyrgð á að búa til svar við vefbeiðni. Hér birtir það 'template1.html' sniðmátið.
```python
    return render_template("template1.html")
```
#### Þessi skreyting tengir vefslóðina "/about" við about() fallið.
```python
@app.route('/about') 
def about(): 
    # Þetta er annað birtingarfall. Það birtir 'about.html' sniðmátið.
    return render_template('about.html')
```
### 4. Aðalinngangur

Eftirfarandi kóðablokk mun aðeins keyra ef skriftan er keyrð beint t.d. með því að keyra python 1-static.py í skipanalínunni (CLI).
```python
if __name__ == '__main__': 
    app.run(debug=True, use_reloader=True)
```   
- `app.run()` ræsir innbyggðan þróunarmiðlara Flask.
- `debug=True` kveikir á villuleitarham, sem gefur hjálpleg villuboð.
- use_reloader=True`` endurræsir miðlarann sjálfkrafa þegar þú gerir breytingar á kóðanum.
- Notaðu ALDREI `debug=True` í raunverulegu vinnsluumhverfi (production).
