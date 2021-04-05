from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from functools import partial
from myUi import Ui_MainWindow
import pyautogui

pyautogui.FAILSAFE = True
import sys, time, PyQt5


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_run.clicked.connect(partial(self.on_click, "run"))
        self.pushButton_pause.clicked.connect(partial(self.on_click, "pause"))
        self.pushButton_abort.clicked.connect(partial(self.on_click, "abort"))

    def on_click(self, functype):
        if functype == "run":
            text = self.plainTextEdit_source.toPlainText()
            # time.sleep(1)
            print(len(text))
            # if text !=None:
            #     for words in text:
            #         pyautogui.write(words, interval=0.25)
        elif functype == "pause":
            print("F")
            self.plainTextEdit_source.insertPlainText("Ggi")
        elif functype == "abort":
            pass
        # print("The function is : " + functype)
        # print(self.pushButton_abort.objectName())
        # print(self.sender())

    def TopMost(self):
        if self.checkBox.isChecked():
            self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
            myWin.show()
        else:
            self.setWindowFlag(Qt.WindowStaysOnTopHint, False)
            myWin.show()
    def test(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainForm()  # 創建對象
    myWin.show()  # 顯示窗口
    sys.exit(app.exec())
