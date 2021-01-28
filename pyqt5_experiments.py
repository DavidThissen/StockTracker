import sys
from PyQt5.QtWidgets import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Stock Tracker"
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)
        self.statusBar().showMessage("How are you David?")
        self.create_main_menu()
        self.show()


    def create_main_menu(self):
        main_menu = self.menuBar()
        main_menu.setNativeMenuBar(False)
        file_menu = main_menu.addMenu('File')
        edit_menu = main_menu.addMenu('Edit')
        help_menue = main_menu.addMenu('Help')

        quit_button = QAction(f"Quit {self.title}",self)
        quit_button.triggered.connect(self.close)
        quit_button.setShortcut("Ctrl+Q")
        quit_button.setStatusTip("Exit Application(changes are saved)")
        file_menu.addAction(quit_button)

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())
