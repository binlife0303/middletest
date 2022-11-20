#!C:\Python311\python.exe
#-*- coding: utf-8 -*-
import codecs, sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
import sql as sq
from dbConfig import conn, cur

print("Content-type: text/html\n")
print('<html><head><meta charset="utf-8"><title>新商品上架</title></head><body>')


shopList = sq.getShopList()
for (id, name, price, stock) in shopList:
    print(f"<p>ID:{id} 名稱:{name} 價格:{price} 庫存:{stock}</p>")

print("<a href='MyList2.html'>加至購物車</a>")
print("<p><a href='MyList.py'>查看購物車</a></p>")
print("<p><a href='addStock.html'>商品增加存貨</a></p>")#未完成
print("<p><a href='InsertGood.html'>上架新商品</a></p>")
print("<p><a href='DeleteGood.html'>下架商品</a></p>")

print("</body></html>")