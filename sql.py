from dbConfig import conn, cur
#查詢存貨列表
def getShopList():
    sql=
    cur.execute(sql)
    shopList = cur.fetchall()
    return shopList
#我的購物車
def getMyList():
    sql=
    cur.execute(sql)
    shopList = cur.fetchall()
    return shopList
#商品加入購物車
def addMyList():
    sql=
    cur.execute(sql,(id,))
    conn.commit()
    return True
#商品移除購物車
def removeMyList():
    sql=
    cur.execute(sql,(id,))
    conn.commit()
    return True

#加入移除後
#存貨列表更新
def updateShopList():
    sql=
    cur.execute(sql,(id,))
    conn.commit()
    return True
#購物車更新
def updateMyList():
    sql=
    cur.execute(sql,(id,))
    conn.commit()
    return True

#商家進貨
def add():
    sql=
    cur.execute(sql,(id,stock))
    conn.commit()
    return True
#增加存貨至賣場
def addList():
    sql=
    cur.execute(sql,(id,))
    conn.commit()
    return True

#刪除商品
#從賣場移除
def deleteFromShop(id):
    sql="DELETE FROM `shoplist` WHERE id = %s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True
#從購物車移除
def deleteFromMyList(id):
    sql="DELETE FROM `shoplist` WHERE id = %s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True