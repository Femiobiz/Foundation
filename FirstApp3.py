#Example 1
import random
# rnd = random.randint(1, 20)
# print(rnd)
# A = ['A', 'B','C', 'D', 'E']
# a =['a', 'b', 'c', 'd', 'e']
# nums = [1,2,3,4,5,6,7,8,9]
# chars=['#','?','£','%','&']
# random.shuffle(A)
# random.shuffle(a)
# random.shuffle(nums)
# random.shuffle(chars)
# password = A[0] + a[0] + str(nums[0]) + chars[0]
# print(password)

#Example 2
# import string
# password2 = string.ascii_letters + string.digits + string.punctuation
# newPassword = random.sample(password2,16)
# print("".join(newPassword))
# import string
# def GeneratePassword(length):
#     password2 = string.ascii_letters + string.digits + string.punctuation
#     newPassword = random.sample(password2,length)
#     print("".join(newPassword))

# GeneratePassword(12)

#########Example 3#################
# def GeneratePassword(length):
#     import string
#     password2 = string.ascii_letters + string.digits + string.punctuation
#     newPassword = random.sample(password2,length)
#     print("".join(newPassword))

# GeneratePassword(12)

# ##############Dictionarty Datatype#########################
# student ={}
# print(type(student))

# student = {'Name':'Ojo', 'Age':34, 'isMarried':True, 'Subject':['English', 'Mathematics', 'French', 'Economics']}
# scores = {1:20, 2:90, 3:45}
# print(student)
# print(scores)
# print(student['Subject'])
# for key in student['Subject']:
#     print(key)
# #### OR #####
# print(student.get('Sunject'))

# ###Nested Dictionary####
# employee ={
#     'junior':{'name':'Olufemi', 'age':24, 'status':'active'},
#     'senior':{'name':'Obisesan', 'age':12, 'status':'active'}
# }
# for emp in employee:
#     if emp =='senior':
#         for x in employee[emp].items():
#             print(x)
#         for x in employee[emp].keys():
#             print(x)
#         for x in employee[emp].values():
#             print(x)


# print(employee.items())

# data = {'name': 'Adewole', 'age': 29, 'phone':'08069816608'}
# result ={}.fromkeys(data)
# print(result)   ##Returns 'none as value fr keys imported from data
# result['name']= 'Femi'
# print(result)


########   Looping##########
# even number from 1 -220
# x =2
# while (x<=20):
#     print(x)
#     x+=2

### or##
# lst = ['Ade', 'Toyin', 'Bimbo', 'Tope', 'Ola']
# i = len(lst)-1
# while i >= 0:
#     print(lst[i])
#     i-=1
###### Multiplication table###
# x=y=1

# while (x<=9):
#     X+=1
#     while (y<=9):
#         print(f'{x} x {y} = {x*y}')
#         y+=1
    
    
# for x in range(1,10):
#     for y in range(1,10):
#         print(f'{x} x {y} = {x*y}')
#         print()
# x=1
# while (x<=9):
#     y=1
#     while (y<=9):
#         print(f'{x} x {y} = {x*y}')
#         y= y+1
#     print("XXXXXXXXXXX")
#     x=x+1
##### Three steps
# x=1
# while (x<=9):
#     y=1
#     while (y<=9):
#         z=1
#         while (z<=9):
#             print(f'{x} x {y} x {z} = {x*y*z}')
#             z=z+1
#         print("XXXXXXXXXX")
#         y= y+1
#     print("XXXXXXXXXXX")
#     x=x+1

########## Functions ################
# def multiplications(x,y,z):
#     x=1
#     while (x<=9):
#         y=1
#         while (y<=9):
#             z=1
#             while (z<=9):
#                 print(f'{x} x {y} x {z} = {x*y*z}')
#                 z=z+1
#             print("XXXXXXXXXX")
#             y= y+1
#         print("XXXXXXXXXXX")
#         x=x+1

# multiplications(3, 5, z)
# def greeting():
#     print('Good norning')

####or
# def greeting(name):
#     print(f'Good norning, dear {name}')

# greeting('Femi')

#####anonymous
# def greeting(name = 'Anonymous'):
#     print(f'Good norning, dear {name}')

# greeting()

#######Return
# def square(value):
#     return value * value

# print(square(4))
####or
# def square(value = 1):
#     return f' The square of {value} is {value*value}'

# print(square(12))

###Lambda Expression
# sum = lambda x, y: x+y
# print(sum(3,5))

#######Infinite parameters ########## Mltiple parameter supply###############
# def sum(*values):
#     sum =0
#     for x in values:
#         sum = sum + x
#     return sum

# print(sum(2,4,7,9))


def multiplications(x,y,z):
    x=1
    while (x<=20):
        y=1
        while (y<=20):
            z=1
            while (z<=20):
                print(f'{x} x {y} x {z} = {x*y*z}')
                z=z+1
            print("XXXXXXXXXX")
            y= y+1
        print("XXXXXXXXXXX")
        x=x+1

multiplications(7,7,7)