#!C:\Python311\python.exe
#-*- coding: utf-8 -*-
import codecs, sys,cgi
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
import sql as sql
from dbConfig import conn, cur

print("Content-type: text/html\n")
print('<html><head><meta charset="utf-8"><title>結帳</title></head><body>')

table = cgi.FieldStorage()
total = 0
MyList = sql.getMyList()
quantity = table.getvalue('quantity')
stock = table.getvalue('stock')
stockLast = stock - quantity

for(id, name, price, quantity) in MyList:
    total += price*quantity
print(f"<p>總價：{total}</p>")
print("<a href='MyList.py'>回購物車</a>")
print("</body></html>")