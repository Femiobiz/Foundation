# print('''
# **********************************************************************************************
# Welcome. Kindly enter your details of the student and it will be saved into the database. 
# Thank you.
# **********************************************************************************************
# ''')
# import datetime
# import time

# class records:
#     staffRecord = []
#     staffcount = []
#     def __init__(self, staffName, staffAge, staffPhone):
#         self.staffName = staffName
#         self.staffAge = staffAge
#         self.staffPhone = staffPhone
#         self.staffRecord.append(self.staffName)
#         self.staffRecord.append(self.staffAge)
#         self.staffRecord.append(self.staffPhone)
#         # studentcount = studentcount.count + 1
#     def drecords(self):
#         return self.staffRecord

# staff2=records('Oluwafemi', 23, '08069816608') 
# staff3 = records('Isaiah', 28, '08088445678')
# staff4 = records('Kemi', 28, '08099764622')

# print(staff2.drecords())


################ Testing #################
# sleek =[]
# bingo ={'Name': 'Kunle', 'Position:': 'Librarian', 'College': 'Medicine'}
# banjo = {'Name': 'Segun', 'Position:': 'Assistant Director', 'College': 'Engineering'}
# sleek.append(bingo)
# sleek.append(banjo)
# print(sleek)
# # print(sleek[1])

######################## try ################
import datetime
import time

class records:
    staffRecord = []
    staffcount = 0
    def __init__(self, staffName, staffAge, staffPhone):
        self.staffName = staffName
        self.staffAge = staffAge
        self.staffPhone = staffPhone
        print("Staff Name:", self.staffName)
        print("Staff Age:", self.staffAge)
        print("Staff P.Number:", self.staffPhone)
        self.staffRecord.append(self.staffName)
        self.staffRecord.append(self.staffAge)
        self.staffRecord.append(self.staffPhone)
        # self.studentcount = (self.studentcount.co) + 1
    def snumber(self):
        return self.staffcount
        
    def drecords(self):
        return self.staffRecord

staff2 = records('Oluwafemi', 23, '08069816608') 
staff3 = records('Isaiah', 28, '08088445678')
staff4 = records('Kemi', 28, '08099764622')
staff5 = records('Adeyemi', 43, '09045322233')

print(staff3.drecords())
print(staff2.snumber())



