#!/usr/bin/env python

"""To query the yum database and fetch the last time when a yum update all was run"""
__author__      =       "Sreeraj M S"
__email__       =       "sreewave@gmail.com"
__version__     =       "1.0"

import os
import datetime
import sqlite3

dbdir= "/var/lib/yum/history"
for yumDBfile in os.listdir(dbdir):
        if yumDBfile.endswith(".sqlite"):
             DBfile = os.path.join(dbdir,yumDBfile)

conn = sqlite3.connect(DBfile)
cur = conn.cursor()
cur.execute("select timestamp from trans_beg where tid=(select tid from trans_cmdline where cmdline='update -y' OR cmdline='update' OR cmdline='update all' order by tid desc limit 1)")
patchtime = cur.fetchall()
print datetime.datetime.fromtimestamp(patchtime[0][0]).strftime('%c')
 
