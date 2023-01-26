# 1/24 04:17時点で最新ver
# 1/26 21:11時点で最新ver
# 実行可

import datetime
import time
import rumps
import sqlite3


index = 0
flag = True


index = 0
flag = True


class MenuBar(rumps.App):
    def __init__(self):
        global index
        cur = con.execute(
            "select * from todo where todo_deadline <> 1 order by todo_deadline")
        # print(cur.fetchall()[0][1])
        super(MenuBar, self).__init__(name="メニューバーtodo",
                                      title=cur.fetchall()[index][1], icon=None)


stak = 0


class MenuBar(rumps.App):
    print("a")

    def __init__(self):
        global stak
        stak = 0
        print(stak)
        # stak=0
        # cur1 = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
        # startTrigar(cur1.fetchall()[0][2])
        # app.run()
        # cur = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
        # print(cur.fetchall()[0][1])
        # todo=cur.fetchall()[0][0]
        cur = con.execute(
            "select * from todo where todo_deadline <> 1 order by todo_deadline")
        super(MenuBar, self).__init__(name="メニューバーtodo",
                                      title=cur.fetchall()[stak][1], icon=None)
        # self.startTrigar()
    # print("2023-01-23 17:00")
        super(MenuBar, self).__init__(name="メニューバーtodo",
              title=cur.fetchall()[index][1], icon=None)
    # print(cur1.fetchall())
    # print(cur1.fetchall())
        cur.close()
        con.close()
    print("a")

    @rumps.clicked("通知オン")
    def reload(self, _):
        self.startTrigar()

    def startTrigar(self):  # aaa

        global index
        global flag

        print("aaa")
        con = sqlite3.connect('todo_list.db')  # データベースに接続
        cur1 = con.execute(
            "select * from todo where todo_deadline <> 1 order by todo_deadline")  # 昇順にデータを取り出し
        # [(1, 'ご飯を食べる', '2023-01-24 02:45', 0)]　ー＞時間を取り出し
        siteizikan = cur1.fetchall()[index][2]
        cur2 = con.execute(
            "select * from todo where todo_deadline <> 1 order by todo_deadline")
        todo = cur2.fetchall()[index][1]  # todo内容の取り出し

        print("aaa")
        con = sqlite3.connect('todo_list.db')  # データベースに接続
        cur1 = con.execute(
            "select * from todo where todo_deadline <> 1 order by todo_deadline")  # 昇順にデータを取り出し
        # [(1, 'ご飯を食べる', '2023-01-24 02:45', 0)]　ー＞時間を取り出し
        siteizikan = cur1.fetchall()[index][2]
        cur2 = con.execute(
            "select * from todo where todo_deadline <> 1 order by todo_deadline")
        todo = cur2.fetchall()[index][1]  # todo内容の取り出し

        global stak
        print(f"aaa{stak}")
        con = sqlite3.connect('todo_list.db')
        cur1 = con.execute(
            "select * from todo where todo_deadline <> 1 order by todo_deadline")
        siteizikan = cur1.fetchall()[stak][2]
        cur1 = con.execute(
            "select * from todo where todo_deadline <> 1 order by todo_deadline")
        todo = cur1.fetchall()[stak][1]
        try:
            cur1 = con.execute(
                "select * from todo where todo_deadline <> 1 order by todo_deadline")
            nextTodo = cur1.fetchall()[stak+1][1]
        except Exception:
            pass
        cur1.close()
        con.close()

        data = datetime.datetime.now()
        # 取り出した期限の時間（siteizikan）は文字列だからdateオブジェクトに変換
        exec_time = datetime.datetime.strptime(siteizikan, '%Y-%m-%d %H:%M')

        # print(type(data))

        print("-----------------------------------")
        print('現在時刻：', data)
        print('実行時間：', exec_time, 'まで待機します。')
        print("-----------------------------------")

        sleep_time = exec_time - data  # (期限)ー(現在時刻)でタイマー時間を算出

        # print(type(sleep_time.total_seconds()))
        print(f'ーー{sleep_time}秒後に通知するよーー')

        try:
            time.sleep(sleep_time.total_seconds())

            try:

                print('実行時間になりました')
                print('現在時刻：', datetime.datetime.now())

                index += 1
                cur2 = con.execute(
                    "select * from todo where todo_deadline <> 1 order by todo_deadline")
                try:

                    next_todo = cur2.fetchall()[index][1]
            try:

                print('実行時間になりました')
                print('現在時刻：', datetime.datetime.now())

                index += 1
                cur2 = con.execute(
                    "select * from todo where todo_deadline <> 1 order by todo_deadline")
                try:

                    next_todo = cur2.fetchall()[index][1]
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

                self.tuuti(todo)

            except Exception:
                print("通知関数を呼び出せませんでした。")

        except Exception:
            print("🟨期限が過ぎているため通知登録ができません。")

            print('実行時間になりました')
            print('現在時刻：', datetime.datetime.now())
            app.title = nextTodo
            stak += 1
            self.tuuti(todo)
        except Exception:
            stak += 1
            print('時刻：', siteizikan)
            print("🟨期限が過ぎているため通知登録ができません。")
                    flag = True
                    print(f'flag:{flag}')
                    print("-------------")
                    app.title = next_todo
                except:
                    flag=False
                    print("次の予定はありません")
                
                
                self.tuuti(todo)

            except  Exception:
                print("通知関数を呼び出せませんでした。")

        except  Exception:
            print("🟨期限が過ぎているため通知登録ができません。")
        
        

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
        text= f"「{todo}」の期限が終了しました。"
        )
        rumps.notification(     #通知
            todo,   #todo内容
            text,
            show_text,
            # icon="fois.png",
        )
        # if flag==True:
        #     self.startTrigar()

    def tuuti(self, todo):
        # cur = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")
        show_text = f"現在時刻は[{datetime.datetime.now()}]です。お疲れ様でした。"
        text = f"「{todo}」の期限が終了しました"
        rumps.notification(  # 通知
            todo,  # タイトル

            show_text,
            # icon="fois.png",
        )
        app.title = self.n
        self.startTrigar()
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
    con.execute("DELETE FROM todo WHERE id = 2")
    con.execute("DELETE FROM todo WHERE id = 3")
    con.execute(
        "INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'ご飯を食べる','2023-01-24 03:59',false)")
    con.execute(
        "INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(2,'勉強をする','2023-01-24 04:00',false)")
    con.execute(
        "INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(3,'おせちを食べる','2023-01-24 04:01',true)")
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'今すぐやれ','2023-01-19 20:05',true)")
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'ご飯を食べる','2023-01-12 19:00',false)")
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(2,'勉強をする','2023-01-23 17:00',false)")
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(3,'おせちを食べる','2023-01-01 12:00',true)")
    con.execute("DELETE FROM todo WHERE id = 1")
    con.execute("DELETE FROM todo WHERE id = 2")
    con.execute("DELETE FROM todo WHERE id = 3")
    con.execute("DELETE FROM todo WHERE id = 4")

    con.execute(
        "INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(2,'sec','2023-01-19 23:15',true)")
    con.execute(
        "INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'fi','2023-01-19 23:14',true)")
    con.execute(
        "INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(4,'four','2023-01-19 23:17',true)")
    con.execute(
        "INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(3,'thir','2023-01-19 23:16',true)")
    # con.execute("DELETE FROM todo WHERE id = 1")

    con.execute("DELETE FROM todo WHERE id = 1") 
    con.execute("DELETE FROM todo WHERE id = 2") 
    con.execute("DELETE FROM todo WHERE id = 3") 
    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'ご飯を食べる','2023-01-24 03:59',false)")
    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(2,'勉強をする','2023-01-24 04:00',false)")
    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(3,'おせちを食べる','2023-01-24 04:01',true)")
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'今すぐやれ','2023-01-19 20:05',true)")
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
