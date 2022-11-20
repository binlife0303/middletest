from dbConfig import conn, cur
#消費者管理
#查看我的購物車
def getMyList():
    sql="select id, name, price, quantity from 我的購物車 order by id asc;"
    cur.execute(sql)
    shopList = cur.fetchall()
    return shopList
#商品加入購物車
def addMyList(id, name, price, quantity):
    sql="INSERT INTO 我的購物車(id, name, price, quantity) VALUES (%s, %s, %s, %s)"
    cur.execute(sql,(id, name, price, quantity))
    conn.commit()
    return True
#減少購物車商品量
def removeMyList(id):
    sql="UPDATE `我的購物車` SET `amount`= amount-1 WHERE id=%s and amount != 0;"
    cur.execute(sql,(id,))
    conn.commit()
    return True
#從購物車移除
def deleteFromMyList(id):
    sql="DELETE FROM `我的購物車` WHERE id = %s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True
#卻保有足夠存貨
def checkS(id):
    sql="SELECT `stock` FROM `商家db` WHERE id=%s"
    cur.execute(sql,(id,))
    S = cur.fetchall()
    return S
def checkQ(id):
    sql="SELECT `quantity` FROM `我的購物車` WHERE id=%s"
    cur.execute(sql,(id,))
    Q = cur.fetchall()
    return Q

#商家管理
#查詢存貨列表
def getShopList():
    sql="select id, name, price, stock from 商家db order by id asc;"
    cur.execute(sql)
    shopList = cur.fetchall()
    return shopList
#增加庫存
def add(id, stock):
    sql="UPDATE `商家db` SET `stock`=stock+%s WHERE id=%s;"#不能將newStock加入stock,
    cur.execute(sql,(stock, id))
    conn.commit()
    return True
#出貨
def ship(id, quantity):
    sql="UPDATE `商家db` SET `stock`= stock-%s WHERE id=%s;"
    cur.execute(sql,(quantity, id))
    conn.commit()
    return True
#新增商品至賣場
def addStock(id, name, price, stock):
    sql="INSERT INTO 商家db(id, name, price, stock) VALUES (%s, %s, %s, %s)"
    cur.execute(sql,(id, name, price, stock))
    conn.commit()
    return True
#將商品下架
def deleteFromShop(id):
    sql="DELETE FROM `商家db` WHERE id = %s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True

#加入或移除後
#存貨列表更新
def updateShopList(id):
    sql="UPDATE `商家db` SET `stock`= stock WHERE id=%s and stock != 0;"
    cur.execute(sql,(id,))
    conn.commit()
    return True
#購物車更新
def updateMyList(id):
    sql="UPDATE `我的購物車` SET `quantity`= quantity WHERE id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True

def getStock(id):
    sql="SELECT `stock` FROM `商家db` WHERE id=%s"
    cur.execute(sql,(id,))
    conn.commit()
    return True