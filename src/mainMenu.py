# Form implementation generated from reading ui file 'mainMenu.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import min_1_typingTest, min_3_typingTest, min_5_typingTest, page_1_typingTest, page_2_typingTest, page_3_typingTest

class Ui_MainWindow(object):
    def load_content(self, sender, current_window):
        test_map = {
            "min_1_btn": "min_1_typingTest.Ui_MainWindow",
            "min_3_btn": "min_3_typingTest.Ui_MainWindow",
            "min_5_btn": "min_5_typingTest.Ui_MainWindow",
            "page_1_btn": "page_1_typingTest.Ui_MainWindow",
            "page_2_btn": "page_2_typingTest.Ui_MainWindow",
            "page_3_btn": "page_3_typingTest.Ui_MainWindow"
                }
        if sender.objectName() in test_map:
            self.new_window = QtWidgets.QMainWindow()
            self.new_ui = eval(test_map[sender.objectName()])()
            self.new_ui.setupUi(self.new_window)
            self.new_window.show()
            current_window.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1337, 720)
        MainWindow.setMaximumSize(QtCore.QSize(1337, 720))
        MainWindow.setStyleSheet("background-color: #B1B2FF;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 10, 1312, 121))
        self.frame.setStyleSheet("align-item: center;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(541, 0, 289, 121))
        self.label.setStyleSheet("font: 63 48pt \"Bahnschrift SemiBold Condensed\";\n"
"color: white;\n"
"font-weight: bold;")
        self.label.setObjectName("label")
        self.main_container = QtWidgets.QWidget(parent=self.centralwidget)
        self.main_container.setGeometry(QtCore.QRect(10, 120, 1314, 551))
        self.main_container.setStyleSheet("background-color: white;\n"
"\n"
"border-radius: 5px;")
        self.main_container.setObjectName("main_container")
        self.widget_2 = QtWidgets.QWidget(parent=self.main_container)
        self.widget_2.setGeometry(QtCore.QRect(10, 13, 1291, 164))
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.widget_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 0, 1271, 164))
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")
        self.frame_2 = QtWidgets.QFrame(parent=self.main_container)
        self.frame_2.setGeometry(QtCore.QRect(17, 186, 1281, 151))
        self.frame_2.setStyleSheet("background-color: #AAC4FF;\n"
"border-radius: 10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.time_test_label = QtWidgets.QLabel(parent=self.frame_2)
        self.time_test_label.setGeometry(QtCore.QRect(90, 43, 161, 61))
        self.time_test_label.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold\";\n"
"color: white;\n"
"font-weight: bold;\n"
"")
        self.time_test_label.setObjectName("time_test_label")
        self.widget_3 = QtWidgets.QWidget(parent=self.frame_2)
        self.widget_3.setGeometry(QtCore.QRect(318, 23, 231, 101))
        self.widget_3.setStyleSheet("background-color:white;\n"
"border-radius: 5px;\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.line = QtWidgets.QFrame(parent=self.widget_3)
        self.line.setGeometry(QtCore.QRect(0, 0, 231, 16))
        self.line.setStyleSheet("background-color: #94B3FD;\n"
"border-radius: 0px;")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.min_1_btn = QtWidgets.QPushButton(parent=self.widget_3)
        self.min_1_btn.setGeometry(QtCore.QRect(10, 69, 211, 25))
        self.min_1_btn.setStyleSheet("""
        QPushButton{
            background-color: #FFD966;
            font: 11pt \"Bahnschrift\";
            color: black;
        }
        QPushButton:hover {
            background-color: #E0BF5A;
            cursor: pointer;
        }
        QPushButton:pressed {
            background-color: #CCAE52;
            color: white;
            cursor: pointer;
        }
        """)
        self.min_1_btn.setObjectName("min_1_btn")
        self.min_1_label = QtWidgets.QLabel(parent=self.widget_3)
        self.min_1_label.setGeometry(QtCore.QRect(77, 23, 71, 31))
        self.min_1_label.setStyleSheet("font: 18pt \"OCR A Extended\";\n"
"color: black;")
        self.min_1_label.setObjectName("min_1_label")
        self.widget_4 = QtWidgets.QWidget(parent=self.frame_2)
        self.widget_4.setGeometry(QtCore.QRect(669, 24, 231, 101))
        self.widget_4.setStyleSheet("background-color:white;\n"
"border-radius: 5px;\n"
"")
        self.widget_4.setObjectName("widget_4")
        self.line_2 = QtWidgets.QFrame(parent=self.widget_4)
        self.line_2.setGeometry(QtCore.QRect(0, 0, 231, 16))
        self.line_2.setStyleSheet("background-color: #94B3FD;\n"
"border-radius: 0px;")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.min_3_btn = QtWidgets.QPushButton(parent=self.widget_4)
        self.min_3_btn.setGeometry(QtCore.QRect(10, 69, 211, 25))
        self.min_3_btn.setStyleSheet("""
        QPushButton{
            background-color: #FFD966;
            font: 11pt \"Bahnschrift\";
            color: black;
        }
        QPushButton:hover {
            background-color: #E0BF5A;
            cursor: pointer;
        }
        QPushButton:pressed {
            background-color: #CCAE52;
            color: white;
            cursor: pointer;
        }
        """)
        self.min_3_btn.setObjectName("min_3_btn")
        self.min_3_label = QtWidgets.QLabel(parent=self.widget_4)
        self.min_3_label.setGeometry(QtCore.QRect(77, 24, 71, 31))
        self.min_3_label.setStyleSheet("font: 18pt \"OCR A Extended\";\n"
"color: black;")
        self.min_3_label.setObjectName("min_3_label")
        self.widget_5 = QtWidgets.QWidget(parent=self.frame_2)
        self.widget_5.setGeometry(QtCore.QRect(1020, 24, 231, 101))
        self.widget_5.setStyleSheet("background-color:white;\n"
"border-radius: 5px;\n"
"")
        self.widget_5.setObjectName("widget_5")
        self.line_3 = QtWidgets.QFrame(parent=self.widget_5)
        self.line_3.setGeometry(QtCore.QRect(0, 0, 231, 16))
        self.line_3.setStyleSheet("background-color: #94B3FD;\n"
"border-radius: 0px;")
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.min_5_btn = QtWidgets.QPushButton(parent=self.widget_5)
        self.min_5_btn.setGeometry(QtCore.QRect(10, 69, 211, 25))
        self.min_5_btn.setStyleSheet("""
        QPushButton{
            background-color: #FFD966;
            font: 11pt \"Bahnschrift\";
            color: black;
        }
        QPushButton:hover {
            background-color: #E0BF5A;
            cursor: pointer;
        }
        QPushButton:pressed {
            background-color: #CCAE52;
            color: white;
            cursor: pointer;
        }
        """)
        self.min_5_btn.setObjectName("min_5_btn")
        self.min_5_label = QtWidgets.QLabel(parent=self.widget_5)
        self.min_5_label.setGeometry(QtCore.QRect(77, 24, 71, 31))
        self.min_5_label.setStyleSheet("font: 18pt \"OCR A Extended\";\n"
"color: black;")
        self.min_5_label.setObjectName("min_5_label")
        self.frame_3 = QtWidgets.QFrame(parent=self.main_container)
        self.frame_3.setGeometry(QtCore.QRect(20, 375, 1281, 151))
        self.frame_3.setStyleSheet("background-color: #AAC4FF;\n"
"border-radius: 10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.page_test_label = QtWidgets.QLabel(parent=self.frame_3)
        self.page_test_label.setGeometry(QtCore.QRect(90, 43, 161, 61))
        self.page_test_label.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold\";\n"
"color: white;\n"
"font-weight: bold;\n"
"")
        self.page_test_label.setObjectName("page_test_label")
        self.widget_6 = QtWidgets.QWidget(parent=self.frame_3)
        self.widget_6.setGeometry(QtCore.QRect(318, 23, 231, 101))
        self.widget_6.setStyleSheet("background-color:white;\n"
"border-radius: 5px;\n"
"")
        self.widget_6.setObjectName("widget_6")
        self.line_4 = QtWidgets.QFrame(parent=self.widget_6)
        self.line_4.setGeometry(QtCore.QRect(0, 0, 231, 16))
        self.line_4.setStyleSheet("background-color: #94B3FD;\n"
"border-radius: 0px;")
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.page_1_btn = QtWidgets.QPushButton(parent=self.widget_6)
        self.page_1_btn.setGeometry(QtCore.QRect(10, 69, 211, 25))
        self.page_1_btn.setStyleSheet("""
        QPushButton{
            background-color: #FFD966;
            font: 11pt \"Bahnschrift\";
            color: black;
        }
        QPushButton:hover {
            background-color: #E0BF5A;
            cursor: pointer;
        }
        QPushButton:pressed {
            background-color: #CCAE52;
            color: white;
            cursor: pointer;
        }
        """)
        self.page_1_btn.setObjectName("page_1_btn")
        self.page_1_label = QtWidgets.QLabel(parent=self.widget_6)
        self.page_1_label.setGeometry(QtCore.QRect(57, 23, 111, 31))
        self.page_1_label.setStyleSheet("font: 18pt \"OCR A Extended\";\n"
"color: black;")
        self.page_1_label.setObjectName("page_1_label")
        self.widget_7 = QtWidgets.QWidget(parent=self.frame_3)
        self.widget_7.setGeometry(QtCore.QRect(669, 24, 231, 101))
        self.widget_7.setStyleSheet("background-color:white;\n"
"border-radius: 5px;\n"
"")
        self.widget_7.setObjectName("widget_7")
        self.line_5 = QtWidgets.QFrame(parent=self.widget_7)
        self.line_5.setGeometry(QtCore.QRect(0, 0, 231, 16))
        self.line_5.setStyleSheet("background-color: #94B3FD;\n"
"border-radius: 0px;")
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.page_2_btn = QtWidgets.QPushButton(parent=self.widget_7)
        self.page_2_btn.setGeometry(QtCore.QRect(10, 69, 211, 25))
        self.page_2_btn.setStyleSheet("""
        QPushButton{
            background-color: #FFD966;
            font: 11pt \"Bahnschrift\";
            color: black;
        }
        QPushButton:hover {
            background-color: #E0BF5A;
            cursor: pointer;
        }
        QPushButton:pressed {
            background-color: #CCAE52;
            color: white;
            cursor: pointer;
        }
        """)
        self.page_2_btn.setObjectName("page_2_btn")
        self.page_2_label = QtWidgets.QLabel(parent=self.widget_7)
        self.page_2_label.setGeometry(QtCore.QRect(57, 24, 111, 31))
        self.page_2_label.setStyleSheet("font: 18pt \"OCR A Extended\";\n"
"color: black;")
        self.page_2_label.setObjectName("page_2_label")
        self.widget_8 = QtWidgets.QWidget(parent=self.frame_3)
        self.widget_8.setGeometry(QtCore.QRect(1020, 24, 231, 101))
        self.widget_8.setStyleSheet("background-color:white;\n"
"border-radius: 5px;\n"
"")
        self.widget_8.setObjectName("widget_8")
        self.line_6 = QtWidgets.QFrame(parent=self.widget_8)
        self.line_6.setGeometry(QtCore.QRect(0, 0, 231, 16))
        self.line_6.setStyleSheet("background-color: #94B3FD;\n"
"border-radius: 0px;")
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.page_3_btn = QtWidgets.QPushButton(parent=self.widget_8)
        self.page_3_btn.setGeometry(QtCore.QRect(10, 69, 211, 25))
        self.page_3_btn.setStyleSheet("""
        QPushButton{
            background-color: #FFD966;
            font: 11pt \"Bahnschrift\";
            color: black;
        }
        QPushButton:hover {
            background-color: #E0BF5A;
            cursor: pointer;
        }
        QPushButton:pressed {
            background-color: #CCAE52;
            color: white;
            cursor: pointer;
        }
        """)
        self.page_3_btn.setObjectName("page_3_btn")
        self.page_3_label = QtWidgets.QLabel(parent=self.widget_8)
        self.page_3_label.setGeometry(QtCore.QRect(57, 24, 121, 31))
        self.page_3_label.setStyleSheet("font: 18pt \"OCR A Extended\";\n"
"color: black;")
        self.page_3_label.setObjectName("page_3_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1337, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_load_content()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Speed Typing Test"))
        self.label.setText(_translate("MainWindow", "Typing Test"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Bahnschrift\'; font-size:24pt; font-weight:296; color:#000000;\">Want to know how to improve your typing speed ? The first step to learn to type fast and increase your typing speed is to take a test!</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Bahnschrift\'; font-size:24pt; font-weight:296; color:#000000;\">The result of this WPM keyboard test will give both your typing speed and your typing accuracy.</span></p></body></html>"))
        self.time_test_label.setText(_translate("MainWindow", "Timed Test"))
        self.min_1_btn.setText(_translate("MainWindow", "1 minute typing test"))
        self.min_1_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">1:00</p></body></html>"))
        self.min_3_btn.setText(_translate("MainWindow", "3 minute typing test"))
        self.min_3_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">3:00</p></body></html>"))
        self.min_5_btn.setText(_translate("MainWindow", "5 minute typing test"))
        self.min_5_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">5:00</p></body></html>"))
        self.page_test_label.setText(_translate("MainWindow", "Page Test"))
        self.page_1_btn.setText(_translate("MainWindow", "1 Page typing test"))
        self.page_1_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">1 Page</p></body></html>"))
        self.page_2_btn.setText(_translate("MainWindow", "2 Page typing test"))
        self.page_2_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">2 Page</p></body></html>"))
        self.page_3_btn.setText(_translate("MainWindow", "3 Page typing test"))
        self.page_3_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">3 Page</p></body></html>"))

    def btn_load_content(self):
        self.min_1_btn.clicked.connect(lambda: self.load_content(self.min_1_btn, MainWindow))
        self.min_3_btn.clicked.connect(lambda: self.load_content(self.min_3_btn, MainWindow))
        self.min_5_btn.clicked.connect(lambda: self.load_content(self.min_5_btn, MainWindow))
        self.page_1_btn.clicked.connect(lambda: self.load_content(self.page_1_btn, MainWindow))
        self.page_2_btn.clicked.connect(lambda: self.load_content(self.page_2_btn, MainWindow))
        self.page_3_btn.clicked.connect(lambda: self.load_content(self.page_3_btn, MainWindow))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
