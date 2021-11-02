import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 50)

dataset = pd.read_excel('./data/Data - Survey Monkey Output Edited.xlsx', sheet_name="Edited_Data")

datamod = dataset.copy()
datamod = datamod.drop(columns=['Start Date', 'End Date', 'Email Address', 'First Name', 'Last Name', 'Custom Data 1'])

colstomelt = list(datamod.columns)[0:8]
valuesvar = list(datamod.columns)[8:]
datamelt = datamod.melt(id_vars=colstomelt,
                        value_vars=valuesvar,
                        var_name="Question + Subquestion",
                        value_name="Answer"
                        )

questions_imp = pd.read_excel('./data/Data - Survey Monkey Output Edited.xlsx', sheet_name="Question")

questions = questions_imp.copy()
questions.drop(columns=["Raw Question", "Raw Subquestion"], inplace=True)

datajoined = pd.merge(left=datamelt, right=questions, how="left", on="Question + Subquestion")

datajoined.rename(columns={"Identify which division you work in. - Response": "Division Primary",
                           "Identify which division you work in. - Other (please specify)": "Division Secondary",
                           "Which of the following best describes your position level? - Response": "Position",
                           "Which generation are you apart of? - Response": "Generation",
                           "Please select the gender in which you identify. - Response": "Gender",
                           "Which duration range best aligns with your tenure at your company? - Response": "Tenure",
                           "Which of the following best describes your employment type? - Response": "Employment Type"
                           }, inplace=True)


respondents = datajoined[datajoined["Answer"].notna()]
respondents = respondents.groupby("Question")["Respondent ID"].nunique().reset_index()
respondents.rename(columns={"Respondent ID": "Respondents"}, inplace=True)

mergie = pd.merge(left=datajoined, right=respondents, how="left", on="Question")

print(respondents)

datajoined["Answer"].fillna(0, inplace=True)

print(mergie)
