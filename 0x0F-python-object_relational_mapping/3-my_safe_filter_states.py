#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. als protects from
MySQL injections!
"""

import sys
import MySQLdb as mdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    search_key = sys.argv[4]
    port = 3306

    db = mdb.connect(host='localhost', port=port, user=username,
                     passwd=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name like %s ORDER BY id",
                (search_key, ))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
