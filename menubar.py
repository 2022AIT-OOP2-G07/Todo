from datetime import datetime

import rumps


class HelloApp(rumps.App):
    @rumps.clicked("Start Timer!")
    def timer(self, _):
        # 一定時間ごとに処理を実行するタイマー

        count = 0

        # callback関数は引数にTimerオブジェクトをとる
        def counter(t):
            nonlocal count
            count += 1
            print(count)
            if count >= 10:
                # print("Stop Timer!")
                self.notification()
                t.stop()

        # タイマーオブジェクト
        # 一定時間ごとにcallbackを呼び出す
        timer = rumps.Timer(callback=counter, interval=1)
        timer.start()

class GetData():
    def getData():
        data=datetime.datetime.now()
        print(data)
        # return data

if __name__ == "__main__":
    get = GetData()
    get.getData()
    # print(get.getData())
    HelloApp("HelloApp", icon="icon/fois.png", quit_button="終了").run()
