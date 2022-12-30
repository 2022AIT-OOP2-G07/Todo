#!/usr/env/bin python
# -*- coding: utf-8 -*-
import rumps
import os


class RumpsTest(rumps.App):
    @rumps.clicked("Hello World")
    def hello_world(self, sender):
        #rumps.alert("Hello World!")
        os.system("osascript -e 'display notification \"こんにちは世界\"'")

    @rumps.clicked("check")
    def check(self, sender):
        # チェックマーク
        sender.state = not sender.state
        sender.title = "On" if sender.state else "Off"

    # @rumps.clicked("open")
    # def check(self, sender):
       # # Todoのページを開かせる(以下の処理は代用)
        # sender.state = not sender.state
        # sender.title = "On" if sender.state else "Off"


if __name__ == "__main__":
    app = RumpsTest("ToDo", title=None, icon=None, menu=[])
    #app.menu["open"].title = u"ToDoを開く"
    app.run()
