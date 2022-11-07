
# file = open('python.txt', 'w')
# file.write('Hello Python class')
# file.close()

## using try and except statement
# try:
#     file = open('python.txt', 'w')
#     file.write('Hello Python class')
# finally:
#     file.close()

# try:
#     file = open('python.txt', 'a')
#     file.write('\n Welcome to the next topic')

# finally:
#     file.close()

# with open('python.txt', 'a') as file:
#     file.write('\n I love programming\n')
#     file.writelines('\n I also love Nigeria\n')

# with open('python.txt', 'r') as file:
#     rs = file.read(15)
#     print(rs)

# with open('python.txt', 'r') as file:
#     rs = file.read()
# print(rs)

# with open('python.txt', 'r') as file:
#     rs = file.read()
#     for x in rs:
#         print(rs)



# with open('docs\python.doc', 'w') as file:
#     file.writelines('I am a Nigerian')

# flip = open('multiplication.doc', 'w')  
# for i in range(1,10):
#     for j in range(1,10):
#         print(f'{i} x {j} = {i * j}', file = flip, end = '\t')
#     print('*****************')

import os

## To rename a file
# os.rename('multiplication.txt', 'timetable.txt')

## To remove/delete a file
# os.remove('docs/python.doc')

# with open('docs/python.xls', 'w') as file:
#     file.write('Welcome to Machine Learning')

## To create a folder
# os.mkdir('C:/Users/23480/Desktop/femiPyhton')
##or
# os.mkdir('C:\\Users\\23480\\Desktop\\femiPyhton3')

## to list dir
# print((os.listdir('C:')))
# rs = (os.listdir('C:'))
# for x in rs:
#     print(rs)

# os.mkdir('C:\\Users\\23480\\Desktop\\femipyhton4')
# with open('C:\\Users\\23480\\Desktop\\femipyhton4\\Flows.doc', 'w') as file:
#     file.write('Good morning, Oga')

####file.exist####
# import os
# stmt = '''
# I have a pen
# It works well
# Thank you
# '''

# if(os.path.exists('docs')):
#     with open('file2.py', 'w') as f:
#         f.writelines(stmt)
# else:
#     os.mkdir('docs')
#     with open('docs/files.py', 'w') as f:
#         f.writelines(stmt)

#### Seek and Tell in read ####################
# f = open('file2.py', 'r')
# rs = f.read(5)
# print(rs)
# f.seek(4)
# print(f.read(5))
# print(f.tell())
# f.close()

#####Removing a file ###
os.unlink('file2.py')