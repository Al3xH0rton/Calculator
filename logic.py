from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(313, 461)
        MainWindow.setMinimumSize(QtCore.QSize(313, 461))
        MainWindow.setMaximumSize(QtCore.QSize(313, 461))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.clear_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clear_Button.setGeometry(QtCore.QRect(0, 70, 61, 51))
        self.clear_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.clear_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.clear_Button.setObjectName("clear_Button")

        # Number Buttons
        self.one_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.one_Button.setGeometry(QtCore.QRect(0, 220, 61, 51))
        self.one_Button.setObjectName("one_Button")

        self.two_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.two_Button.setGeometry(QtCore.QRect(60, 220, 61, 51))
        self.two_Button.setObjectName("two_Button")

        self.three_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.three_Button.setGeometry(QtCore.QRect(120, 220, 61, 51))
        self.three_Button.setObjectName("three_Button")

        self.four_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.four_Button.setGeometry(QtCore.QRect(0, 170, 61, 51))
        self.four_Button.setObjectName("four_Button")

        self.five_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.five_Button.setGeometry(QtCore.QRect(60, 170, 61, 51))
        self.five_Button.setObjectName("five_Button")

        self.six_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.six_Button.setGeometry(QtCore.QRect(120, 170, 61, 51))
        self.six_Button.setObjectName("six_Button")

        self.seven_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.seven_Button.setGeometry(QtCore.QRect(0, 120, 61, 51))
        self.seven_Button.setObjectName("seven_Button")

        self.eight_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.eight_Button.setGeometry(QtCore.QRect(60, 120, 61, 51))
        self.eight_Button.setObjectName("eight_Button")

        self.nine_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.nine_Button.setGeometry(QtCore.QRect(120, 120, 61, 51))
        self.nine_Button.setObjectName("nine_Button")

        self.zero_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.zero_Button.setGeometry(QtCore.QRect(60, 270, 61, 51))
        self.zero_Button.setObjectName("zero_Button")

        self.num_Box = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.num_Box.setGeometry(QtCore.QRect(0, 0, 241, 71))
        self.num_Box.setMinimumSize(QtCore.QSize(241, 71))
        self.num_Box.setMaximumSize(QtCore.QSize(241, 71))
        self.num_Box.setObjectName("num_Box")
        self.num_Box.setReadOnly(True)

        # Connect number buttons to the function
        self.one_Button.clicked.connect(lambda: self.update_display("1"))
        self.two_Button.clicked.connect(lambda: self.update_display("2"))
        self.three_Button.clicked.connect(lambda: self.update_display("3"))
        self.four_Button.clicked.connect(lambda: self.update_display("4"))
        self.five_Button.clicked.connect(lambda: self.update_display("5"))
        self.six_Button.clicked.connect(lambda: self.update_display("6"))
        self.seven_Button.clicked.connect(lambda: self.update_display("7"))
        self.eight_Button.clicked.connect(lambda: self.update_display("8"))
        self.nine_Button.clicked.connect(lambda: self.update_display("9"))
        self.zero_Button.clicked.connect(lambda: self.update_display("0"))

        self.clear_Button.clicked.connect(self.clear_display)

        # Additional setup
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update_display(self, value):
        current_text = self.num_Box.text()
        new_text = current_text + value  # Append the number to the current display
        self.num_Box.setText(new_text)

    def clear_display(self):
        self.num_Box.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clear_Button.setText(_translate("MainWindow", "Clear"))
        self.one_Button.setText(_translate("MainWindow", "1"))
        self.two_Button.setText(_translate("MainWindow", "2"))
        self.three_Button.setText(_translate("MainWindow", "3"))
        self.four_Button.setText(_translate("MainWindow", "4"))
        self.five_Button.setText(_translate("MainWindow", "5"))
        self.six_Button.setText(_translate("MainWindow", "6"))
        self.seven_Button.setText(_translate("MainWindow", "7"))
        self.eight_Button.setText(_translate("MainWindow", "8"))
        self.nine_Button.setText(_translate("MainWindow", "9"))
        self.zero_Button.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
