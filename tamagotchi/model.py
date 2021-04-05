import sqlite3
import csv #trocar por json
from sqlite3 import Error
from random import randint, choice, random

sqlite3.enable_callback_tracebacks(True):
conn = sqlite3.connect(":memory:")

c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    codigo integer,
    nome text,
    senha text,
    PRIMARY KEY (codigo)
)''')
c.execute('''
CREATE TABLE IF NOT EXISTS pets (
    codigo text,
    nome text,
    tipo text,
    tempodevida integer,
    atualizadoem real,
    humores text,
    estados text,
    acoes text,
    PRIMARY KEY (codigo),
)''')


c.executemany("INSERT INTO usuarios VALUES (?, ?,?)", usuarios)
c.executemany("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?)", pets)


conn.commit()
conn.close()