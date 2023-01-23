import datetime
import time
import rumps
import sqlite3
# import threading


index=0
class MenuBar(rumps.App):
    def __init__(self):
        global index
        cur = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
        # print(cur.fetchall()[0][1])
        super(MenuBar, self).__init__(name="メニューバーtodo",title=cur.fetchall()[index][1],icon=None)
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
        global index
        global flag
        print("aaa")
        con = sqlite3.connect('todo_list.db')
        cur1 = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
        siteizikan=cur1.fetchall()[index][2]

        data=datetime.datetime.now()
        exec_time = datetime.datetime.strptime(siteizikan ,'%Y-%m-%d %H:%M')    #取り出した期限の時間（siteizikan）は文字列だからdateオブジェクトに変換

        # print(type(data))

        print("-----------------------------------")
        print('現在時刻：' , data)
        print('実行時間：' , exec_time , 'まで待機します。')
        print("-----------------------------------")

        sleep_time = exec_time - data   #(期限)ー(現在時刻)でタイマー時間を算出

        # print(type(sleep_time.total_seconds()))
        print(f'ーー{sleep_time}秒後に通知するよーー')
        
        try:
            time.sleep(sleep_time.total_seconds())
            print('実行時間になりました')
            print('現在時刻：' , datetime.datetime.now())
        except  Exception:
            print("🟨期限が過ぎているため通知登録ができません。")

        


    def tuuti(self,todo):
        global flag

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

    app=MenuBar()
    app.run()
    