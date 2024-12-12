import sqlite3
import os

class Database:
    def __init__(self, db_name="database.db"):
        self.db_name = os.path.join(os.path.dirname(__file__), db_name)
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS suggestions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    message_id INTEGER NOT NULL,
                    status TEXT NOT NULL DEFAULT 'under review'
                )
            """)
            conn.commit()

    def add_suggestion(self, user_id, message_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO suggestions (user_id, message_id, status)
                VALUES (?, ?, 'under review')
            """, (user_id, message_id))
            conn.commit()

    def get_last_suggestion_id(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(id) FROM suggestions")
            result = cursor.fetchone()
            return result[0] if result[0] else 0

    def get_suggestion(self, suggestion_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM suggestions WHERE id = ?", (suggestion_id,))
            return cursor.fetchone()

    def update_status(self, suggestion_id, new_status):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE suggestions
                SET status = ?
                WHERE id = ?
            """, (new_status, suggestion_id))
            conn.commit()

    def get_all_suggestions(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM suggestions")
            return cursor.fetchall()