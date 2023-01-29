# 1/29 02:06時点で最新ver

# エラーコード
# ERROR[1]->データベースに登録されている時間データが正しい書式で登録されていない
# ERROR[2]->登録されたtodo名が長いことで通知センターから怒られている？

import datetime
import json
import rumps
import sqlite3

# １．DB接続。ファイルがなければ作成する
con = sqlite3.connect('todo_list.db')

# ２．テーブル作成
con.execute("CREATE TABLE IF NOT EXISTS todo(id integer PRIMARY KEY, todo_data text, todo_deadline datetime, check_data boolean)")
con.commit()

# ４．データ参照
cur = con.execute("SELECT * FROM todo")
for row in cur:
    # print(row[1])
    # print(type(row[1]))

    # cur.close()

    # con.close()


@rumps.clicked("Hello World")
def hello_world(sender):
    rumps.alert("Hello World")


if __name__ == "__main__":
    app = rumps.App("Rumps Test", title=None, icon="img/icon/icon.png",
                    quit_button="終了").run()
    # HelloApp("HelloApp", icon="img/icon/icon.png", quit_button="終了").run()
