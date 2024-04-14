#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb as mdb

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = mdb.connect(host="localhost", port=3306,
                     user=user, passwd=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
