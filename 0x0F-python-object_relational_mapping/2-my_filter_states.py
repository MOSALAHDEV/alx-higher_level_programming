#!/usr/bin/python3
""" Lists states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database)
    cur = db.cursor()
    query = """
    SELECT * FROM states
    WHERE name = %s
    ORDER BY states.id ASC""".format(name.replace("'", "''"))
    cur.execute(query)
    results = cur.fetchall()
    for result in results:
        print(result)

    cur.close()
    db.close()
