#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database)
    cur = db.cursor()
    query = """
    SELECT * FROM states
    WHERE name LIKE BINARY 'N%'
    ORDER BY states.id ASC"""
    cur.execute(query)
    values = cur.fetchall()
    for value in values:
        print(value)

    cur.close()
    db.close()
