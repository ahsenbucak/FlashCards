import os 
import json
import datetime

class User:
    def __init__(self,name,level=1):
        self.name=name
        self.level=level
        self.totalTime='00:00:00'

    def login(self):
        if not os.path.exists("users/{}.json".format(self.name)):
            myDict={
                "name":self.name,
                "level":self.level,
                "totaltime":self.totalTime,
            }
        with open("user/{}.json".format(self.name),"w") as json_file:
            json.dump(myDict,json_file,indent=4)

        with open("user/{}.json".format(self.name),"r") as json_file:
            data=json.load(json_file)
            self.level=data["level"]
            self.totalTime=data["totaltime"]

    def registerUserStat(self,lastlevel,passedtime):
        my_file=open("user/{}.json".format(self.name),"r")
        data=json.load(my_file)
        my_file.close()
        data["level"]=lastlevel
        self.level=lastlevel
        h,m,s=data["totalTime"].split(":")
        totalseconds=int(h)*3600+int(m)*60+int(s)+passedtime
        self.converted_time=str(datetime.timedelta(seconds=totalseconds))
        data["totalTime"]=self.converted_time
        self.totalTime=self.converted_time
        my_file=open("user/{}.json".format(self.name),"w")
        json.dump(data,my_file,indent=4)
        my_file.close()

       

    def registerUserStat(self):
        pass