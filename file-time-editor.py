from mainui import MainUI

import os
import sys
import tkinter as tk

def main():
    master = tk.Tk()
    master.attributes("-topmost", True)

    master.title("文件时间编辑器")

    app = MainUI(master)
    app.initUI()
    master.resizable(False, False) # 禁止调整窗口大小
    master.update_idletasks() # 强制布局渲染，以保证可以读取窗口大小

    # 窗口位置
    x = (master.winfo_screenwidth() - master.winfo_width()) / 2
    y = (master.winfo_screenheight() - master.winfo_height()) / 2
    master.geometry("+%d+%d" % (x, y))

    # 图标
    if sys.argv[0].endswith('.py'):
        master.iconbitmap('icon.ico')
    else:
        master.iconbitmap(os.path.join(os.path.dirname(sys.executable), 'icon.ico'))
    
    master.mainloop()

if __name__ == "__main__":
    main()