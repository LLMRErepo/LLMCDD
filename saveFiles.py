from json import dumps
import os
import csv

def savePreResults(newpath, file, us, result):
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    f = open(newpath+file, 'w')
    # f.write("User Story:\n")
    # f.write(us)
    # f.write("\n" + "="*20 + "Result" + "="*20 + "\n")
    f.write(result)

def savePreCompletion(newpath, file, completion):
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    f = open(newpath+file, 'w')
    f.write(dumps(completion) + "\n")

def saveListToCsv(newpath, file, mylist):
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    with open(newpath+file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(mylist)


def saveDicToCsv(newpath, file, myDict):
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    with open(newpath+file, 'w', newline='') as file:
        writer = csv.writer(file)
        for key, value in myDict.items():
            writer.writerow([key, value])