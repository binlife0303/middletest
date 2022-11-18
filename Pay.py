#!C:\Users\tommy\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
import codecs, sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

from dbConfig import conn, cur

print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>結帳</title>
</head>
<body>
""")

total = 0
shopList = sql.getMyList()
for(id, name, price, amount) in shopList:
    total += price*amount
print(f"<p>總價：{total}</p>")
print("<a href='myCart.py'>回購物車</a>")
print("</body></html>")