
import sqlite3
import time

connection = sqlite3.connect("company.db")
query = "SELECT * FROM employees WHERE department = ?"
start = time.perf_counter()
results = connection.execute(query, ("Engineering",)).fetchall()
duration = time.perf_counter() - start
print("Records retrieved:", len(results))
print("Query execution time:", round(duration, 6), "seconds")
connection.close()
