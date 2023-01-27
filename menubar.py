# 1/26 21:11時点で最新ver
# 実行可

import datetime
import time
import rumps
import sqlite3


index = 0
flag = True

data=[]

def getData():
    global data
    con = sqlite3.connect('todo_list.db')  # データベースに接続
    cur = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")  # 昇順にデータを取り出し
    # [(1, 'ご飯を食べる', '2023-01-24 02:45', 0)]　ー＞時間を取り出し
    z=cur.fetchall()
    if data!= z and len(data)!=0:
        print("------------------------")
        print("⭐️データが更新されました⭐️")
        print("------------------------")
    data = z
    
    cur.close()
    con.close()

# def check_menubar():
#     global index,data
#     for el in data:
#         if

# def check_tuuti():
#     global index,data
#     for el in data:
#         if



class MenuBar(rumps.App):

    def __init__(self):
        global index,data
        getData()
        print(data)
        # for 
        super(MenuBar, self).__init__(name="メニューバーtodo",title=data[index][1], icon=None)
        print("アプリ起動-no problem")
    

    

    def tuuti(self, todo):
        global flag

        show_text = f"現在時刻は[{datetime.datetime.now()}]です。お疲れ様でした。"
        text = f"「{todo}」の期限が終了しました。"
        rumps.notification(  # 通知
            todo,  # todo内容
            text,
            show_text,
            # icon="fois.png",
        )
        # if flag==True:
        #     self.startTrigar()

    @rumps.clicked("通知オン")
    def timer(self, _):
        
        def trigar(t):
            global index
            global flag,data
            
            getData()
            print(data)
            siteizikan = data[index][2]  # [(1, 'ご飯を食べる', '2023-01-24 02:45', 0)]　->時間を取り出し
            todo = data[index][1]  # todo内容の取り出し

            siteizikan_date = datetime.datetime.strptime(siteizikan, '%Y-%m-%d %H:%M')  # 取り出した期限の時間（siteizikan）は文字列だからdateオブジェクトに変換
            siteizikan_format=siteizikan_date.strftime("%Y-%m-%d %H:%M")    #dateオブジェクトに変換したsiteizikan_dateを"%Y-%m-%d %H:%M"にフォーマット
            now = datetime.datetime.now()
            now_format=now.strftime("%Y-%m-%d %H:%M")
            print(f"sitei:{siteizikan_format}")
            print(f"now:{now_format}")
            
            print("a")
            if siteizikan_format == now_format:
                
                try:
                    print(f"{todo}の時間だよ！")
                    print('現在時刻：', datetime.datetime.now())
                    index += 1
                    
                    try:
                        next_todo = data[index][1]
                        print("-------------")
                        print(f'次の予定は[{next_todo}]です。')
                        print(f'index:{index}')
                        
                        flag = True
                        print(f'flag:{flag}')
                        print("-------------")
                        app.title = next_todo
                    except:
                        flag = False
                        print("次の予定はありません")
                        t.stop()
                    
                except Exception:
                    print("通知関数を呼び出せませんでした。")
                self.tuuti(todo)    #検査のためにtry文だしてる
                

        
        timer = rumps.Timer(callback=trigar, interval=1)
        timer.start()
        
    # @rumps.clicked("更新")
    # def timer(self, _):
    #     pass


if __name__ == "__main__":
    con = sqlite3.connect('todo_list.db')

    con.execute(
        "CREATE TABLE IF NOT EXISTS todo(id integer PRIMARY KEY, todo_data text, todo_deadline datetime, check_data boolean)")
    # # # # ３．テーブルにデータを追加
    con.execute("DELETE FROM todo WHERE id = 1")
    # con.execute("DELETE FROM todo WHERE id = 2")
    # con.execute("DELETE FROM todo WHERE id = 3")
    # con.execute("DELETE FROM todo WHERE id = 4")

    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(4,'4＿課題提出','2023-01-26 21:42',false)")
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(2,'2＿朝ごはんだよ','2023-01-26 21:40',false)")
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(3,'3＿出る時間だよ','2023-01-26 21:41',true)")
    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'1＿起きるよ','2023-01-27 02:43',true)")
    con.commit()

    app = MenuBar()
    app.run()
