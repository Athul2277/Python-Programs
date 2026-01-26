
import sqlite3
import shutil
from datetime import datetime

source = "company.db"
backup = "company_backup.db"

try:
    connection = sqlite3.connect(source)
    connection.execute("PRAGMA quick_check").fetchone()
    connection.close()

    shutil.copy2(source, backup)
    print("Backup Created:", datetime.now())
except sqlite3.Error as error:
    print("Database Error:", error)
