# person = {'name':'Zed','age':39,'height':6*12+2}
# person['name'] = 'Shubh'
# person['age'] += 1
# person['college'] = True
# person['city'] = "Philly"
# person['siblings'] = ['Cory']
# person['siblings'].append('Shubh')
# print(person)

billy = {
    'name':'Billy',
    'grades' : [100,80,67,100,89],
    'attendance':[True,True,True,True,True]
}

sarah = {
    'name': 'Sarah',
    'grades': [0, 99, 0, 100, 0],
    'attendance': [True, False, True, False, True]
}

ben = {
    'name': 'Ben',
    'grades': [60, 82, 71, 92, 100],
    'attendance': [False, False, False, False, False]
}

students= {'1':billy,'2':sarah,'3':ben}

#get number of students
print(len(students))#number of keys

#get student id's
print(students.keys())

print(students.values())

#iterate over students
for k in students:
    print('key',k)

#ger billy's attendance
billy = students['1']
print(billy['attendance'])

#get sarah's grades
sarah = students.get('2')
print(sarah.get('grades'))

#get all key balues of ben
ben  = students.get('3')
items = ben.items()
for key,val in items:
    print(key,val)


#get average student grade for all assignments
grades = []
items = students.items()
print(items)
for key,val in items:
    for g in val['grades']:
        grades.append(g)
print(round(sum(grades) / len(grades)))

grades_concat = []
students.items()
for key,value in items:
    grades_concat += val['grades']

print(round(sum(grades_concat)/len(grades_concat)))


