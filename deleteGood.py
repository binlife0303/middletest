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
sql.deleteFromMyList(id)
sql.deleteFromShop(id)
sql.updateMyList(id)
sql.updateShopList(id)
print("商品已下架!")
print("<br><a href='Home.py'>確認</a>")
print("</body></html>")