import datetime
import time
import rumps
import sqlite3
import threading


stak=0
class MenuBar(rumps.App):
    print("a")
    def __init__(self):
        global stak
        stak=0
        print(stak)
        # stak=0
        # cur1 = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
        # startTrigar(cur1.fetchall()[0][2])
        # app.run()
        # cur = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
        # print(cur.fetchall()[0][1])
        # todo=cur.fetchall()[0][0]
        cur = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
        super(MenuBar, self).__init__(name="メニューバーtodo",title=cur.fetchall()[stak][1],icon=None)
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
        global stak
        print(f"aaa{stak}")
        con = sqlite3.connect('todo_list.db')
        cur1 = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
        siteizikan=cur1.fetchall()[stak][2]
        cur1 = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
        todo=cur1.fetchall()[stak][1]
        try:
            cur1 = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
            nextTodo=cur1.fetchall()[stak+1][1]
        except Exception:
            pass
        cur1.close()
        con.close()
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
            app.title=nextTodo
            stak+=1
            self.tuuti(todo)
        except  Exception:
            stak+=1
            print('時刻：' , siteizikan)
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

    def tuuti(self,todo):
        # cur = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
        show_text = f"現在時刻は[{datetime.datetime.now()}]です。お疲れ様でした。"
        text= f"「{todo}」の期限が終了しました"
        rumps.notification(     #通知
            todo,#タイトル
            
            show_text,
            # icon="fois.png",
        )
        app.title=self.n
        self.startTrigar()


if __name__ == "__main__":
    con = sqlite3.connect('todo_list.db')
        
    con.execute("CREATE TABLE IF NOT EXISTS todo(id integer PRIMARY KEY, todo_data text, todo_deadline datetime, check_data boolean)")
    # # # # ３．テーブルにデータを追加
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'ご飯を食べる','2023-01-12 19:00',false)")
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(2,'勉強をする','2023-01-23 17:00',false)")
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(3,'おせちを食べる','2023-01-01 12:00',true)")
    con.execute("DELETE FROM todo WHERE id = 1")
    con.execute("DELETE FROM todo WHERE id = 2")
    con.execute("DELETE FROM todo WHERE id = 3")
    con.execute("DELETE FROM todo WHERE id = 4")

    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(2,'sec','2023-01-19 23:15',true)")
    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'fi','2023-01-19 23:14',true)")
    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(4,'four','2023-01-19 23:17',true)")
    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(3,'thir','2023-01-19 23:16',true)")
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