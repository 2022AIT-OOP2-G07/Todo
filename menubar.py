# 1/29 02:06時点で最新ver

#エラーコード
#ERROR[1]->データベースに登録されている時間データが正しい書式で登録されていない
#ERROR[2]->登録されたtodo名が長いことで通知センターから怒られている？

import datetime
import json
import rumps
import sqlite3
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


def check_tuuti():  #通知設定が可能かどうかチェックし可能であれば設定可能なtodoが格納されているインデックス番号を設定するメソッド
    global index_tuuti,data,flag,timer_stop,reloade,tuuti_state,c,index_bar,notification
    index_tuuti=0

    print("🟢通知 チェック")
    for el in data:
        try:
            kigen_time = datetime.datetime.strptime(el[2], '%Y-%m-%dT%H:%M')
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

    siteizikan_date = datetime.datetime.strptime(siteizikan, '%Y-%m-%dT%H:%M')  # 取り出した期限の時間（siteizikan）は文字列だからdateオブジェクトに変換
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

    app = MenuBar()
    app.run()