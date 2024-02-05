def readInstuction(file):
    f = open(file, "r")
    text = f.read()
    print(text)
    return text

def readOutputFormat(file):
    f = open(file, "r")
    text = f.read()
    return text

def readUS(file):
    f = open(file, "r")
    text = f.readlines()
    return text

def readUsExamples(file):
    f = open(file, "r")
    text = f.readlines()
    print(text)
    return text

def readUsUMLExamples(file):
    f = open(file, "r")
    text = f.readlines()
    allUS = []
    strs = ''
    for i in text:
        if i != '\n':
            strs += i
        else:
            allUS.append(strs)
            strs = ''
    return allUS

def readUmlExamples(file):
    f = open(file, "r")
    lines = f.readlines()
    print(lines)
    results = []
    text = ""
    for i in lines:
        if '<start>' in i:
            text = ""
            continue
        elif '<end>' in i:
            text = '<start>\n' + text + '<end>'
            results.append(text)
            continue
        else:
            text += i
            continue

    print(results)

    return results

def readResults(file):
    f = open(file, "r")
    text = f.readlines()
    return text

