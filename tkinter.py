import tkinter as tk


def pri():
    print("aaa")


class Top_Menu(tk.Menu):
    def __init__(self, root):
        super().__init__()
        root.config(menu=self)

        self.top = tk.Menu(root)
        self.add_command(label="トップに戻る", command=pri)

        self.search = tk.Menu(root)
        self.add_cascade(label="検索", menu=self.search)

        self.edit = tk.Menu(root)
        self.add_command(label="編集", command=pri)

        self.save = tk.Menu(root)
        self.add_command(label="上書保存", command=pri)

        self.cancel = tk.Menu(root)
        self.add_command(label="取消", command=pri)

        self.help = tk.Menu(root)
        self.add_command(label="ヘルプ", command=pri)


root = tk.Tk()
root.geometry('800x700')

menu = Top_Menu(root)

root.mainloop()
