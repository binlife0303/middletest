#!C:\Python311\python.exe
#-*- coding: utf-8 -*-
import codecs, sys, cgi
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
import sql as sql
from dbConfig import conn, cur

print("Content-type: text/html\n")
print('<html><head><meta charset="utf-8"><title>將商品加入購物車</title></head><body>')

table = cgi.FieldStorage()
id = table.getvalue('id')
quantity = table.getvalue('數量')
sql.addMyList(id, quantity)
print("商品已存入購物車")
print("<br><a href='MyList.py'>回購物車</a>")
print("</body></html>")
