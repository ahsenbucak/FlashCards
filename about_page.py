from PyQt5 import QtWidgets, uic

class AboutWindow(QtWidgets.QDialog):
    def __init__(self):
        super(AboutWindow,self).__init__()
        uic.loadUi('ui/about_ui.ui',self)
        self.ok_button.clicked.connect(self.exit)
        self.show()

    def exit(self):
        self.close()