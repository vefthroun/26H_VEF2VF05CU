
## Verkefni 3 
- 20% af heildareinkunn
- Viðfangsefni:
  1. Formvinnsla
  1. Sessions
  1. Flash Message 
  1. Jinja: inheritance

### Verkefnalýsing

Útfærðu innskráningarsíðu til að komast inná admin síðu þar sem notandi getur búið til blogfærslu sem er svo vistuð (bætt við) í gagnagrind (listi af dictionaries í .py skrá). Allar blofærslur birtast á forsíðu.

![v3.svg](https://github.com/vefthroun/Vefforritun1/blob/main/Verkefni3/v3.svg)

1. Innskráningarsíða (login) sem inniheldur: **20%**
    - HTML <!-- [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.2.x/) viðbótina til að búa til --> form með inntaksreitina; notandi (netfang) og lykilorð.
    - formprófun (validation) á inntaksreitum (email / ekki tóm).
    - Notaðu [flash message](https://flask.palletsprojects.com/en/2.2.x/patterns/flashing/) til að láta vita hvort aðgerð hafi tekist. 
1.  Notaðu [Session](https://flask.palletsprojects.com/en/3.0.x/quickstart/#sessions) fyrir aðgangsstýringar og auðkenningu (authentication). **20%**
    - Það á ekki ekki að vera hægt að fara beint inná adminsíðu nema að hafa aðgang (bara einn notandi), notaðu netfangið `admin@admin.is` og lykilorðið `1234`.
    - Útfærðu útskráningarvirkni (eyða session)
1. Adminsíða (admin) sem inniheldur: **20%**
    - nafn innskráðs notanda.
    - form til að búa til blogfærslu; titill, textainnihald með [CKEditor](https://flask-ckeditor.readthedocs.io/en/latest/basic.html) (rich-text editor), dagsetning og nafn höfundar. 
    - blogfærsla er [skrifuð](https://www.freecodecamp.org/news/everything-you-need-to-know-about-python-dictionaries/) (vistuð) í gagnagrind (listi með dictionaries) sem dictionary þegar smellt er á hnapp. 
    - notaðu formprófun (validation) og flash message til að láta vita hvort aðgerð hafi tekist og _redirect_ á forsíðuna.
1. Forsíða sem birtir nýlega búna til blogfærslu ásamt öllum hinum úr gagnagrind, raðað eftir dagsetningu, nýjasta á að vera efst. **10%**
1. Valmynd með forsíðu, login, logout og admin. Hlekkirnir admin og logout (í stað login) birtast í valmynd þegar notandi er innskráður annars ekki. **10%**
1. Notaðu [inhertiance](https://flask.palletsprojects.com/en/2.3.x/patterns/templateinheritance/) með Jinja fyrir skipulag. **10%**
1. Notaðu eigið CSS safn og / eða t.d. [Pico CSS](https://picocss.com/docs/forms) eða [NEW.CSS](https://newcss.net/) fyrir form og aðra framsetningu. **10%**

---

### Námsmat og skil 
- Gefið er fullt fyrir hvern lið sem er fullnægjandi, hálft ef hann er að hluta til kominn og ekkert ef hann vantar. 
- Skilaðu þjappaðri ( zip/rar ) möppu með öllum skrám (ekki venv) á Innu.

