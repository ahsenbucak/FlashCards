import time
import json
from flashcard_user import User

class Game:
    def __init__(self,obj):
        self.object=obj
        self.true_number=0
        self.attempts_number=0
        self.word_list=self.words()

    def starting_time(self):
        self.start_time=time.time()
        return self.start_time

    def totalTime(self):
        end_time=time.time()
        self.total_time=end_time-self.start_time
        return self.total_time

    def words(self):
        self.level=str(self.object.level)
        with open('data/word.json',"r") as json_file:
            data=json.load(json_file)
            words=[]
            for word in data[self.level]:
                level_words=[]
                level_words.append(word)
                level_words.append(data[self.level][word])
                words.append(level_words)
            return words

        

    def show_words(self):
        if self.true_number==20:
            self.object.level +=1
            self.totalTime()
            self.object.registerUserStat(self.object,self.total_time)
            self.starting_time()
            self.word_list=self.words()
            self.true_number=0
            self.attempts_number=0
        self.nl=self.word_list[self.true_number][0]
        self.en=self.word_list[self.true_number][1]
        return self.nl,self.en,self.true_number
    
    def total_attempt_number(self):
        self.attempts_number +=1
        return self.attempts_number
    
    def true(self):
        self.true_number +=1 

    def false(self):
        self.false_word =self.word_list.pop(self.true_number)
        self.word_list.append(self.false_word)


user1=User("User")
game1=Game(user1)

#Controlling totalTime()
# game1.starting_time()
# time.sleep(3)
# print(game1.totalTime())


#controlling show_words()
# print(game1.words())

#controlling the true()
# game1.true()
# print(game1.show_words())

game1.starting_time()
game1.true()
print(game1.show_words())
game1.false()
game1.total_attempt_number()
print(game1.show_words())
print(game1.word_list)
print(game1.attempts_number)

time.sleep(1)
print(game1.totalTime())

