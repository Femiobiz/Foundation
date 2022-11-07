# import random

# record = {}

# name = input('Enter your name')
# dept = input('Enter your department')
# phone = input('Enter your phone number')
# age = int(input('Enter your age'))

# record.clear()
# studentA = {}
# studentA['name'] = name
# studentA['Department']= dept
# studentA['Phone'] =phone
# studentA['Phone'] = phone
# studentA['Age'] = age

# record = studentA.copy()

record = []

for j in range (3):
    name = input('Enter your name')
    dept = input('Enter your department')
    phone = input('Enter your phone number')
    age = int(input('Enter your age'))
    studentA = {}
    studentA['name'] = name
    studentA['Department']= dept
    studentA['Phone'] =phone
    studentA['Age'] = age
    record.append(studentA)

print(record)

for r in record:
    for x in r.items():
        print(x)
    print('----------Another Record--------------')
