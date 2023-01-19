from datetime import datetime

import rumps


class HelloApp(rumps.App):
    pass

if __name__ == "__main__":
    HelloApp("HelloApp", icon="img/icon/fois.png", quit_button="終了").run()
