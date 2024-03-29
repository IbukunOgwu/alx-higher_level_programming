#!/usr/bin/python3
"""This lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor_db = db.cursor()
    cursor_db.execute(
        "SELECT * FROM states\
        WHERE BINARY name = '{}'\
        ORDER BY states.id ASC".format(sys.argv[4]))
    states = cursor_db.fetchall()
    for state in states:
        print(state)
    cursor_db.close()
    db.close()
