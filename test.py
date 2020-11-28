# -*- coding: utf-8 -*-

import sys
from PySide import QtCore,QtGui

import window

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent,QtCore.Qt.WindowStaysOnTopHint)
        self.ui = window.Ui_MainWindow()
        self.ui.setupUi(self)

        #ドロップ許可
        self.setAcceptDrops(True)

    def dropEvent(self,event):
        #ドラッグされたオブジェクトのドロップ許可がおりた場合の処理     
        mimedata = event.mimeData()
        urllist = mimedata.urls()

        for i in urllist:
            print(i.path())           

    def dragEnterEvent(self,event):
        #ドラッグされたオブジェクトがファイルなら許可する
        mime = event.mimeData()

        if mime.hasUrls() == True:
            event.accept()
        else:
            event.ignore()

def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()