#!/usr/bin/python3
""" Lists all cities linked to a specific state """
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database)
    cur = db.cursor()
    query = """
    SELECT DISTINCT cities.name
    FROM states
    JOIN cities ON states.id = cities.state_id
    WHERE states.name = %s
    """
    cur.execute(query, (state,))
    results = cur.fetchall()
    if results:
        print(", ".join(result[0] for result in results))
    else:
        print("")
    cur.close()
    db.close()
