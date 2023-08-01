from PyQt5 import QtWidgets, uic
import login_page
import game_page

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,object):
        self.object=object
        super(MainWindow,self).__init__()
        uic.loadUi('ui/menu_ui.ui',self)
        self.welcome_label.setText("WELCOME  "+self.object.name.upper())
        self.level_label.setText("LEVEL: "+str(self.object.level))
        self.total_time_label.setText("          TOTAL TIME:  "+str(self.object.totalTime))
        self.level_progressbar.setValue(int(self.progress_bar()))
        self.logout_button.clicked.connect(self.login_window_show)
        self.play_button.clicked.connect(self.play_window_show)
        self.show()

    def login_window_show(self):
        self.cams=login_page.LoginWindow()
        self.cams.show()
        self.close()

    def play_window_show(self):
        self.cams=game_page.GameWindow(self.object)
        self.cams.show()
        self.close()

    def progress_bar(self):  
       # print(int(self.object.level)/250*100)
          
        return   int(self.object.level)/250*100
        
    

  