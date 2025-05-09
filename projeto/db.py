import sqlite3
import pandas as pd

# Conectar (ou criar) o banco de dados
conn = sqlite3.connect("web_scraping.db")
cursor = conn.cursor()

# Criar a tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    preco_antigo TEXT,
    preco_novo TEXT,
    desconto TEXT,
    link TEXT
)
""")

# Confirmar e fechar
conn.commit()

df_1 = pd.read_csv('produtos_pagina_inicial.csv')
df_2 = pd.read_csv('produtos_paginas_restantes.csv')
df_1['preco_antigo'] = df_1['preco_antigo'].astype(str)
df_1['preco_novo'] = df_1['preco_novo'].astype(str)

df_2['preco_antigo'] = df_2['preco_antigo'].astype(str)
df_2['preco_novo'] = df_2['preco_novo'].astype(str)


df_1.to_sql("produtos", conn, if_exists="append", index=False)
df_2.to_sql("produtos", conn, if_exists="append", index=False)

conn.close()
