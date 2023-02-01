# 1/24 04:17時点で最新ver
# 1/26 21:11時点で最新ver
# 1/28 4:53時点で最新ver
# 1/28 14:53時点で最新ver
# 1/28 15:36時点で最新ver
# 実行可
# 1/29 02:06時点で最新ver

# エラーコード
# ERROR[1]->データベースに登録されている時間データが正しい書式で登録されていない
# ERROR[2]->登録されたtodo名が長いことで通知センターから怒られている？

# エラー対応
# ERROR[1]->データベースに登録されている時間データが正しい書式で登録されていない
# ERROR[2]->登録されたtodo名が長いことで通知センターから怒られている？
# 1/29 02:06時点で最新ver

# エラーコード
# ERROR[1]->データベースに登録されている時間データが正しい書式で登録されていない
# ERROR[2]->登録されたtodo名が長いことで通知センターから怒られている？

import datetime
import json
import rumps
import sqlite3
c = 0
k = 0

# １．DB接続。ファイルがなければ作成する
con = sqlite3.connect('todo_list.db')
json_file = open('setting.json', 'r')
notification_flag = json.load(json_file)
notification = notification_flag["notification"]

index_bar = 0
index_tuuti = 0
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
con = sqlite3.connect('todo_list.db')  # データベースに接続
cur = con.execute(
    "select * from todo where todo_deadline <> 1 order by todo_deadline")
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


def getData(self):
    global data, reloade, tuuti_state, notification, c, app_flag

    try:
        con = sqlite3.connect('todo_list.db')  # データベースに接続
        cur = con.execute(
            "select * from todo where todo_deadline <> 1 order by todo_deadline")  # 昇順にデータを取り出し
        z = cur.fetchall()
    except Exception:
        print("データベースが存在しません\n先にWEBアプリの方からデータベースの作成をしてください(大夢がこのアプリからもtodoを登録できる様にする予定だからできる様になればこの様なことがなくなる)")
        sys.exit()

    if reloade._status:
        # 通知するものがない場合や通知設定がなされてない場合に表示するデータ待機中の表示
        print(f"-> getData{reloade._status}--スレッド数：{c}個")

    if data != z and app_flag != False:
        print("------------------------------------------------------")
        print("⭐️データが更新されました⭐️")
        print("------------------------------------------------------")
        tuuti_state = False
        data = z
        hyouzi = check_menubar()
        check_tuuti()
        app.title = hyouzi+'×' if notification != True else hyouzi+'⚪︎'

        if reloade._status == True:
            c -= 1
            reloade.stop()

        if notification == True and flag == True:
            swich(self)
        else:

            if reloade._status == False:
                c += 1
                reloade.start()

    else:
        data = z

    cur.close()
    con.close()


def check_menubar():  # メニューバーに表示する内容を判断し表示するtodoがあればそのインデックス番号を設定するメソッド
    global index_bar, data, flag
    index_bar = 0
    print("🟢menuBar チェック")
    for el in data:
        if el[3] == 0:
            print(f"•{el[1]}ー{el[3]}:メニューバー表示⭕️")
            break
        else:
            print(f"•{el[1]}ー{el[3]}:メニューバー表示❌")
            index_bar += 1
# tuuti_state = notification
import sys


c=0
k=0
index_bar = 0
index_tuuti = 0
flag = True
tuuti_state=None
data=[]
timer_stop=False
app_flag=False

try:
    json_file = open('setting.json', 'r')
    notification_flag = json.load(json_file)
    notification = notification_flag["notification"]
except Exception:
    json_data={
                "notification" : False
            }
    with open('setting.json', 'w') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)   #設定情報をJSONファイル(setting.json)に記録
    notification = False    #設定情報がなかった場合に初期値としてFalseを代入(通知オフ)


def getData(self):
    global data, reloade, tuuti_state, notification, c, app_flag

def getData(self):
    global data,reloade,tuuti_state,notification,c,app_flag

    try:
        con = sqlite3.connect('todo_list.db')  # データベースに接続
        cur = con.execute("select * from todo where todo_deadline <> 1 order by todo_deadline")  # 昇順にデータを取り出し
        z=cur.fetchall()
    except Exception:
        print("データベースが存在しません\n先にWEBアプリの方からデータベースの作成をしてください(大夢がこのアプリからもtodoを登録できる様にする予定だからできる様になればこの様なことがなくなる)")
        sys.exit()
    
    if reloade._status: print(f"-> getData{reloade._status}--スレッド数：{c}個")    #通知するものがない場合や通知設定がなされてない場合に表示するデータ待機中の表示

    if data!= z and app_flag!=False:
        print("------------------------------------------------------")
        print("⭐️データが更新されました⭐️")
        print("------------------------------------------------------")
        tuuti_state=False
        data = z
        hyouzi=check_menubar()
        check_tuuti()
        app.title = hyouzi+'×' if notification != True else hyouzi+'⚪︎'

        if reloade._status == True:
            c-=1
            reloade.stop()
        
        if notification == True and flag == True:
            swich(self)
        else:
            
            if reloade._status == False:
                c+=1
                reloade.start()
        
    else:
        data = z
    
    cur.close()
    con.close()

def check_menubar():    #メニューバーに表示する内容を判断し表示するtodoがあればそのインデックス番号を設定するメソッド
    global index_bar,data,flag
    index_bar=0
    print("🟢menuBar チェック")
    for el in data:
            if el[3]==0:
                print(f"•{el[1]}ー{el[3]}:メニューバー表示⭕️")
                break
            else:
                print(f"•{el[1]}ー{el[3]}:メニューバー表示❌")
                index_bar+=1
    
    if index_bar<len(data):
        print(f"メニューバーの表示は「{data[index_bar][1]}(index:{index_bar})」に設定します")
        print("------------------------------------------------------")
        return data[index_bar][1]
    else:
        print("すべて実行済みです")
        print("------------------------------------------------------")
        flag=False
        return "すべて実行済みです"


    if index_bar < len(data):
        print(f"メニューバーの表示は「{data[index_bar][1]}(index:{index_bar})」に設定します")
        print("------------------------------------------------------")
        return data[index_bar][1]
    else:
        print("すべて実行済みです")
        print("------------------------------------------------------")
        flag = False
        return "すべて実行済みです"


def check_tuuti():  # 通知設定が可能かどうかチェックし可能であれば設定可能なtodoが格納されているインデックス番号を設定するメソッド
    global index_tuuti, data, flag, timer_stop, reloade, tuuti_state, c, index_bar, notification
    index_tuuti = 0

    print("🟢通知 チェック")
    for el in data:
        try:
            kigen_time = datetime.datetime.strptime(el[2], '%Y-%m-%dT%H:%M')
            now = datetime.datetime.now()
        except Exception:
            print("ERROR[1]->->-> 🚨dateオブジェクトに変換中に問題が発生しました🚨 <-<-<-")
            break
            flag = False

        if kigen_time > now and el[3] == 0:
            print(f"•{el[1]}ー{el[2]}ー{el[3]}:通知設定可能⭕️")
            break
        else:
            print(f"•{el[1]}ー{el[2]}ー{el[3]}:通知設定不可能❌")
            index_tuuti += 1

    if index_tuuti < len(data):  # 通知設定可能であるtodoが一つでもある場合
        print(f"通知は「{data[index_tuuti][1]}(index:{index_tuuti})」に設定します")
        # app.title=data[index_bar][1]+'×' if notification == False else data[index_bar][1]+'⚪︎'
        print(
            f"--> メニューバー設定[2]：{data[index_bar][1]+'×' if notification == False else data[index_bar][1]+'⚪︎'}")
        flag = True
        timer_stop = False
        print("------------------------------------------------------")
        # return data[index_bar][1]
    else:  # 通知設定可能なtodoが一つもない場合
        print(f"すべて通知不可です(index:{index_tuuti})")
        flag = False
        timer_stop = True

        if reloade._status == False:
            c += 1
            print("------------------------------------------------------[2]")
            reloade.start()

        print("------------------------------------------------------")
        return "すべて実行済みです"


def trigar(t):  # 通知が実行されている時に毎秒実行されるメソッド
    global index_bar, index_tuuti
    global flag, data, tuuti_state, timer_stop, reloade, c, k, timer

    getData(timer)

    # print(f"trigar:{timer._status}--スレッド数：{k}個")
    print(f"trigar:{timer._status}")
    if timer_stop:
        print(f"t.statue:{timer._status}")
        if timer._status == True:
            print("ここだよ154")
            k = k-1
            timer.stop()
        timer_stop = False
        tuuti_state = False
        print("--通知をオフにします--")

        if reloade._status == False:
            c += 1
            reloade.start()
        return
    else:
        if reloade._status == True:
            c -= 1
            reloade.stop()

    # [(1, 'ご飯を食べる', '2023-01-24 02:45', 0)]　->時間を取り出し
    siteizikan = data[index_tuuti][2]
    todo = data[index_tuuti][1]  # todo内容の取り出し

    # 取り出した期限の時間（siteizikan）は文字列だからdateオブジェクトに変換
    siteizikan_date = datetime.datetime.strptime(siteizikan, '%Y-%m-%dT%H:%M')
    # dateオブジェクトに変換したsiteizikan_dateを"%Y-%m-%d %H:%M"にフォーマット
    siteizikan_format = siteizikan_date.strftime("%Y-%m-%d %H:%M")
    now = datetime.datetime.now()
    now_format = now.strftime("%Y-%m-%d %H:%M")

    print(f"期限:{siteizikan_format}")
    print(f"現在:{now_format}")

    if siteizikan_format == now_format:

        try:
            print(f"{todo}の時間だよ！")
            print('現在時刻：', datetime.datetime.now())
            tuuti(todo)
            try:
                next_todo = data[index_tuuti+1][1]
                print("-----------------------------------------------------")
                print(f"次の予定は[{next_todo}]です(index:{index_bar+1})")
                print("-----------------------------------------------------")
            except:
                print("-----------------------------------------------------")
                print("🟡次の予定はありません")
                print("-----------------------------------------------------")
                if timer._status == True:
                    k = k-1
                    print("ここだよ199")
                    timer.stop

                tuuti_state = False

                if reloade._status == False:
                    c += 1
                    reloade.start()

        except Exception:
            print("ERROR[2]->->-> 🚨通知関数を呼び出せませんでした🚨 <-<-<-")
        check_tuuti()


reloade = rumps.Timer(callback=getData, interval=1)
timer = rumps.Timer(callback=trigar, interval=1)


def swich(self):
    global tuuti_state, timer_stop, reloade, c, k, timer

    print("ここかな217")

    hyouzi = check_menubar()
    if flag == True:
        self.title = data[index_bar][1] + \
            '×' if notification != True else data[index_bar][1]+'⚪︎'
    else:
        self.title = hyouzi+'×' if notification != True else hyouzi+'⚪︎'

    if notification == True:  # 通知設定がなされているか
        if tuuti_state != True:  # 通知が実行されているかどうか
            if flag != False:  # 通知するtodoがあるかどうか
                if timer._status == False:
                    k += 1
                    timer.start()
                print("--> 通知をオンにしました")
                tuuti_state = True
            else:
                print("-----------------------------------------------------")
                print("🟡すべて期限が過ぎています")
                print("-----------------------------------------------------")
                if reloade._status == False:
                    c += 1
                    reloade.start()
        else:
            print("-----------------------------------------------------")
            print("🟡すでに通知オンになっている")
            print(
                "-----------------------------------------------------{\n\n}")
            timer_stop = True
    else:
        tuuti_state = False
        timer_stop = True


def tuuti(todo):  # 通知メソッド
    now = datetime.datetime.now()
    now_format = now.strftime("%m月%d日 %H時%M分")
    show_text = f"現在時刻は[{now_format}]です。お疲れ様でした。"
    text = f"「{todo}」の期限が終了しました。"
    rumps.notification(  # rumpsの通知メソッド
        todo,  # todo内容
        text,
        show_text
    )

def check_tuuti():  #通知設定が可能かどうかチェックし可能であれば設定可能なtodoが格納されているインデックス番号を設定するメソッド
    global index_tuuti,data,flag,timer_stop,reloade,tuuti_state,c,index_bar,notification
    index_tuuti=0

    print("🟢通知 チェック")
    for el in data:
        try:
            kigen_time = datetime.datetime.strptime(el[2], '%Y-%m-%d %H:%M')
            now = datetime.datetime.now()
        except Exception:
            print("ERROR[1]->->-> 🚨dateオブジェクトに変換中に問題が発生しました🚨 <-<-<-")
            break
            flag=False

        if kigen_time > now and el[3]==0:
            print(f"•{el[1]}ー{el[2]}ー{el[3]}:通知設定可能⭕️")
            break
        else:
            print(f"•{el[1]}ー{el[2]}ー{el[3]}:通知設定不可能❌")
            index_tuuti+=1
    
    if index_tuuti<len(data):   #通知設定可能であるtodoが一つでもある場合
        print(f"通知は「{data[index_tuuti][1]}(index:{index_tuuti})」に設定します")
        # app.title=data[index_bar][1]+'×' if notification == False else data[index_bar][1]+'⚪︎'
        print(f"--> メニューバー設定[2]：{data[index_bar][1]+'×' if notification == False else data[index_bar][1]+'⚪︎'}")
        flag=True
        timer_stop=False
        print("------------------------------------------------------")
        # return data[index_bar][1]
    else:   #通知設定可能なtodoが一つもない場合
        print(f"すべて通知不可です(index:{index_tuuti})")
        flag=False
        timer_stop=True
        
        if reloade._status == False:
            c+=1
            print("------------------------------------------------------[2]")
            reloade.start()
        
        print("------------------------------------------------------")
        return "すべて実行済みです"

def trigar(t):  #通知が実行されている時に毎秒実行されるメソッド
    global index_bar,index_tuuti
    global flag,data,tuuti_state,timer_stop,reloade,c,k,timer
    
    getData(timer)

    # print(f"trigar:{timer._status}--スレッド数：{k}個")
    print(f"trigar:{timer._status}")
    if timer_stop:
        print(f"t.statue:{timer._status}")
        if timer._status == True:
            print("ここだよ154")
            k=k-1
            timer.stop()
        timer_stop=False
        tuuti_state = False
        print("--通知をオフにします--")
        
        if reloade._status == False:
            c+=1
            reloade.start()
        return
    else:
        if reloade._status == True:
            c-=1
            reloade.stop()
    
    siteizikan = data[index_tuuti][2]  # [(1, 'ご飯を食べる', '2023-01-24 02:45', 0)]　->時間を取り出し
    todo = data[index_tuuti][1]  # todo内容の取り出し

    siteizikan_date = datetime.datetime.strptime(siteizikan, '%Y-%m-%d %H:%M')  # 取り出した期限の時間（siteizikan）は文字列だからdateオブジェクトに変換
    siteizikan_format=siteizikan_date.strftime("%Y-%m-%d %H:%M")    #dateオブジェクトに変換したsiteizikan_dateを"%Y-%m-%d %H:%M"にフォーマット
    now = datetime.datetime.now()
    now_format=now.strftime("%Y-%m-%d %H:%M")
    
    
    print(f"期限:{siteizikan_format}")
    print(f"現在:{now_format}")
    
    if siteizikan_format == now_format:
        
        try:
            print(f"{todo}の時間だよ！")
            print('現在時刻：', datetime.datetime.now())
            tuuti(todo)
            try:
                next_todo = data[index_tuuti+1][1]
                print("-----------------------------------------------------")
                print(f"次の予定は[{next_todo}]です(index:{index_bar+1})")
                print("-----------------------------------------------------")
            except:
                print("-----------------------------------------------------")
                print("🟡次の予定はありません")
                print("-----------------------------------------------------")
                if timer._status == True:
                    k=k-1
                    print("ここだよ199")
                    timer.stop
                    
                tuuti_state = False
                
                if reloade._status == False:
                    c+=1
                    reloade.start()
            
        except Exception:
            print("ERROR[2]->->-> 🚨通知関数を呼び出せませんでした🚨 <-<-<-")
        check_tuuti()
                    
reloade = rumps.Timer(callback=getData, interval=1)
timer = rumps.Timer(callback=trigar, interval=1)

def swich(self):
    global tuuti_state,timer_stop,reloade,c,k,timer
    
    print("ここかな217")
    

    hyouzi=check_menubar()
    if flag==True:
        self.title = data[index_bar][1]+'×' if notification != True else data[index_bar][1]+'⚪︎'
    else:
        self.title = hyouzi+'×' if notification != True else hyouzi+'⚪︎'

    if notification == True:    #通知設定がなされているか
        if tuuti_state!=True:   #通知が実行されているかどうか
            if flag != False:   #通知するtodoがあるかどうか
                if timer._status == False:
                    k+=1
                    timer.start()
                print("--> 通知をオンにしました")
                tuuti_state=True
            else:
                print("-----------------------------------------------------")
                print("🟡すべて期限が過ぎています")
                print("-----------------------------------------------------")
                if reloade._status == False:
                    c+=1
                    reloade.start()
        else:
            print("-----------------------------------------------------")
            print("🟡すでに通知オンになっている")
            print("-----------------------------------------------------{\n\n}")
            timer_stop=True
    else:
        tuuti_state=False
        timer_stop=True

def tuuti(todo):    #通知メソッド
    now = datetime.datetime.now()
    now_format=now.strftime("%m月%d日 %H時%M分")
    show_text = f"現在時刻は[{now_format}]です。お疲れ様でした。"
    text = f"「{todo}」の期限が終了しました。"
    rumps.notification(  # rumpsの通知メソッド
        todo,  # todo内容
        text,
        show_text
    )


class MenuBar(rumps.App):

    def __init__(self):
        global data, notification, tuuti_state, app_flag

        getData(self)
        print("------------------------------------------------------")
        print(f"---> アプリの通知設定[起動時]：",
              '通知オン' if notification != False else '通知オフ')
        print("------------------------------------------------------")
        hyouzi = check_menubar()
        check_tuuti()
        if notification == True:
            swich(self)

        super(MenuBar, self).__init__(name="メニューバーtodo", title=hyouzi +
                                      '×' if notification == False else hyouzi+'⚪︎', icon='static/img/icon/icon.png')
        print("\n|\n|\n🟥チェック完了\n|\n|\nアプリ起動-no problem\n|\n|")
        app_flag = True

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
    def task()
        # 予定を表示
        task = []
        for doc in cur:
            task.append(doc[1])
            self.menu = task
            print(task)
            self.menu[task[0]].add("削除")
            del task[0]

    @rumps.clicked("通知")
    def timer(self, _):
        global tuuti_state, notification

        json_data = {
            "notification": not notification
        }
        with open('setting.json', 'w') as f:
            # 設定情報をJSONファイル(setting.json)に記録
            json.dump(json_data, f, indent=2, ensure_ascii=False)

        notification = not notification
        print(f"アプリの通知設定[変更]：", '通知オン' if notification != False else '通知オフ')
        swich(self)

    # Webページを開く
    @rumps.clicked("Webを開く")
    def Web(self, _):
        webbrowser.open("http://127.0.0.1:5000")
        global index_bar,data
        global notification,tuuti_state
        global data,notification,tuuti_state
        global data,notification,tuuti_state,app_flag

        getData(self)
        print("------------------------------------------------------")
        print(f"---> アプリの通知設定[起動時]：",'通知オン' if notification != False else '通知オフ')
        print("------------------------------------------------------")
        hyouzi=check_menubar()
        check_tuuti()
        if notification==True:
            swich(self)

        super(MenuBar, self).__init__(name="メニューバーtodo",title=hyouzi+'×' if notification == False else hyouzi+'⚪︎', icon='static/img/icon/icon.png')
        print("\n|\n|\n🟥チェック完了\n|\n|\nアプリ起動-no problem\n|\n|")
        app_flag=True


    @rumps.clicked("通知")
    def timer(self,_):      
        global tuuti_state,notification

        json_data={
                "notification" : not notification
            }
        with open('setting.json', 'w') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)   #設定情報をJSONファイル(setting.json)に記録
        
        notification = not notification
        print(f"アプリの通知設定[変更]：",'通知オン' if notification != False else '通知オフ')
        swich(self)



if __name__ == "__main__":

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
    con.execute("DELETE FROM todo WHERE id = 2")
    con.execute("DELETE FROM todo WHERE id = 3")
    con.execute("DELETE FROM todo WHERE id = 4")

    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(4,'4＿課題提出','2023-01-28 01:18',false)")
    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(2,'2＿朝ごはんだよ','2023-01-28 01:09',false)")   
    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(3,'3＿出る時間だよ','2023-01-28 01:10',false)")
    con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'1＿起きるよ','2023-01-28 01:08',false)")

    con.commit()
    #ここまでコメントアウトしてください
    
    app = MenuBar()
    app.run()
@rumps.clicked("Hello World")
def hello_world(sender):
    rumps.alert("Hello World")


if __name__ == "__main__":
    app = rumps.App("Rumps Test", title=None, icon="img/icon/icon.png",
                    quit_button="終了").run()
    # HelloApp("HelloApp", icon="img/icon/icon.png", quit_button="終了").run()
    app.run()
