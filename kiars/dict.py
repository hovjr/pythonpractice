import pandas as pd

Weekly_Calender = {}
# Weekly_Calender['Monday'] = {'Work': "9-5", 'Exercise': '6-7:30'}
# Weekly_Calender['Tuesday'] = {'Dick': '9-5', 'Vagina': '6-7:30'}

Weekly_Calender = {'Monday': ['penis', 'vagina', 23], 'Tuesday': ['bumole', 'tigis', 12]}

# print(Weekly_Calender['Tuesday'][2])
# print(Weekly_Calender.get('Monday'))

# Weekly_Calender['Phone'] = ['555-5555', 'for plug']

# Weekly_Calender.update({'Monday': ''})

# print(Weekly_Calender)

# a = Weekly_Calender.values()
# print(a)

# print(Weekly_Calender.keys())

# for key, values in Weekly_Calender.items():
#     print(values)

test4 = pd.DataFrame(data=Weekly_Calender)

bwed = ['kolonoscopy', 'drugs', 54]

test4['Wednesday'] = bwed

# temp = a.set_index['Monday']

calender_copy = test4
ctest = test4.join(test4, lsuffix=' First week', rsuffix=' Secondweek')

print(ctest)
# print(temp)
