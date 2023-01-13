import datetime
import time
import rumps


class GetData():
    def getData():
        data=datetime.datetime.now()
        exec_time = datetime.datetime(2023,1,13,17,6,30,0)
        print('現在時刻：' , data)
        print('実行時間：' , exec_time , 'まで待機します。')
        sleep_time = exec_time - data
        time.sleep(sleep_time.total_seconds())

        tuuti()

        print('実行時間になりました！')
        print('現在時刻：' , datetime.datetime.now())
        
        # print(data)
        # return data

def tuuti():
    show_text = f"現在時刻は[{datetime.datetime.now()}]です"
    rumps.notification(     #通知
        "Helloタイトル",#タイトル
        "Hello world",
        show_text,
        # icon="fois.png",
    )

if __name__ == "__main__":
    get = GetData
    get.getData()

    # GetData.getData()