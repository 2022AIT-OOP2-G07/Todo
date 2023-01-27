# 1/28 4:53時点で最新ver
# 実行可

import datetime
import json
# import time
import rumps
import sqlite3
c=0
k=0

json_file = open('setting.json', 'r')
notification_flag = json.load(json_file)
notification = notification_flag["notification"]

index_bar = 0
index_tuuti = 0
flag = True
# tuuti_state = notification
tuuti_state=None
data=[]
timer_stop=False

def getData(self):
    global data,reloade,tuuti_state,notification,c
    # print(f"🟦------------------{tuuti_state}")
    con = sqlite3.connect('todo_list.db')  # データベースに接続
    cur = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")  # 昇順にデータを取り出し
    # [(1, 'ご飯を食べる', '2023-01-24 02:45', 0)]　ー＞時間を取り出し
    z=cur.fetchall()
    
    print(f"getData{reloade._status}--スレッド数：{c}個")
    if data!= z and len(data)!=0:
        # print(f"🟦------------------{tuuti_state}")
        print("------------------------")
        print("⭐️データが更新されました⭐️")
        print("------------------------")
        print(data)
        print("----------------------------------------------")
        print(z)
        print("----------------------------------------------")
        tuuti_state=False
        data = z
        hyouzi=check_menubar()
        print(f"-hyouzi-{hyouzi}")
        check_tuuti()
        # print(f"🟦------------------{tuuti_state}")
        
        app.title = hyouzi+'×' if notification != True else hyouzi+'⚪︎'
        print(hyouzi+'×' if notification != True else hyouzi+'⚪︎')

        if reloade._status == True:
            c-=1
            print("------------------------------------------------------(1)")
            reloade.stop()
        
        if notification == True and flag == True:
            print("???????????????")
            swich(self)
        else:
            
            if reloade._status == False:
                c+=1
                print("------------------------------------------------------[1]")
                reloade.start()
        
    else:
        # check_tuuti()
        data = z
    
    
    cur.close()
    con.close()

def check_menubar():
    global index_bar,data,flag
    index_bar=0
    for el in data:
            if el[3]==0:
                print(f"{el[1]}:メニューバー表示可能⭕️{el[3]}")
                break
            else:
                print(f"{el[1]}:メニューバー表示可能❌")
                index_bar+=1
    # print(f"index:{index_bar}")
    if index_bar<len(data):
        print(f"メニューバー表示は「{data[index_bar][1]}(index:{index_bar})」に設定します")
        return data[index_bar][1]
    else:
        print("すべて実行済みです")
        flag=False
        return "すべて実行済みです"



def check_tuuti():
    global index_tuuti,data,flag,timer_stop,reloade,tuuti_state,c
    index_tuuti=0
    for el in data:
        try:
            kigen_time = datetime.datetime.strptime(el[2], '%Y-%m-%d %H:%M')
            now = datetime.datetime.now()
        except Exception:
            print("🚨dateオブジェクトに変換中に問題が発生しました🚨")
            break
            flag=False

        if kigen_time > now and el[3]==0:
            print(f"{el[1]}:通知設定可能⭕️")
            break
        else:
            print(f"{el[1]}:通知設定不可能❌")
            index_tuuti+=1
    if index_tuuti<len(data):
        print(f"通知設定は「{data[index_tuuti][1]}(index:{index_tuuti})」に設定します")
        app.title=data[index_bar][1]+'×' if notification == False else data[index_bar][1]+'⚪︎'
        flag=True
        timer_stop=False
        
        # return data[index_bar][1]
    else:
        print("すべて通知不可です")
        print(f"通知設定(index:{index_tuuti})")
        flag=False
        print(f"------------------------------timerSTOPはP103")
        timer_stop=True
        print(f"ーーーーー116ーーーーーー{notification}")
        print(f"ーーーーーーーーーーー{tuuti_state}")
        if reloade._status == False:
            c+=1
            print("------------------------------------------------------[5]")
            reloade.start()
        return "すべて実行済みです"

def trigar(t):
    global index_bar,index_tuuti
    global flag,data,tuuti_state,timer_stop,reloade,c,k
    
    getData(t)  #⏬怪しい
    # print(f"🟦------------------{tuuti_state}")
    # print(f"t:{t._status}")
    print(f"trigae:{t._status}--スレッド数：{k}個")
    # print(f"timer_stop---{timer_stop}")
    if timer_stop:
        print(f"t.statue:{t._status}")
        if t._status == True:
            k-=1
            print("------------------------------------------------------(k1)")
            t.stop()
        timer_stop=False
        tuuti_state = False
        app.title=data[index_bar][1]+'×' if tuuti_state == False else data[index_bar][1]+'⚪︎'
        # print(f"----{timer_stop}")
        print("--通知をオフにします--")
        
        if reloade._status == False:
            c+=1
            print("------------------------------------------------------[2]")
            reloade.start()
        return
    else:
        if reloade._status == True:
            c-=1
            print("------------------------------------------------------(2)")
            reloade.stop()
    
    siteizikan = data[index_tuuti][2]  # [(1, 'ご飯を食べる', '2023-01-24 02:45', 0)]　->時間を取り出し
    todo = data[index_tuuti][1]  # todo内容の取り出し

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
            # index_tuuti += 1
            tuuti(todo)
            #getData()
            try:
                next_todo = data[index_tuuti+1][1]
                print("-------------")
                print(f'次の予定は[{next_todo}]です。')
                print(f'index:{index_bar+1}')
                
                # flag = True
                # print(f'flag:{flag}')
                print("-------------")
                # app.title = next_todo
                # app.title=next_todo+'×' if tuuti_state == False else next_todo+'⚪︎'
            except:
                # flag = False
                print("🟡次の予定はありません")
                if t._status == True:
                    k-=1
                    print("------------------------------------------------------(k2)")
                    t.stop()
                tuuti_state = False
                
                if reloade._status == False:
                    c+=1
                    print("------------------------------------------------------[3]")
                    reloade.start()
            
        except Exception:
            print("🚨通知関数を呼び出せませんでした。🚨")
        check_tuuti()
                    
reloade = rumps.Timer(callback=getData, interval=1)

def swich(self):
    global tuuti_state,timer_stop,reloade,c,k
    print("-------P172--------")
    timer = rumps.Timer(callback=trigar, interval=1)
    hyouzi=check_menubar()
    if flag==True:
        self.title = data[index_bar][1]+'×' if notification != True else data[index_bar][1]+'⚪︎'
        print(data[index_bar][1]+'×' if notification != True else data[index_bar][1]+'⚪︎')
    else:
        self.title = hyouzi+'×' if notification != True else hyouzi+'⚪︎'
        print(hyouzi+'×' if notification != True else hyouzi+'⚪︎')

    if notification == True:
        if tuuti_state!=True:
            if flag != False:
                print(f"ーーーーー184ーーーーーー{notification}")
                print(f"ーーーーーーーーーーー{tuuti_state}")
                if timer._status == False:
                    k+=1
                    print("------------------------------------------------------[k1]")
                    timer.start()
                print(f"-----------{tuuti_state}")
                
                print("--通知をオンにしました--")
                tuuti_state=True
            else:
                print(f"ーーーーー192ーーーーーー{notification}")
                print(f"ーーーーーーーーーーー{tuuti_state}")
                print("🟡すべて期限が過ぎています")
                
                if reloade._status == False:
                    c+=1
                    print("------------------------------------------------------[4]")
                    reloade.start()
        else:
            print(f"ーーーーーー197ーーーーー{notification}")
            print(f"ーーーーーーーーーーー{tuuti_state}")
            print("🟡すでに通知オンになっている")
            print(f"-----------timerSTOPはP184")
            timer_stop=True
    else:
        tuuti_state=False
        timer_stop=True
        print("!!!!!!!!!!!")

def tuuti(todo):    #通知メソッド
    now = datetime.datetime.now()
    now_format=now.strftime("%m月%d日 %H時%M分")
    show_text = f"現在時刻は[{now_format}]です。お疲れ様でした。"
    text = f"「{todo}」の期限が終了しました。"
    rumps.notification(  # 通知
        todo,  # todo内容
        text,
        show_text
    )


class MenuBar(rumps.App):

    def __init__(self):
        global index_bar,data
        global notification,tuuti_state
        getData(self)
        print(f"アプリの通知設定：",'通知オン' if notification != False else '通知オフ')
        print(f"ーーーーーーーーーーー{tuuti_state}")
        
        hyouzi=check_menubar()
        print("----------------------------------------------")
        print(data)
        print(f"初めに表示するのは:{hyouzi}")
        print("----------------------------------------------")

        check_tuuti()
        if notification==True:
            # tuuti_state=False
            swich(self)

        super(MenuBar, self).__init__(name="メニューバーtodo",title=hyouzi+'×' if notification == False else hyouzi+'⚪︎', icon='icon/icon.png')
        # super(MenuBar, self).__init__(name="メニューバーtodo",menu=['通知オン' if tuuti_state == False else '通知オフ'],title=hyouzi, icon='icon/fois.png')
        print("アプリ起動-no problem")


    # @rumps.clicked('通知オン' if tuuti_state == False else '通知オフ')
    @rumps.clicked("通知")
    def timer(self,_):      
        global tuuti_state,index_bar,notification,data
        
        print(f"ーーーーー1ーーーーーー{notification}")
        print(f"ーーーーー1ーーーーーー{tuuti_state}")
        print("-------P219--------")

        json_data={
                "notification" : not notification
            }   #この形式でデータを保存（json形式に準じて）
        with open('setting.json', 'w') as f:   #書き込み
            json.dump(json_data, f, indent=2, ensure_ascii=False)

        notification = not notification
        print(f"アプリの通知設定：",'通知オン' if notification != False else '通知オフ')
        print(f"ーーーーー2ーーーーーー{notification}")
        print(f"ーーーーー2ーーーーーー{tuuti_state}")
        
        print("-------P232--------")
        swich(self)






if __name__ == "__main__":
    con = sqlite3.connect('todo_list.db')

    con.execute(
        "CREATE TABLE IF NOT EXISTS todo(id integer PRIMARY KEY, todo_data text, todo_deadline datetime, check_data boolean)")
    # # # # ３．テーブルにデータを追加
    con.execute("DELETE FROM todo WHERE id = 1")
    con.execute("DELETE FROM todo WHERE id = 2")
    con.execute("DELETE FROM todo WHERE id = 3")
    con.execute("DELETE FROM todo WHERE id = 4")
    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(4,'4＿課題提出','2023-01-28 01:18',false)")
    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(2,'2＿朝ごはんだよ','2023-01-28 01:09',false)")   
    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(3,'3＿出る時間だよ','2023-01-28 01:10',false)")
    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'1＿起きるよ','2023-01-28 01:08',false)")

    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(4,'4＿課題提出','2023-01-27 15:40',false)")
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(2,'2＿朝ごはんだよ','2023-01-27 15:10',false)")
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(3,'3＿出る時間だよ','2023-01-27 15:30',false)")
    # con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'1＿起きるよ','2023-01-27 15:00',false)")
    con.commit()

    app = MenuBar()
    app.run()