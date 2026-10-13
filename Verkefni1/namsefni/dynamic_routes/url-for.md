# url_for

Það eru nokkrar mjög mikilvægar ástæður fyrir því að **mælt er með því að nota `url_for()`** frekar en að harðkóða vefslóðirnar handvirkt:

1.  **Auðveldara að breyta slóðum í framtíðinni (Maintainability):**
    Ef þú ákveður síðar að breyta vefslóðinni í Python kóðanum þínum (t.d. breyta `@app.route('/pizzaval/<int:id>')` yfir í `@app.route('/pizzur/<int:id>')`), þá þarftu **aðeins að breyta því á einum stað** (í `app.py`). Flask og Jinja2 munu sjálfkrafa uppfæra og búa til réttu slóðina alls staðar þar sem `url_for('pizza', ...)` er notað. Ef þú harðkóðar slóðirnar þarftu að finna og breyta þeim handvirkt í öllum þínum HTML skrám.
2.  **Örugg sjálfvirk breyting sérstafa (URL Escaping):**
    `url_for()` sér sjálfkrafa og gagnsætt um að **kóða sérstafi og óleyfileg tákn** í vefslóðum á öruggan hátt (t.d. ef gildið inniheldur bil eða íslenska stafi) svo vafrinn skilji slóðina rétt.
3.  **Kemur í veg fyrir villur með afstæðar slóðir (Absolute Paths):**
    Slóðirnar sem `url_for()` býr til eru alltaf **algildar (absolute)**. Harðkóðaðar slóðir eins og `pizzaval/...` eru oft afstæðar (relative) og geta auðveldlega brotnað ef notandinn er staddur á undirsíðu (t.d. ef hann er á `/matseðill/pizzur` og smellir á slíkan hlekk, gæti vafrinn reynt að opna `/matseðill/pizzur/pizzaval/...` í stað `/pizzaval/...`).
4.  **Sjálfvirk meðhöndlun á rót forritsins (Application Root):**
    Ef vefforritið þitt er keyrt á vefþjóni undir undirmöppu (t.d. `www.vefsida.is/mitt-app/` í stað þess að vera beint á rótinni `www.vefsida.is/`), þá sér `url_for()` um að bæta réttu forskeyti við allar slóðir sjálfkrafa. Harðkóðaða slóðin myndi reyna að leita beint á rótinni og skila 404 villu.
5.  **Skýrari og lýsandi kóði:**
    Að vísa í **nafn á falli (view function)** í Python kóðanum þínum (`pizza`) er oft lýsandi og mun skýrara en að harðkóða slóðina handvirkt inn í sniðmátið.

---

### 1. Bakendinn: Breytileg rás í Flask (`app.py`)
Í Flask notarðu hornklofa `<variable_name>` til að segja til um að hluti vefslóðarinnar sé breytilegur. Þar sem auðkenni (ID) á að vera heiltala er best að tilgreina gagnatýpuna með `<int:id>`. 

Python fallið verður að heita **`pizza`** (þar sem `url_for` vísar í nafn fallsins en ekki slóðina) og taka á móti breytunni **`id`** sem færibreytu:

```python
# Breytileg slóð sem tekur við heiltölu
@app.route('/pizzur/<int:id>') 
def pizza(id): # Fallið heitir 'pizza' og tekur við 'id'
    # Hér geturðu notað id-ið til að sækja réttu gögnin úr gagnagrunni eða orðasafni
    # dæmi: pizza_gogn = pizzas_table.get(doc_id=id)
    
    return render_template('pizza_detail.html', pizza_id=id)
```

### 2. Framendinn: Jinja2 sniðmátið þitt
Í HTML skjalinu notarðu svo `url_for()` til að búa til slóðina. Fyrsta röksemdin er nafn fallsins í Python (`'pizza'`), og við sendum `id` gildið sem viðbótarbreytu sem Flask notar til að fylla í breytilega hlutann í slóðinni:

```html
{# Við ítrum í gegnum lista af pizzum úr Python #}
{% for pizza in pizzulisti %}
    <div>
        <h3>{{ pizza.nafn }}</h3>
        <!-- url_for býr sjálfkrafa til slóðina /pizzur/1, /pizzur/2 o.s.frv. -->
        <a href="{{ url_for('pizza', id=pizza['id']) }}">Skoða nánar</a>
    </div>
{% endfor %}
```

### Af hverju passar þetta svona vel saman?
*   **Sveigjanleiki:** Ef þú ákveður síðar að breyta slóðinni í `@app.route('/pizzur/<int:id>')` yfir í `@app.route('/matseðill/pizza/<int:id>')`, þá breytirðu því bara í Python. Flask uppfærir sjálfkrafa alla hlekki á síðunni þinni þar sem `url_for('pizza', ...)` er notað.
*   **Samræmi á breytum:** Lykillinn `id` í `url_for(..., id=...)` verður að vera nákvæmlega sá sami og breytan í slóðinni `<int:id>` og í skilgreiningu Python fallsins `def pizza(id)` 🍕.

