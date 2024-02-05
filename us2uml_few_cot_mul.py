'''
few-shot
CoT: class identification, attribute identification, relation identification (example_uml_few_cot_v3.txt)
turbo
add conclusion in CoT, and add resaoning message based on last step.
add existing class diagram for update
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
    ins = "Please derive or update class diagrams for following user stories.\n"
    exUS = readUsUMLExamples("Prompts/example_us_mul.txt")
    exUML = readUmlExamples("Prompts/example_uml_few_cot_mul.txt")
    outputFormat = readOutputFormat("Prompts/outputFormat_cot_mul.txt")

    # print(exUML)
    # print(len(exUML))
    # print(exUS)
    # print(len(exUS))

    promptEx = []
    for i in range(len(exUML)):
        ex_user = {"role": "user", "content": ins + "User Story:\n" + exUS[i]}
        ex_assistant = {"role": "assistant", "content": exUML[i]}
        promptEx.append(ex_user)
        promptEx.append(ex_assistant)
        existMsg = "Existing Class Diagram Components:\n"
        initalUML = "Class: NA\nAttribute: NA\nRelathionship:NA\n"
        currentMsg = existMsg + initalUML


    for usNo in range(len(us)):
        print("currentMsg\n")
        print(currentMsg)
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
                      "content": ins + "User Story:\n" + us[usNo] + "\n" + currentMsg},
                     ]
        promptInput = context + promptEx + promptIns


        res, com = askGPT(promptInput)
        results = res.split("\n")
        updatedUML = ''
        for i in results:
            if "Class: " in i:
                updatedUML += i + "\n"
            if "Attribute: " in i:
                updatedUML += i + "\n"
            if "Relationship: " in i:
                updatedUML += i + "\n"
        # updatedUML = results[7] + "\n" + results[8] + "\n" + results[9]
        currentMsg = existMsg + updatedUML

        print("="*20, "result ", str(usNo), "="*20)
        print(res)
        path = "Results/" + scriptNo + "/g" + projectNo + "_v2/"
        resFile = "res_" + str(usNo) + ".txt"
        comFile = "com_" + str(usNo) + ".txt"
        savePreResults(path, resFile, us[0], res)
        savePreCompletion(path, comFile, com)

script = "us2uml_few_cot_mul"
projects = ["13"]
for project in projects:
    runByProject(project, script)