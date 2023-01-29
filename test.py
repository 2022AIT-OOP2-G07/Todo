# -*- coding: utf-8
#!/usr/bin/env python
import sqlite3
import rumps
# import app
# import subprocess
import webbrowser

task = []
# taskNumbar = 1

con = sqlite3.connect('todo_list.db')  # データベースに接続
cur = con.execute(
    "select * from todo where todo_deadline <> 1 order by todo_deadline")


def getData(self):
    con = sqlite3.connect('todo_list.db')  # データベースに接続
    cur = con.execute(
        "select * from todo()")
    print(cur)


def delete_task():
    con.execute('delete from todo where id = taskNumbar')
    con.commit()


class MenuBar(rumps.App):
    def __init__(self):
        super(MenuBar, self).__init__(
            "MenuBar", icon="static/img/icon/icon.png", quit_button="終了")
        taskNumbar = 1
        for doc in cur:
            task.append(doc[1])
            print(task)
            self.menu = task
            # self.menu[task[0]].add("削除")
            # delete_task()
            # self.menu[task[0]].add
            taskNumbar += 1
            del task[0]
        taskNumbar = 1

    @rumps.clicked("Webを開く")
    def Web(self, _):
        webbrowser.open("http://127.0.0.1:5000")

    # 未完
    @rumps.clicked("'MenuBar'を更新する")
    def update(self, _):
        con = sqlite3.connect('todo_list.db')
        cur.execute('SELECT * FROM todo')
        con.commit()
        # cur.close()
        # con.close()


# @rumps.clicked("Notify!")
if __name__ == "__main__":
    MenuBar().run()
