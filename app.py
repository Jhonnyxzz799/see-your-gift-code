from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/loja')
def loja():
    db = get_db()
    produtos = db.execute('SELECT * FROM produtos').fetchall()
    return render_template('loja.html', produtos=produtos)

@app.route('/comprar/<int:id>')
def comprar(id):
    db = get_db()
    produto = db.execute('SELECT * FROM produtos WHERE id = ?', (id,)).fetchone()
    return render_template('comprar.html', produto=produto)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    db = get_db()
    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])
        db.execute('INSERT INTO produtos (nome, preco) VALUES (?, ?)', (nome, preco))
        db.commit()
        return redirect('/admin')
    produtos = db.execute('SELECT * FROM produtos').fetchall()
    return render_template('admin.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)