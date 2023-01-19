# ０．sqlite3をインポート。これがないと始まらない
import sqlite3
# １．DB接続。ファイルがなければ作成する
con = sqlite3.connect('todo_list.db')
# ２．テーブル作成
# con.execute("CREATE TABLE IF NOT EXISTS todo(id integer PRIMARY KEY, todo_data text, todo_deadline datetime, check_data boolean)")
# # # ３．テーブルにデータを追加
# con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'ご飯を食べる','2023-01-12 19:00',false)")
# con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(2,'勉強をする','2023-01-23 17:00',false)")
# con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(3,'おせちを食べる','2023-01-01 12:00',true)")
# con.commit()


# # 5．データ削除
# ##con.execute("DELETE FROM todo WHERE id = 1")
# ##con.execute("DELETE FROM todo WHERE id = 2")
# ##con.execute("DELETE FROM todo WHERE id = 3")
# con.commit()
# ４．データ参照
cur = con.execute("SELECT * FROM todo")
# for row in cur:
#     print(row[1])
#     print(type(row[1]))
print(cur.fetchall()[0][1])

cur.close()

# 6．テーブル削除
##con.execute("DROP TABLE todo")
# 7．DB接続解除
con.close()
