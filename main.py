from gui import *

def main():
    window = Tk()
    window.title('Calculator')
    window.geometry('313x461')
    window.resizable(False, False)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())