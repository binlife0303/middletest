#!C:\Python311\python.exe
#-*- coding: utf-8 -*-
import codecs, sys, cgi
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
import sql as sql
from dbConfig import conn, cur

print("Content-type: text/html\n")
print('<html><head><meta charset="utf-8"><title>移除購物車</title></head><body>')

table = cgi.FieldStorage()
id = table.getvalue('id')
sql.removeMyList(id)
sql.updateMyList(id)
print("商品數量已減少!")
print("<br><a href='MyList.py'>返回購物車</a>")
print("</body></html>")