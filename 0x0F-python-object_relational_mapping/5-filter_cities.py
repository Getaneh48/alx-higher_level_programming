#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb as mdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]
    port = 3306

    db = mdb.connect(host='localhost', port=port, user=username,
                     passwd=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT c.name FROM cities as c\
                JOIN states as s ON c.state_id = s.id WHERE s.name\
                like %s ORDER BY c.id", (state_name, ))
    cities = [row[0] for row in cur.fetchall()]
    print(*cities, sep=", ")
    cur.close()
    db.close()
