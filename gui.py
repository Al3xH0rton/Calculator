# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


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
        self.inverse_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.inverse_Button.setGeometry(QtCore.QRect(60, 70, 61, 51))
        self.inverse_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.inverse_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.inverse_Button.setObjectName("inverse_Button")
        self.percent_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.percent_Button.setGeometry(QtCore.QRect(120, 70, 61, 51))
        self.percent_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.percent_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.percent_Button.setObjectName("percent_Button")
        self.divide_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.divide_Button.setGeometry(QtCore.QRect(180, 70, 61, 51))
        self.divide_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.divide_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.divide_Button.setObjectName("divide_Button")
        self.eight_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.eight_Button.setGeometry(QtCore.QRect(60, 120, 61, 51))
        self.eight_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.eight_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.eight_Button.setObjectName("eight_Button")
        self.nine_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.nine_Button.setGeometry(QtCore.QRect(120, 120, 61, 51))
        self.nine_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.nine_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.nine_Button.setObjectName("nine_Button")
        self.seven_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.seven_Button.setGeometry(QtCore.QRect(0, 120, 61, 51))
        self.seven_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.seven_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.seven_Button.setObjectName("seven_Button")
        self.multiply_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.multiply_Button.setGeometry(QtCore.QRect(180, 120, 61, 51))
        self.multiply_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.multiply_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.multiply_Button.setObjectName("multiply_Button")
        self.five_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.five_Button.setGeometry(QtCore.QRect(60, 170, 61, 51))
        self.five_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.five_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.five_Button.setObjectName("five_Button")
        self.six_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.six_Button.setGeometry(QtCore.QRect(120, 170, 61, 51))
        self.six_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.six_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.six_Button.setObjectName("six_Button")
        self.four_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.four_Button.setGeometry(QtCore.QRect(0, 170, 61, 51))
        self.four_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.four_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.four_Button.setObjectName("four_Button")
        self.subtract_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.subtract_Button.setGeometry(QtCore.QRect(180, 170, 61, 51))
        self.subtract_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.subtract_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.subtract_Button.setObjectName("subtract_Button")
        self.two_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.two_Button.setGeometry(QtCore.QRect(60, 220, 61, 51))
        self.two_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.two_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.two_Button.setObjectName("two_Button")
        self.three_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.three_Button.setGeometry(QtCore.QRect(120, 220, 61, 51))
        self.three_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.three_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.three_Button.setObjectName("three_Button")
        self.one_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.one_Button.setGeometry(QtCore.QRect(0, 220, 61, 51))
        self.one_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.one_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.one_Button.setObjectName("one_Button")
        self.add_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_Button.setGeometry(QtCore.QRect(180, 220, 61, 51))
        self.add_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.add_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.add_Button.setObjectName("add_Button")
        self.zero_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.zero_Button.setGeometry(QtCore.QRect(60, 270, 61, 51))
        self.zero_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.zero_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.zero_Button.setObjectName("zero_Button")
        self.decimal_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.decimal_Button.setGeometry(QtCore.QRect(120, 270, 61, 51))
        self.decimal_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.decimal_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.decimal_Button.setObjectName("decimal_Button")
        self.calctype_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calctype_Button.setGeometry(QtCore.QRect(0, 270, 61, 51))
        self.calctype_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.calctype_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.calctype_Button.setObjectName("calctype_Button")
        self.equal_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.equal_Button.setGeometry(QtCore.QRect(180, 270, 61, 51))
        self.equal_Button.setMinimumSize(QtCore.QSize(61, 51))
        self.equal_Button.setMaximumSize(QtCore.QSize(61, 51))
        self.equal_Button.setObjectName("equal_Button")
        self.basic_calc_Frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.basic_calc_Frame.setGeometry(QtCore.QRect(0, 0, 241, 321))
        self.basic_calc_Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.basic_calc_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.basic_calc_Frame.setObjectName("basic_calc_Frame")
        self.num_Box = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.num_Box.setGeometry(QtCore.QRect(0, 0, 241, 71))
        self.num_Box.setMinimumSize(QtCore.QSize(241, 71))
        self.num_Box.setMaximumSize(QtCore.QSize(241, 71))
        self.num_Box.setObjectName("num_Box")
        self.num_Box.setReadOnly(True)
        self.pi_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pi_Button.setGeometry(QtCore.QRect(250, 70, 61, 51))
        self.pi_Button.setObjectName("pi_Button")
        self.square_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.square_Button.setGeometry(QtCore.QRect(250, 120, 61, 51))
        self.square_Button.setObjectName("square_Button")
        self.cube_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cube_Button.setGeometry(QtCore.QRect(250, 170, 61, 51))
        self.cube_Button.setObjectName("cube_Button")
        self.root_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.root_Button.setGeometry(QtCore.QRect(250, 220, 61, 51))
        self.root_Button.setObjectName("root_Button")
        self.scientific_calc_Frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.scientific_calc_Frame.setGeometry(QtCore.QRect(250, 70, 61, 251))
        self.scientific_calc_Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.scientific_calc_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.scientific_calc_Frame.setObjectName("scientific_calc_Frame")
        self.basic_calc_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.basic_calc_Button.setGeometry(QtCore.QRect(0, 320, 61, 51))
        self.basic_calc_Button.setObjectName("basic_calc_Button")
        self.scientific_calc_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.scientific_calc_Button.setGeometry(QtCore.QRect(0, 370, 61, 51))
        self.scientific_calc_Button.setObjectName("scientific_calc_Button")
        self.calc_type_Frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.calc_type_Frame.setGeometry(QtCore.QRect(0, 320, 61, 101))
        self.calc_type_Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.calc_type_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.calc_type_Frame.setObjectName("calc_type_Frame")
        self.basic_calc_Button.raise_()
        self.basic_calc_Frame.raise_()
        self.equal_Button.raise_()
        self.clear_Button.raise_()
        self.inverse_Button.raise_()
        self.percent_Button.raise_()
        self.divide_Button.raise_()
        self.eight_Button.raise_()
        self.nine_Button.raise_()
        self.seven_Button.raise_()
        self.multiply_Button.raise_()
        self.five_Button.raise_()
        self.six_Button.raise_()
        self.four_Button.raise_()
        self.subtract_Button.raise_()
        self.two_Button.raise_()
        self.three_Button.raise_()
        self.one_Button.raise_()
        self.add_Button.raise_()
        self.zero_Button.raise_()
        self.decimal_Button.raise_()
        self.calctype_Button.raise_()
        self.num_Box.raise_()
        self.pi_Button.raise_()
        self.square_Button.raise_()
        self.cube_Button.raise_()
        self.root_Button.raise_()
        self.scientific_calc_Frame.raise_()
        self.scientific_calc_Button.raise_()
        self.calc_type_Frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 21))
        self.menubar.setObjectName("menubar")
        self.menuCalculator = QtWidgets.QMenu(parent=self.menubar)
        self.menuCalculator.setObjectName("menuCalculator")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCalculator.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clear_Button.setText(_translate("MainWindow", "Clear"))
        self.inverse_Button.setText(_translate("MainWindow", "+/-"))
        self.percent_Button.setText(_translate("MainWindow", "%"))
        self.divide_Button.setText(_translate("MainWindow", "DIV"))
        self.eight_Button.setText(_translate("MainWindow", "8"))
        self.nine_Button.setText(_translate("MainWindow", "9"))
        self.seven_Button.setText(_translate("MainWindow", "7"))
        self.multiply_Button.setText(_translate("MainWindow", "MULT"))
        self.five_Button.setText(_translate("MainWindow", "5"))
        self.six_Button.setText(_translate("MainWindow", "6"))
        self.four_Button.setText(_translate("MainWindow", "4"))
        self.subtract_Button.setText(_translate("MainWindow", "SUB"))
        self.two_Button.setText(_translate("MainWindow", "2"))
        self.three_Button.setText(_translate("MainWindow", "3"))
        self.one_Button.setText(_translate("MainWindow", "1"))
        self.add_Button.setText(_translate("MainWindow", "ADD"))
        self.zero_Button.setText(_translate("MainWindow", "0"))
        self.decimal_Button.setText(_translate("MainWindow", "."))
        self.calctype_Button.setText(_translate("MainWindow", "CALC"))
        self.equal_Button.setText(_translate("MainWindow", "="))
        self.pi_Button.setText(_translate("MainWindow", "π"))
        self.square_Button.setText(_translate("MainWindow", "x²"))
        self.cube_Button.setText(_translate("MainWindow", "x³"))
        self.root_Button.setText(_translate("MainWindow", "√"))
        self.basic_calc_Button.setText(_translate("MainWindow", "Basic"))
        self.scientific_calc_Button.setText(_translate("MainWindow", "Scientific"))
        self.menuCalculator.setTitle(_translate("MainWindow", "Calculator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())