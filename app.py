from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

# Funzione per inizializzare il database
def init_db():
    # Connessione al database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Creare una tabella
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # Salvare (commit) le modifiche
    conn.commit()

    # Chiudere la connessione
    conn.close()

# Inizializzazione del database
init_db()


# Route per visualizzare il form
@app.route('/')
def index():
    return render_template('form.html')

# Route per gestire l'invio del form
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

############################################
# validazione dati
############################################
    if not name or not email:
        return "Please provide both name and email", 400
############################################

    # Connessione al database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Aggiungere un nuovo record nel database
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))

    # Salvare (commit) le modifiche
    conn.commit()

    # Chiudere la connessione
    conn.close()

    # return redirect('/')
    # restituzione nella dashboard dei dati inseriti 
    return redirect('/dashboard')

# Route per visualizzare la dashboard
@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return render_template('dashboard.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)