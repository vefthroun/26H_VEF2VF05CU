# How to build a Virtual Environment

1. install Python -> hakið við `PATH`
   * ![install python](install-python-1.jpg)

Við notum **CLI** (_Command Line Interface_) forrit til að búa til vefþróunarsvæði, nánari upplýsingar um aðgerðir sem hægt er að framkvæma í CLI eru hér:

- [**Windows Command Promt**](https://serverspace.io/support/help/windows-cmd-commands-cheat-sheet/)
- [**Linux Terminal**](https://linux-commands.labex.io/)
- [**Mackintosh Terminal**](https://www.geeksforgeeks.org/linux-unix/complete-mac-terminal-commands-cheat-sheet/)
- [**Unix** og þróun stýrikerfa (_í stuttu máli_)](https://medium.com/@rajamanii/the-story-of-unix-posix-linux-macos-and-windows-f8252c091be0)


Veljið vinnusvæði (möppu) í _Terminal_ (Mac-Linux) eða _Command Prompt_ (PC) þar sem verkefni áfangans VEFÞ2VF verða unnin.

CLI dæmi ` cd ~/Desktop/ ` - ` mkdir VEFÞ2VF ` -` cd ~/Desktop/VEFÞ2VF/ `

## How to Install Flask on Linux, Windows, and macOS

- Step 1: Install Virtual Environment. 
  * PC Command Prompt: `python -m venv venv` 
  * Mac/Linux: `python3 -m venv venv`
- Step 2: Create an Environment. `cd venv\Scripts\`
- Step 3: Activate the Environment. `activate`
  * ![activate venv](activate-venv.jpg)
- Step 4: Í Visual Studio Code - bætið Python í Extension
  * Neðst í hægra horni forritsins á að sjást `Python 3.xx.x (venv)` <small>(x = útgáfan sem þú ert með á tölvunni þinni)</small>
  * ![VCS ok](vsc-venv-ok.jpg)
- Step 5: In VSC, Python teminal, install Flask. `pip install Flask`
  * ![pip install](pip-install-Flask.jpg)
  * í Terminal er hægt að sjá hvort Flask pakkinn ('_module_') sé kominn í venv möppuna <br>
  !['treminal'](piplist.jpg)

### Test the Development Environment

- Step 6: Setjið eftirfarandi kóða í py skjal

```python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Halló, Python - Flask er á porti 5000!</h1>"

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  

```
- Step 7: Keyrið python skjalið (_run python file_)
  - ![Flask run](runFlaskrun.jpg)
- Step 8: Hægri smellið á 'http://127.0.0.1:5000' í _terminal_ og opnið vafra
  - ![Halló Flask](halloFlask.jpg)
