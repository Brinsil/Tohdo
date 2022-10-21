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




