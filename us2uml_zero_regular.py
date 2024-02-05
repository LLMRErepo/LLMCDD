'''
few-shot
CoT: class identification, attribute identification, relation identification (umlExamples_2.txt)
turbo
'''

import openai
import configs as cf
from readFiles import *
from saveFiles import *
import time

def askGPT(prompt):
    time.sleep(20)
    openai.api_key = cf.OPENAI_KEY
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages = prompt
    )
    ans = completion.choices[0].message.content+'\n'

    return ans, completion

def runByProject(projectNo, scriptNo):
    us = readUS("UserStories_v2/g" + projectNo + ".txt")
    ins = "Please generate class diagrams for following user stories.\n"
    outputFormat = readOutputFormat("Prompts/outputFormat_regular.txt")

    for usNo in range(len(us)):
        # if usNo > 10:
        #     break
        # if usNo < 10:
        #     continue
        print("=" * 50)
        context = [{"role": "system",
                    "content": "You are a tool of generating class diagrams with relations for given user stories.\n Here is the output format." + outputFormat + "\n"}
                    ]
        promptMsg = [ {"role": "user",
                      "content": ins + "User Story:\n" + us[usNo]},
                     ]
        promptInput = context + promptMsg


        res, com = askGPT(promptInput)
        print("="*20, "result", str(usNo), "="*20)
        print(res)
        path = "Results/" + scriptNo + "/g" + projectNo + "_v2/"
        resFile = "res_" + str(usNo) + ".txt"
        comFile = "com_" + str(usNo) + ".txt"
        savePreResults(path, resFile, us[0], res)
        savePreCompletion(path, comFile, com)

script = "us2uml_zero_regular"
# projects = ["02","03","04","05","08","10","11","12","13","14","16","17","18","19","21","22","23","24","25","26","27","28"]
projects = ["14"]
for project in projects:
    runByProject(project, script)