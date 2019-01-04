#!/usr/bin/python3
"""
script that lists all states from database 'hbtn_0e_0_usa'
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
    JOIN states ON cities.state_id = states.id\
    WHERE states.name = %s ORDER BY cities.id",
                (sys.argv[4],))
    rows = cur.fetchall()
    retval = ""
    for row in range(len(rows)):
        if row != len(rows) - 1:
            retval += rows[row][0] + ", "
        else:
            retval += rows[row][0]
    print(retval)
    cur.close()
    db.close()
