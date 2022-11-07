############### class ##########
# class Animal:
#     name = 'Dog'
#     sound = 'bark'

# myDog = Animal()
# # print(myDog.name)
# print(myDog.sound)


####Student with ' _init_ '#####
# class Student:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

#     def getName(self):
#         return self.name

#     def getAge(self):
#         return self.age

#     def getsex(self):
#         return self.sex

#     def getRecord(self):
#         rs = []
#         rs.append(self.name)
#         rs.append(self.age)
#         rs.append(self.sex)
#         return rs

#     def deleteRecord(self):    
#         del self.age
#         del self.sex
#         del self.name

#     def ToUpper(self, text):
#         return text.upper()

# std = Student('Olakunle', 37, 'Male')
# print(std.getAge())
# print(std.sex)
# print(std.getRecord())
# print(std.getRecord())


####
# class tailor:

#     def __init__(self, customers_name, customers_age, length, girth):
#         self.customers_name = name
#         self.customers_age = age
#         self.length = length
#         self.girth = girth

#     de
# myname = std.getName()
# print(std.ToUpper(myname))

##### without _init_######
# class Student:
#     def setRecord(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def getName(self):
#         return self.name

#     def getAge(self):
#         return self.age

#     def getsex(self):
#         return self.sex

#     def getRecord(self):
#         rs = []
#         rs.append(self.name)
#         rs.append(self.age)
#         rs.append(self.sex)
#         return rs

#     def deleteRecord(self):    
#         del self.age
#         del self.sex
#         del self.name

#     def ToUpper(self, text):
#         return text.upper()

# std = Student()
# std.setRecord('Oluwafemi', 23, 'Male')
# print(std.getRecord())



######## Class cont'd #####
class Python:

    store = []
    def __init__(self, stdName, stdAge, stdPhone):
        self.studentName = stdName
        self.studentAge = stdAge
        self.studentPhone = stdPhone
        self.store.append(self.studentName)
        self.store.append(self.studentAge)
        self.store.append(self.studentPhone)

    def getRecord (self):
        return self.store

students = Python('Olufemi', 22, '8076885443')

print(getRecord(students))


# ##### Inheritance ###
# class Boy:
#     eyes = 2
#     mouth = 1

#     def __init__(self):
#         self.age = 30

#     def run(self):
#         print('You can run')
    
#     def dance(self):
#         print('You can dance')

#     def getEyes(self):
#         return self.eyes

#     class Girl(Boy):
#         def __init__(self):
#             pass

Girl
        



####### Iteration ######
# class Num:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         if(self.a < 5):
#             b = self.a
#             self.a = self.a + 1
#             return b
#         else:
#             StopIteration

# obj = Num()
# itr =iter(obj)
# print(next(itr))
# print(next(itr))   
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

##### without _init_######
# class Student:
#     def setRecord(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def getName(self):
#         return self.name

#     def getAge(self):
#         return self.age

#     def getsex(self):
#         return self.sex

#     def getRecord(self):
#         rs = []
#         rs.append(self.name)
#         rs.append(self.age)
#         rs.append(self.sex)
#         return rs

#     def deleteRecord(self):    
#         del self.age
#         del self.sex
#         del self.name

#     def ToUpper(self, text):
#         return text.upper()

# std = Student()
# std.setRecord('Oluwafemi', 23, 'Male')
# print(std.getRecord())