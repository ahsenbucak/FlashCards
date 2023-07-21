import csv
import json

csv_File_Path="word.csv"
json_File_Path="word.json"

jsonList=[]
with open(csv_File_Path,'r') as csvf:
    reader=csv.reader(csvf)
    for i in reader:
        jsonList.append(i)
jsonDict={}
level=0

for i in range(0,5000,20):
    myDict={}  
    level+=1 
    for j in range(i,i+20):
        myDict[jsonList[j][0]]=jsonList[j][1] 
    jsonDict[level]=myDict
    
  
with open(json_File_Path, 'w') as jsvf:
    jsonString=json.dumps(jsonDict,indent=4,ensure_ascii=False)#I used "ensure_ascii=False" to fix nonEngish alphabet problem
    jsvf.write(jsonString)
  
######Previous Code
# with open(csv_File_Path,'r') as csvf:
#     csvReader=csv.DictReader(csvf)
#     for row in csvReader:
#         jsonlist.append(row)
# with open(json_File_Path,'w') as jsonf:
#     jsonString=json.dumps(jsonlist,indent=4)
#     jsonf.write(jsonString)
    