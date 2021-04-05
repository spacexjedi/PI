import sqlite3 as sql


username = "boss"
password = "1234"
con = sql.connect("data.db")
cur = con.cursor()
statement = f"SELECT username from users WHERE username='{username}' AND Password = '{password}';"
cur.execute(statement)
if not cur.fetchone():  # An empty result evaluates to False.
    print("Login failed")
else:
    print("Welcome")