# -*- coding: utf-8
import sqlite3
import rumps

# データベース開く
db = sqlite3.connect(
    "sarvant.db")

c = db.cursor()
# テーブル作成
#c.execute('create table artoria (name text, atk int, hp int)')

# # データ追加(レコード登録)
# sql = 'insert into artoria (name, atk, hp) values (?,?,?)'
# data = ('artoria', 11221, 15150)
# c.execute(sql, data)

# コミット
db.commit()

# # データ（レコード）取得
# sql = 'select * from artoria'
# for row in c.execute(sql):
#     print(row)


class HelloApp(rumps.App):
    pass


if __name__ == "__main__":
    HelloApp("HelloApp", icon="img/icon/fois.png", quit_button="終了").run()


# クローズ
db.close()

"""
('artoria', 11221, 15150)
"""
