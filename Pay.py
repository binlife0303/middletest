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
Shop = sql.getShopList()
quantity = table.getvalue('quantity')
stock = table.getvalue('stock')


#for(id,name,price,quantity) in MyList:#2
#    if(sql.checkS(id)>=sql.checkQ(id)):
#        total += price*quantity
#        sql.ship(id, quantity)
#if (total == 0):
#    print("有商品之存貨不足!")
#else:
    #print(f"<p>總價：{total}</p>")
for(id,name,price,quantity) in MyList:#2
    total += price*quantity
Q=sql.checkQ(1)    
print(Q)
print(f"<p>總價：{total}</p>")
print("<a href='MyList.py'>回購物車</a>")
print("<a href='Home.py'>回賣場</a>")
print("</body></html>")