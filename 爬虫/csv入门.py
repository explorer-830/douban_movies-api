#with open("csv_data/01.csv","w",encoding="utf-8")as f:
    #f.write("姓名,年龄,性别,爱好\n")
    #f.write("小王,18,男,football\n")
    #f.write("小可,19,男,baseball\n")
    #f.write("小七,21,男,pytho\n")

#with open("csv_data.csv","r",encoding="utf=8") as f:
import csv
from encodings import utf_8

with open("csv_data/02.csv",'w',econding=utf_8) as f:
    csv.DictWriter(f,fieldnames=["姓名","年龄","性别","爱好"])
    


