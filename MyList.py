#!C:\Python311\python.exe
#-*- coding: utf-8 -*-
import codecs, sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
import sql as sql
from dbConfig import conn, cur

print("Content-type: text/html\n")
print('<html><head><meta charset="utf-8"><title>新商品上架</title></head><body>')

MyList = sql.getMyList()
for (id, name, price, quantity) in MyList:
    print(f"<p>ID:{id} 名稱:{name} 價格:{price} 數量:{quantity}</p>")

print("<a href='Home.py'>返回賣場</a>")
print("<br><a href='Pay.py'>結帳</a>")
print("</body></html>")