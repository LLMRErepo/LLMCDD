# LLMCDD
This repository contains experiments conducted in the paper 'LLM-based Class Diagram Derivation from User Stories with Chain-of-Thought Prompting'.

## Abstract
In agile requirements engineering, user stories are the primary means of capturing project requirements. However, deriving conceptual models, such as class diagrams, from user stories requires significant manual effort. This paper explores the potential of leveraging large language models (LLMs) and a tailored prompting technique called chain-of-art (CoT) to automate this task. We conducted a comprehensive preliminary study to investigate different prompting techniques applied to the task of deriving conceptual models from user stories. The study involved comparing LLM-based approaches with guided human extraction and evaluating the effectiveness of CoT prompting in enhancing relationship identification between classes. Our findings demonstrate that LLM-based approaches, particularly when combined with well-crafted few-shot prompts, outperform guided human extraction in identifying classes from user stories. The integration of CoT prompting further improves the comprehensiveness of relationship identification. However, we also identified areas of suboptimal performance through qualitative analysis. This work delves into the reasons behind the identified shortcomings in the LLM-based approach and discusses potential avenues for improvement. The insights gained from this analysis provide valuable guidance for further research in automating the derivation of conceptual models from user stories. The proposed CoT prompting technique offers a promising pathway to automate the derivation of class diagrams in agile projects, reducing the reliance on manual effort. Our study contributes valuable insights and directions for future research in this field.

## Dataset
The user stories for our preliminary study are placed under "/UserStories"
- g13 (Project PP)
- g14 (Project DH)

## Implementation
In this work, we evaluate the LLM-based task of deriving class diagrams from user stories with three prompting techniques.
- Zero-shot prompting (us2uml_zero_regular.py)
- Few-shot prompting (us2uml_few_regular.py)
- CoT prompting (us2uml_few_cot.py)

To evaluate the effectiveness of different interactive input methods employed with CoT prompting, two input templates are implemented.
- CoT one-step prompting (us2uml_few_cot.py)
- CoT multiple-step prompting (us2uml_few_cot_mul.py)

To evaluate the effectiveness of different examples employed with CoT prompting, two example templates are implemented.
- CoT prompting covering six examples (us2uml_few_cot.py)
- CoT prompting covering five examples (us2uml_few_cot_5ex.py)

## Configuration
The prompting is implemented via gpt-turbo-3.5. To run the above scripts, please specify the OPENAI key information under "config.py".
To run the scripts for different projects, please update the project number (13 or 14) at the end of your script.

## Results
Under "/Results", the gold standard and evaluation results are provided.
- /GoldStandard (the gold standard for projects PP and DH)
- Tab PP(g13) in evaluation.xlsx  (one sample LLM-based output for Project PP)
- Tab DH(g14) in evaluation.xlsx (one sample LLM-based output for Project DH)
- evaluation.xlsx (the calculated completeness and validity)
