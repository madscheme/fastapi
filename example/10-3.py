import sqlite3
import os

db_name = os.environ.get("CRYPTID_SQLITE_DB", "cryptid.db")
conn = sqlite3.connect(db_name)
curs = conn.cursor()
