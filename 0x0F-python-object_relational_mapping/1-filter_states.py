#!/usr/bin/python3
"""A simple use of MySQLdb to display data from db

    Usage ./1-filter_states.py <mysql username> <mysql password> <db name>
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

    cur.execute("SELECT id, name FROM states WHERE name REGEXP '^N\w*'")
    data = cur.fetchall()

    for row in data:
        print(row)
