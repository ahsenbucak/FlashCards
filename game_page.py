from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer
from flashcard_game import Game
import menu_page

class GameWindow(QtWidgets.QMainWindow):
    def __init__(self,object):
        self.object=object
        self.game=Game(self.object)
        self.game.starting_time()
        # self.true_button.setEnabled(False)
        # self.false_button.setEnabled(False)
        super(GameWindow,self).__init__()
        uic.loadUi('ui/play_ui.ui',self)
        self.back_button.clicked.connect(self.menu_show)
        self.true_button.clicked.connect(self.true_button_function)
        self.false_button.clicked.connect(self.false_button_fuction)
        self.exit_button.clicked.connect(self.exit)
        self.level_label.setText("LEVEL "+str(self.game.level))
        self.words_level.setProperty('Value', str(self.game.true_number))
        self.timer_
        self.show()

    def menu_show(self):
        self.cams=menu_page.MainWindow(self.object)
        self.passedTime=int(self.game.totalTime())
        self.object.registerUserStat(self.game.level,self.passedTime)
        self.cams.show()
        self.close()

    def starting(self):
        self.word_nl,self.word_en,self.true_num=self.game.show_words()
        self.totalTry_num=self.game.attempts_number
        self.languages.setText("NEDERLANDS")
        self.cards.setStyleSheet("border-color: rgb(170, 85, 0);\nbackground-color:rgb(5, 119, 161);\nborder-style: solid;\nborder-width: 3px;\nborder-radius:50px;")
        self.true_button.setEnabled(False)
        self.false_button.setEnabled(False)
        self.words_level.setProperty('value',self.game.true_number)
        self.words.setText(self.word_nl)
        self.true_score.setText(str(self.true_num))
        self.total_try.setText(str(self.totalTry_num))
        self.level_label.setText("LEVEL"+str(self.game.level))

    def en_word(self,en):
        self.en=en
        self.languages.setText("ENGLISH")
        self.cards.setStyleSheet("border-color: rgb(170, 85, 0);\nbackground-color:rgb(255, 255, 220);\nborder-style: solid;\nborder-width: 3px;\nborder-radius:50px;")
        self.words.setText(self.word_en)
        
    def update(self):
        self.timer_label.setText(str(self.count))
        if self.count==0:
            self.true_button.setEnabled(True)
            self.false_button.setEnabled(True)
            self.timer.stop()
            self.en_word(self.word_en)
        self.count -=1

    def timer_(self):
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
        self.count=3
        self.starting()
    
    def true_button_function(self):
        self.game.true()
        self.game.total_attempt_number()
        self.timer_()
        
    def false_button_fuction(self):
        self.game.false()
        self.game.total_attempt_number()
        self.timer_()

    def exit(self):
        self.passedTime=int(self.game.totalTime())
        self.object.registerUserStat(self.game.level, self.passedTime)
        self.close()