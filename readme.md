# sqlLite Python project

## Requirement:
- Install Python3
- Install Virtual Environment (VENV)
    * py -3 -m venv .venv
    * .venv\Scripts\activate
- Install PIP
- Install dependencies:
    * pip install setuptools
    * $ pip install flask
    * $ pip install sqlite3

- Check if installed correctly:
    * $ pip list

- Run App
    * $ python app.py
        or alternatively: 
    * $ flask --app app run

## Explane project
Dopo il comando di esecuzione dell'App, verrà creato in automatico il file database.db. 
Se il file esiste già, verrà semplicemente aperto.

Dopo aver inviato il form, i dati vengono salvati nel file database.db.

Puoi verificare questo aprendo una console SQLite e visualizzando i dati nella tabella users.

Ogni volta che un utente invia il form, i dati vengono salvati nel file database.db.

Questo file è persistente, quindi i dati rimangono salvati anche dopo che l'applicazione Flask viene chiusa e riaperta.

Puoi continuare a utilizzare questo file per memorizzare tutti i dati inseriti dai tuoi utenti.