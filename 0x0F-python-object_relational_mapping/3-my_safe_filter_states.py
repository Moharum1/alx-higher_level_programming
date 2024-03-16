#!/usr/bin/python3
"""A simple use of MySQLdb to display data from db

Usage ./3-my_safe_filter_states.py <mysql user> <mysql password> <db> <state>
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
    state = params[4]
    cur = db.cursor()

    cur.execute("SELECT id, name FROM states")
    data = cur.fetchall()

    for row in data:
        if row[1] == state:
            print(row)
