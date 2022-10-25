# Database for todo list

import sqlite3
from typing import List
from datetime import datetime

from tohdo_model import Tohdo

conn = sqlite3.connect('tohdo.db')
c = conn.cursor()


c.execute("""
    CREATE TABLE IF NOT EXISTS tohdo (
        Id Integer,
        Task Text,
        Section Text,
        Created_On Text,
        Due_On Text,
        Status Text
    )
""")

def insert_tohdo(tohdo: Tohdo):
    c.execute('SELECT COUNT(*) FROM tohdo')
    id = c.fetchone()[0]
    tohdo.id = id if id else 0
    with conn:
        c.execute('INSERT INTO tohdo VALUES (:id, :task, :section, :date_added, :date_completed, :status)',
                  {'task': tohdo.task, 'section': tohdo.section, 'date_added': tohdo.date_added,
                   'date_completed': tohdo.date_completed, 'status': tohdo.status, 'id': tohdo.id })

def get_tohdo(position: int) -> Tohdo:
    c.execute('SELECT * FROM tohdo WHERE Id = :position', {'position' : position})
    task = c.fetchall()[0]
    return Tohdo(*task)

def get_all_tohdos() -> List[Tohdo]:
    tohdos = []
    with conn:
        c.execute('SELECT * FROM tohdo')
        results = c.fetchall()
        for result in results:
            result = Tohdo(*result)
            tohdos.append(result)
    return tohdos

def update(id: int, column: str, value: str) -> None:
    with conn:
        c.execute(f'UPDATE tohdo SET {column} = :value WHERE Id = :id', {'column' : column, 'value' : value, 'id' : id})







