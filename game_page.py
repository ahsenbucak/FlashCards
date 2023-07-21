from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer
from flashcard_game import Game
import menu_page

class GameWindow(QtWidgets.QMainWindow):
    def __init__(self,object):
        self.object=object
        self.game=Game(self.object)
        self.game.starting_time()
        super(GameWindow,self).__init__()
        uic.loadUi('ui/play_ui.ui',self)
        self.show()

    def menu_show(self):
        self.cams=menu_page.MainWindow()
        self.passedTime=int(self.game.totalTime())
        self.object.registerUserStat(self.object.level,self.passedTime)
        self.cams.show()
        self.close()

    def starting(self):
        self.word_nl,self.word_en,self.true_num=self.game.show_words()
        self.totalTry_num=self.game.attempts_number
        self.language_label.setText("NEDERLANDS")
        self.word_label.setText(self.word_nl)
        self.true_label.setText(self.true_num)
        self.try_label.setText(str(self.totalTry_num))
        self.level_label.setText("LEVEL"+str(self.object.level))