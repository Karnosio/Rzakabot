import os
import random
import sqlite3


def execute_query(query: str) -> list:
    db_path = os.path.join(os.getcwd(), 'db.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return result

def add_new_string(text: str) -> bool:
    execute_query(f"INSERT INTO Strings (text) VALUES ('{text}')")
    return True


def get_caption() -> str:
    caption = random.choices(execute_query("SELECT text FROM Strings"))
    return caption[0][0]
