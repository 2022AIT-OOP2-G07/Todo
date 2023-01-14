import datetime
import time
import rumps


class HelloApp(rumps.App):
    @rumps.clicked("通知オン")
    def reload(self, _):
        getData("2023-1-15 00:46:0.0000")



def getData(siteizikan):
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
    HelloApp("HelloApp", icon="icon/fois.png", quit_button="終了").run()
    
    # get.getData("2023-1-15 00:37:30.0000")

