#!C:\Python311\python.exe
#-*- coding: utf-8 -*-
import codecs, sys, cgi
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
import sql as sql
from dbConfig import conn, cur

print("Content-type: text/html\n")
print('<html><head><meta charset="utf-8"><title>新商品上架</title></head><body>')

table = cgi.FieldStorage()
id = table.getvalue('id')
stock = table.getvalue('stock')
sql.add(id, stock)
sql.updateShopList(id)
print("商品存貨已增加!")
print("<a href='Home.py'>確認</a>")
print("</body></html>")