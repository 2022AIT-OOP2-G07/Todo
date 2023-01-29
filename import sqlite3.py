import sqlite3

dbname = 'todo_list.db'
# 1.データベースに接続
con = sqlite3.connect(dbname)

# 2.sqliteを操作するカーソルオブジェクトを作成
cur = con.cursor()

# 3.テーブルのデータを削除
con.execute('delete from todo where id = 1')
con.commit()

# 取得したデータを出力
cur.execute('SELECT * FROM todo')
for row in cur:
    print(row)
# print(cur.fetchall())

# 4.データベースの接続を切断
cur.close()
con.close()
