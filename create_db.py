import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('''
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)
''')
conn.commit()
conn.close()
print("Banco de dados criado com sucesso!")