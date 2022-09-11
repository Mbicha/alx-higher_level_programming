#!/usr/bin/python3
"""
This script takes an argument and display all values of in the
states table matching the name argument passed
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    name_value = argv[4]
    sql = (
        "SELECT * FROM states WHERE name=%s ORDER BY id ASC".format(name_value)
    )
    cur = conn.cursor()
    cur.execute(sql, (name_value,))
    print(cur.fetchone())
    cur.close()
    conn.close()
