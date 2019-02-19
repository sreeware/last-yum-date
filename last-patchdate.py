#!/usr/bin/env python

"""To query the yum database and fetch the last time when a yum update all was run"""
__author__      =       "Sreeraj M S"
__email__       =       "sreewave@gmail.com"
__version__     =       "1.0"

import os
import datetime
import sqlite3

dbdir= "/var/lib/yum/history"

# the os.listdir() function lists the files in arbitrary order. In the very rare case of yum having two sqlite DB files, the 'FilesList'
# function will list the files in the 'dbdir' by the order of its mtime and helps in picking up the latest sqlite DB file.

def filesList(path):
        mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
        return list(sorted(os.listdir(path), key=mtime))

for yumFiles in filesList(dbdir):
        if yumFiles.endswith(".sqlite"):
             DBfile = os.path.join(dbdir,yumFiles)

conn = sqlite3.connect(DBfile)
cur = conn.cursor()
cur.execute("select timestamp from trans_beg where tid=(select tid from trans_cmdline where cmdline='update -y' OR cmdline='update' OR cmdline='update all' order by tid desc limit 1)")
patchtime = cur.fetchall()
print datetime.datetime.fromtimestamp(patchtime[0][0]).strftime('%c')
 
