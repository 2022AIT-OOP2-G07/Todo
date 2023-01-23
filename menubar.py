import datetime
import time
import rumps
import sqlite3
# import threading


index=0
flag=True
class MenuBar(rumps.App):
    def __init__(self):
        global index
        cur = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
        # print(cur.fetchall()[0][1])
        super(MenuBar, self).__init__(name="メニューバーtodo",title=cur.fetchall()[index][1],icon=None)
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
        con = sqlite3.connect('todo_list.db')   #データベースに接続
        cur1 = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")    #昇順にデータを取り出し
        siteizikan=cur1.fetchall()[index][2]    #[(1, 'ご飯を食べる', '2023-01-24 02:45', 0)]　ー＞時間を取り出し
        cur2 = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
        todo=cur2.fetchall()[index][1]  #todo内容の取り出し

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
            try:
                
                print('実行時間になりました')
                print('現在時刻：' , datetime.datetime.now())

                index+=1
                cur2 = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
                try:
                    
                    next_todo=cur2.fetchall()[index][1]
                    print("-------------")
                    print(f'次の予定は[{next_todo}]です。')
                    print(f'index:{index}')

                    flag=True
                    print(f'flag:{flag}')
                    print("-------------")
                    app.title=next_todo
                except:
                    flag=False
                    print("次の予定はありません")
                
                
                self.tuuti(todo)

            except  Exception:
                print("通知関数を呼び出せませんでした。")

        except  Exception:
            print("🟨期限が過ぎているため通知登録ができません。")
        
        



    def tuuti(self,todo):
        global flag

        show_text = f"現在時刻は[{datetime.datetime.now()}]です。お疲れ様でした。"
        text= f"「{todo}」の期限が終了しました。"
        rumps.notification(     #通知
            todo,   #todo内容
            text,
            show_text,
            # icon="fois.png",
        )
        # if flag==True:
        #     self.startTrigar()


if __name__ == "__main__":
    con = sqlite3.connect('todo_list.db')
        
    con.execute("CREATE TABLE IF NOT EXISTS todo(id integer PRIMARY KEY, todo_data text, todo_deadline datetime, check_data boolean)")
    # # # # ３．テーブルにデータを追加
    con.execute("DELETE FROM todo WHERE id = 1") 
    con.execute("DELETE FROM todo WHERE id = 2") 
    con.execute("DELETE FROM todo WHERE id = 3") 
    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'ご飯を食べる','2023-01-24 03:59',false)")
    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(2,'勉強をする','2023-01-24 04:00',false)")
    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(3,'おせちを食べる','2023-01-24 04:01',true)")
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'今すぐやれ','2023-01-19 20:05',true)")
    con.commit()

    app=MenuBar()
    app.run()
    