#!/usr/bin/python3
"""A simple use of MySQLdb to display data from db
"""
import MySQLdb
import sys

if __name__ == "__main__":
    params = sys.argv
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=params[1],
        passwd=params[2],
        db=params[3]
    )
    cur = db.cursor()

    cur.execute("""
                SELECT cities.id, cities.name, states.name FROM states
                INNER JOIN cities ON states.id = cities.state_id """)
    data = cur.fetchall()

    for row in data:
        print(row)
