import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

from write import write_file


# ファイル指定の関数
def filedialog_clicked():
    fTyp = [("", "*")]
    iFile = os.path.abspath(os.path.dirname(__file__))
    iFilePath = filedialog.askopenfilename(filetype = fTyp, initialdir = iFile)
    entry2.set(iFilePath)

# 実行ボタン押下時の実行関数
def conductMain():
    text = ""

    filePath = entry2.get()

    if filePath:
        text += "ファイルパス：" + filePath

    if not text:
        messagebox.showerror("error", "パスの指定がありません。")

    try:
        write_file(filePath)
        messagebox.showinfo("処理完了", "処理が完了しました")
        root.destroy()
    except:
        messagebox.showerror("error", "エラーが生じました")



if __name__ == "__main__":

    # rootの作成
    root = Tk()
    root.title("CopyLight")

    # Frame2の作成
    frame2 = ttk.Frame(root, padding=10)
    frame2.grid(row=2, column=1, sticky=E)

    # 「ファイル参照」ラベルの作成
    IFileLabel = ttk.Label(frame2, text="ファイル参照＞＞", padding=(5, 2))
    IFileLabel.pack(side=LEFT)

    # 「ファイル参照」エントリーの作成
    entry2 = StringVar()
    IFileEntry = ttk.Entry(frame2, textvariable=entry2, width=30)
    IFileEntry.pack(side=LEFT)

    # 「ファイル参照」ボタンの作成
    IFileButton = ttk.Button(frame2, text="参照", command=filedialog_clicked)
    IFileButton.pack(side=LEFT)

    # Frame3の作成
    frame3 = ttk.Frame(root, padding=10)
    frame3.grid(row=5,column=1,sticky=W)

    # 実行ボタンの設置
    button1 = ttk.Button(frame3, text="実行", command=conductMain)
    button1.pack(fill = "x", padx=30, side = "left")

    # キャンセルボタンの設置
    button2 = ttk.Button(frame3, text=("閉じる"), command=quit)
    button2.pack(fill = "x", padx=30, side = "left")

    root.mainloop()