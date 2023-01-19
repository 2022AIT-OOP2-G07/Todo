import datetime
import time
import rumps
import sqlite3
import threading


timer=0
class MenuBar(rumps.App):
    @rumps.timer(1)
    def hello_world_repeat(sender):
        print ("タイマーだよ")
    print("a")
    def __init__(self):
        # cur1 = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
        # startTrigar(cur1.fetchall()[0][2])
        # app.run()
        cur = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
        # print(cur.fetchall()[0][1])
        super(MenuBar, self).__init__(name="メニューバーtodo",title=cur.fetchall()[0][1],icon=None)
        # self.startTrigar()
    # print("2023-01-23 17:00")
    # print(cur1.fetchall())
    # print(cur1.fetchall())
        cur.close()
        con.close()
    print("a")

    @rumps.clicked("通知オン")
    def reload(self, _):
        self.startTrigar()
    


    def startTrigar(self):#aaa
        print("aaa")
        con = sqlite3.connect('todo_list.db')
        cur1 = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
        siteizikan=cur1.fetchall()[0][2]

        data=datetime.datetime.now()
        # exec_time = datetime.datetime(2023,1,14,5,50,30,0)
        exec_time = datetime.datetime.strptime(siteizikan ,'%Y-%m-%d %H:%M')
        
        print(exec_time)
        print('現在時刻：' , data)
        print('実行時間：' , exec_time , 'まで待機します。')
        sleep_time = exec_time - data
        print(type(data))
        print(type(sleep_time.total_seconds()))
        print(sleep_time)
        
        try:
            time.sleep(sleep_time.total_seconds())
            print('実行時間になりました')
            print('現在時刻：' , datetime.datetime.now())
            time.sleep(2)
        except  Exception:
                print("🟨期限が過ぎているため通知登録ができません。")

        

    # def startTrigar(siteizikan):
        
    #     data=datetime.datetime.now()
    #     # exec_time = datetime.datetime(2023,1,14,5,50,30,0)
    #     exec_time = datetime.datetime.strptime(siteizikan ,'%Y-%m-%d %H:%M')
    #     print(type(data))
    #     # exec_time
    #     print('現在時刻：' , data)
    #     print('実行時間：' , exec_time , 'まで待機します。')
    #     sleep_time = exec_time - data
    #     print(type(sleep_time.total_seconds()))
    #     print(sleep_time)
    #     time.sleep(sleep_time.total_seconds())

    #     tuuti()

    #     print('実行時間になりました')
    #     print('現在時刻：' , datetime.datetime.now())
    #     time.sleep(1)

    def tuuti(self):
        show_text = f"現在時刻は[{datetime.datetime.now()}]です"
        rumps.notification(     #通知
            "Helloタイトル",#タイトル
            "Hello world",
            show_text,
            # icon="fois.png",
        )


if __name__ == "__main__":
    con = sqlite3.connect('todo_list.db')
        
    con.execute("CREATE TABLE IF NOT EXISTS todo(id integer PRIMARY KEY, todo_data text, todo_deadline datetime, check_data boolean)")
    # # # # ３．テーブルにデータを追加
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'ご飯を食べる','2023-01-12 19:00',false)")
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(2,'勉強をする','2023-01-23 17:00',false)")
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(3,'おせちを食べる','2023-01-01 12:00',true)")
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'今すぐやれ','2023-01-19 20:05',true)")
    # con.execute("DELETE FROM todo WHERE id = 7")
    # con.execute("DELETE FROM todo WHERE id = 1") 
    con.commit()

    
    

    # cur1 = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
    # startTrigar(cur1.fetchall()[0][2])
    # app=
    # MenuBar().run()
    # startTrigar()
    app=MenuBar()
    app.run()
    # thread_1 = threading.Thread(target=MenuBar().run())
    # thread_2 = threading.Thread(target=startTrigar)

    # thread_2.start()
    # thread_1.start()