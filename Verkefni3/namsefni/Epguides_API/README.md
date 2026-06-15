# Epguides API

- https://epguides-api.readthedocs.io/en/latest/

Til að bæta sjónvarpsþáttasíðu við núverandi vefuppsetningu þína þarftu að nýta **Epguides API** til að sækja gögnin og **Flask** til að birta þau í gegnum sniðmát sem erfir frá `layout.html`.

Hér er hvernig þú getur útfært þetta:

### 1. Sækja gögn úr Epguides API
Epguides API er ókeypis REST þjónusta sem krefst ekki API-lykils. Þú getur notað Python-safnið `requests` til að sækja JSON gögn um þætti. Þar sem þú vilt aðeins birta 20 þætti geturðu notað skurð (e. slicing) í Python á listann sem API-ið skilar.

**Dæmi um Flask rás (route):**
```python
import requests
from flask import render_template

@app.route('/shows')
def shows():
    # Sækjum gögn frá Epguides API (þetta er dæmi um slóð)
    response = requests.get('https://epguides.frecar.no/shows/')
    all_shows = response.json()
    
    # Veljum aðeins fyrstu 20 þættina úr listanum
    top_20_shows = all_shows[:20]
    
    return render_template('shows.html', shows=top_20_shows)
```

### 2. Hanna shows.html með erfðum
Til að síðan passi inn í vefinn þinn á hún að nota `{% extends "layout.html" %}` eins og við ræddum áður [Conversation]. API-ið gefur þér gögn eins og titil, sjónvarpsstöð (network) og myndir frá TVMaze.

**Dæmi um shows.html:**
```html
{% extends "layout.html" %}

{% block title %}20 Vinsælir Þættir{% endblock %}

{% block content %}
    <h1>Sjónvarpsþættir</h1>
    <div class="shows-container">
        {% for show in shows %}
            <div class="show-card">
                <h3>{{ show.title }}</h3>
                <p><strong>Stöð:</strong> {{ show.network }}</p>
                <p><strong>Land:</strong> {{ show.country }}</p>
                {# Ef API-ið gefur myndaslóð er hún birt hér #}
                {% if show.image %}
                    <img src="{{ show.image }}" alt="{{ show.title }}" style="width:200px;">
                {% endif %}
            </div>
        {% endfor %}
    </div>
{% endblock %}
```

### 3. Samþætting við núverandi kerfi
*   **Navigation:** Bættu hlekk á nýju síðuna í `nav` hlutann í `layout.html` með því að nota `url_for('shows')` [39, Conversation].
*   **Gagnageymsla:** Ef þú vilt vista upplýsingar um uppáhalds þættina þína gætirðu notað **TinyDB** til að geyma þá í `db.json` skrá.
*   **Öryggi:** Flask sér sjálfkrafa um að **hreinsa (escape)** öll gögn sem koma úr API-inu áður en þau eru birt í Jinja2 sniðmátinu til að verjast öryggisvandanum.

**Af hverju þessi leið?**
Með því að nota API-ið beint þarftu ekki að skrá gögnin handvirkt í gagnagrunn. Með því að nota `render_template` og Jinja2 lykkjur (`{% for ... %}`) geturðu birt mikið magn af gögnum á skipulegan hátt með lágmarks kóðun.