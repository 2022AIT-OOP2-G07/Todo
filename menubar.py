import datetime
import time
import rumps
import sqlite3


class MenuBar(rumps.App):
    def __init__(self):
        con = sqlite3.connect('todo_list.db')
        cur = con.execute("SELECT * FROM todo")
        # print(cur.fetchall()[0][1])
        super(MenuBar, self).__init__(name="メニューバーtodo",title=cur.fetchall()[0][1],icon=None)
        cur.close()
        con.close()

    @rumps.clicked("通知オン")
    def reload(self, _):
        startTrigar("2023-1-15 00:46:0.0000")



def startTrigar(siteizikan):
    data=datetime.datetime.now()
    # exec_time = datetime.datetime(2023,1,14,5,50,30,0)
    exec_time = datetime.datetime.strptime(siteizikan ,'%Y-%m-%d %H:%M:%S.%f')
    print(type(data))
    # exec_time
    print('現在時刻：' , data)
    print('実行時間：' , exec_time , 'まで待機します。')
    sleep_time = exec_time - data
    print(type(sleep_time.total_seconds()))
    print(sleep_time)

    time.sleep(sleep_time.total_seconds())

    tuuti()

    print('実行時間になりました')
    print('現在時刻：' , datetime.datetime.now())

def tuuti():
    show_text = f"現在時刻は[{datetime.datetime.now()}]です"
    rumps.notification(     #通知
        "Helloタイトル",#タイトル
        "Hello world",
        show_text,
        # icon="fois.png",
    )


if __name__ == "__main__":
    app=MenuBar()
    app.run()
    
    # MenuBar("HelloApp", icon="icon/fois.png", quit_button="終了").run()
    # get.getData("2023-1-15 00:37:30.0000")

