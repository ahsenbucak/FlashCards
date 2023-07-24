from PyQt5 import QtWidgets, uic
from logo import logo_rc
from flashcard_user import User
import menu_page
import about_page

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow,self).__init__()
        uic.loadUi('ui/login_ui.ui',self)
        self.enter_button.clicked.connect(self.create)
        self.about_us_button.clicked.connect(self.about_show)
        self.show()

    def create(self):
        user=User(self.username_line.text())
        user.login()
        self.menu_show(user)

    def menu_show(self,object):
        self.object=object
        self.cams=menu_page.MainWindow(self.object)
        self.cams.show()
        self.close()
        
    def about_show(self):
        self.cams=about_page.AboutWindow()
        self.cams.show()
