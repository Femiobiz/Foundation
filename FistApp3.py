# 

# Femi1 = [1,2,3,4,5,6,7,8,9,10]
# [print(x+1) for x in Femi]

# factorial = 1
# Enter_number = int(input("insert number"))
# if (Enter_number <0):
#     print('It is not a valid number')
# elif(Enter_number == 0):
#     print(("Factorial of 0 is o"))
# elif(Enter_number == 1):
#     print("Factorial of 1 is 1")
# else:
#     for x in range(1, Enter_number + 1):
#         factorial = factorial * x
#         print(factorial)

# import math

# #Quadratic eqution
# a = 2
# b = 4
# c = 2
# determinant = (b**2) - 4*a*c
# if (determinant < 0):
#     print(('It is a complex root'))
# elif(determinant == 0):
#     x1 = ((-b) + math.sqrt(determinant))/2*a
#     print(x1)
# else:
#     x1 = ((-b) + math.sqrt(determinant))/2*a
#     x2 = ((-b) + math.sqrt(determinant))/2*a 


#Assignment
# Word =  (input('Enter word'))
# Word2 = reversed(Word)
# print(Word2)
# if Word == Word2:
#     print("Word is Palindrone")
# else:
#     print("Word is not palindrone")

###### Assignment Correct #####
# Word1=list((input('Enter word')))
# print(Word1) 
# Word2=Word1.copy()
# Word2.reverse()
# print(str(Word2))
# if Word1==Word2:
#     print("Word is Palindrone")
# else:
#     print("Word is not Palindrone")


##
#Word1 =  (input('Enter word'))
#word3 = Word1.split(" My name is Oluwafemi")
#print(word3)

#Palindrone
# def isPalindrone(Newword):
#     return Newword == Newword[::-1]     

# mywords = str.lower(input('Enter your words'))

# if(isPalindrone(mywords)):
#     print(('It is Palindrone'))
# else:
#     print('Not a palindrne')


#Solution
# words = str.lower(input("Enter word"))
# reverse = words.split('')
# [print(x) for x in reverse]


# words = list((str.lower(input('Enter word'))))
# word5 = words.copy().reverse()
# [print(f'The (words) is not a palindrone')]


############### Set Datatype (Module 1)################
# from pickle import FALSE, TRUE
# myset = {1,2,3,4,5,6,7,8,9}
# print(myset)
# myset.add(10)    ######## to add a single value
# myset.update({11,12,13,14})
# mycopy = myset.copy()
# print(mycopy)
# myset.remove(8)
# print(myset)
# myset.clear()
# print(myset)
# print(mycopy)

########
# from math import pi
# r = float(input("Enter your radius "))
# area_of_circle = pi * r**2
# print(f'The area of the circle with radius {r} is {area_of_circle}')


###### Even number######
t = 0
while (t<= 51):
    print(t)
    t += 2



############## Set Datatype (module 2)###################
# A = {1,2,3,4,5,6,7,8}
# B = {6,7,8,9,10}
# C = {3,4,5}
# print(A.union(B))     ###OR
# print(A|B)

# ####Intercept########
# print(A.intersection(B))  #####OR
# print(A&B)

# ############Differences##############
# print(A.difference(B))         ###OR
# print(B.difference(A))         ##OR
# print(A^B)                     ##OR
# print(B^A)
# ############ NOT Intercept#############
# print(A.symmetric_difference(B))
# print(A.isdisjoint(B))
# print(B)
# print(not(A&B))

# #####subset and superset##########
# print(C.issubset(A))
# print(C.issuperset(A))
# import math
# # [print(sqrt x) for x in A]

########## Area of a Circle #########
import math
# R = float(input("Input radius"))
# print(R)
# pi = float(3.1426)
# Area_circle = pi*(R**2)
# print(Area_circle)
##### or #####
# pi1 = math.pi
# r = float(input('Enter your radius'))
# answer = pi1 * r**2
# print(f'Answe for {r} radius is {answer}')

######Question#####
# setA = {2,6,1,4,9,8,7,3}
# print(sum(setA))
# print(f'Sum of setA is {setA}')
# minV = min(setA)
# maxV = max(setA)
# print(f'minimum value of setA is {minV}')
# print(f'maximum value of setA is {maxV}')
# ## Ordering a set#######
# print(sorted(setA, reverse=True))    ##### Reverse = False is the default

