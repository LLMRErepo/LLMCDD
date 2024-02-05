from readFiles import *
from saveFiles import *
import csv

def resultsHandling(project, script, usNo):
    path = "Results/" + script + "/g" + project + "/"
    # allFile = path + "results_g" + project + "_.csv"
    # f = open(allFile, 'w')
    # writer = csv.writer(f)
    allClss = []
    allAtt = []
    allRel = []
    allRes = []

    for i in range(usNo):
        file = path + "res_" + str(i) + ".txt"
        result = readResults(file)
        allRes.append(result[1:-1])
        for j in result:
            # print(j)
            # j = j.replace(";", ",")
            if "Class: " in j:
                classes = j[7:-1].split(";")
                allClss.append(classes)
            if "Attribute: " in j:
                attrs = j[11:-1].split(";")
                allAtt.append(attrs)
            if "Relationship: " in j:
                rel = j[13:-1].split(";")
                allRel.append(rel)

    print(allClss)
    print(allAtt)
    print(allRel)
    print(allRes)

    saveListToCsv(path, "results.csv", allRes)

    return allClss, allAtt, allRel

def classHandling(classes):
    simClasses = []
    for i in range(len(classes)):
        for j in classes[i]:
            j = j.strip()
            j = j.replace(' ', '')
            j = [j]
            if j not in simClasses:
                simClasses.append(j)

    print(simClasses)
    print(len(simClasses))

    return simClasses

def attributeHandling(attrs):
    simAttrs = {}
    for i in range(len(attrs)):
        for pairs in attrs[i]:
            pairs = pairs.strip()
            pairs = pairs.replace(' ', '')
            idx = pairs.find("(")
            key = pairs[:idx]
            value = pairs[idx+1:-1]
            # print(key, value)
            # print(simAttrs)
            if value != 'NA':
                if key not in simAttrs:
                    simAttrs[key] = [value]
                else:
                    checkValues = simAttrs[key]
                    if value not in checkValues:
                        simAttrs[key].append(value)

    print(simAttrs)
    print(len(simAttrs))

    return simAttrs

def relationHandling(rels):
    simRel = {}
    for i in range(len(rels)):
        for pairs in rels[i]:
            pairs = pairs.strip()
            pairs = pairs.replace(' ', '')
            if pairs !='NA':
                idx = pairs.find("(")
                key = pairs[:idx]
                value = pairs[idx + 1:-1]
                # print(key, value)
                if key not in simRel:
                    simRel[key] = [value]
                else:
                    checkValues = simRel[key]
                    if value not in checkValues:
                        simRel[key].append(value)



    print(simRel)
    print(len(simRel))

    return simRel


script = "us2uml_few_cot_v9"
# script = "us2uml_few_regular"
# script = "us2uml_zero_regular"
# projects = ["02","03","04","05","08","10","11","12","13","14","16","17","18","19","21","22","23","24","25","26","27","28"]
# project = "13"
# usNo = 53 # g13
# project = "14"
# usNo = 66 # g14
project = "13_v2"
usNo = 20 # g13_v2
# project = "14_v2"
# usNo = 22 # g14_v2
cls, att, rel = resultsHandling(project, script, usNo)
nondupCls = classHandling(cls)
nondupAtt = attributeHandling(att)
nondupRel = relationHandling(rel)
path = "Results/" + script + "/g" + project + "/"
saveListToCsv(path, "cls.csv", nondupCls)
saveDicToCsv(path, "att.csv", nondupAtt)
saveDicToCsv(path, "rls.csv", nondupRel)
