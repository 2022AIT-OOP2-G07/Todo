# ０．sqlite3をインポート。これがないと始まらない
import sqlite3
# １．DB接続。ファイルがなければ作成する
con = sqlite3.connect('todo_list.db')
# ２．テーブル作成

con.execute("CREATE TABLE IF NOT EXISTS todo(id integer PRIMARY KEY, todo_data text, todo_deadline datetime, check_data boolean)")
# (通知ボタンを押すことで一番近い予定の期限になったら通知を送ってくれる)

# 3．データ参照
cur = con.execute("SELECT * FROM todo")
