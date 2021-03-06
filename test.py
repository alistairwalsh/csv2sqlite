#!/usr/bin/env python
import csv
import sqlite3

from csv2sqlite import convert

def test():
    '''Simple test case'''
    import StringIO
    import os
    fileobj = StringIO.StringIO(
'''heading_1,heading_2,heading_3
abc,1,1.0
xyz,2,2.0
efg,3,3.0'''
    )
    dbpath = '/tmp/csv2sqlite-test-data.db'
    if os.path.exists(dbpath):
        os.remove(dbpath)
    table = 'data'
    convert(fileobj, dbpath, table)
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute('select count(heading_3) from %s' % table);
    row = c.next()
    assert row[0] == 3, row

def test_semicolon():
    '''Simple test case (semicolon)'''
    import StringIO
    import os
    fileobj = StringIO.StringIO(
'''heading_1;heading_2;heading_3
abc;1;1,0
xyz;2;2,0
efg;3;3,0'''
    )
    dbpath = '/tmp/csv2sqlite-test-data.db'
    if os.path.exists(dbpath):
        os.remove(dbpath)
    table = 'data'
    convert(fileobj, dbpath, table)
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute('select count(heading_3) from %s' % table);
    row = c.next()
    assert row[0] == 3, row

if __name__ == '__main__':
       test()
       test_semicolon()
