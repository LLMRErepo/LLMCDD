'''
few-shot
CoT: class identification, attribute identification, relation identification (example_uml_few_cot_v5.txt)
turbo
add conclusion in CoT, and add resaoning message based on last step.
change class and attribute identificaiton description
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
    us = readUS("UserStories/g" + projectNo + ".txt")
    ins = "Please generate class diagrams for following user stories.\n"
    exUS = readUsExamples("Prompts/example_us.txt")
    exUML = readUmlExamples("Prompts/example_uml_few_cot_5ex.txt")
    outputFormat = readOutputFormat("Prompts/outputFormat_cot.txt")

    promptEx = []
    for i in range(len(exUML)):
        ex_user = {"role": "user", "content": ins + "User Story:\n" + exUS[i]}
        ex_assistant = {"role": "assistant", "content": exUML[i]}
        promptEx.append(ex_user)
        promptEx.append(ex_assistant)


    for usNo in range(len(us)):
        # if usNo > 10:
        #     break
        # if usNo < 10:
        #     continue
        print("=" * 50)
        context = [{"role": "system",
                    "content": "You are a tool of generating class diagrams with relations for given user stories.\n Here is the output format." + outputFormat + "\n"}
                    ]
        promptIns = [
                     {"role": "user",
                      "content": ins + "User Story:\n" + us[usNo]},
                     ]
        promptInput = context + promptEx + promptIns


        res, com = askGPT(promptInput)
        print("="*20, "result ", str(usNo), "="*20)
        print(res)
        path = "Results/" + scriptNo + "/g" + projectNo + "_v2/"
        resFile = "res_" + str(usNo) + ".txt"
        comFile = "com_" + str(usNo) + ".txt"
        savePreResults(path, resFile, us[0], res)
        savePreCompletion(path, comFile, com)

script = "us2uml_few_cot_5ex"
projects = ["14"] # 13 and 14
for project in projects:
    runByProject(project, script)