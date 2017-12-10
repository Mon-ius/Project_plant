#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import psycopg2
import sys
 
 
con = None
 
try:
    con = psycopg2.connect("host='localhost' dbname='testdb' user='pythonspot' password='password'")   
    cur = con.cursor()
    cur.execute("SELECT * FROM Products")
 
    while True:
        row = cur.fetchone()
 
        if row == None:
            break
 
        print("Product: " + row[1] + "\t\tPrice: " + str(row[2]))
 
except psycopg2.DatabaseError, e:
    if con:
        con.rollback()
 
    print 'Error %s' % e    
    sys.exit(1)
 
finally:   
    if con:
        con.close()