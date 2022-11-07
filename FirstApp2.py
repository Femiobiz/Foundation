#25-07-2022
#List for copy
a = [1,2,3,4,5]
b = [6,7,8]
# to extend
a.extend(b)
print(a)
#copy
result = a.copy()
print(result)

print(a is result)    #compsres object
print(a == result)   #compares content

names = ['Ojo', 'Dada', 'Joshua', 'Tolani', 'Mosun']
for x in names:
    print(x)

#2
names = ['Ojo', 'Dada', 'Joshua', 'Tolani', 'Mosun']
for x in names:
    if (x =='Dada'):
        print(x)
[print(x.upper()) for x in names] 

#3
names = ['Ojo', 'Dada', 'Joshua', 'Tolani', 'Mosun']
for x in names:
    if (x =='Dada'):
        print(x)
[print(x.upper()) for x in names if x== "Dada"]   #use [] for comprehensional expression
#Expression, looping and condition
#  
names = ['Ojo', 'Dada', 'Joshua', 'Tolani', 'Mosun']
for x in names:
    if (x =='Dada'):
        print(x)
[print(len(x)) for x in names] 

#question
Femi = []
Obis = ['Kunle', 'fff', 'Tolu']
Femi.extend(Obis)
print(Femi)
Oluwa = ['you', 'two']
Femi.extend(Oluwa)
print(Femi)

#comprehensional operator
[print(x.upper()) for x in Femi if 'u' in x]

#Control structure
age = int(input('Enter your age'))
if (age >= 18):
    print('You are allowed to VOTE')

# If else
age = int(input('Enter your age'))
if (age >= 18):
    print('You are allowed to VOTE')
else:
    print('Not eligible to VOTE')


Grade = int(input('Enter your score'))
if (Grade >= 75):
    print('A')
elif (Grade >= 65):
    print('B')
elif (Grade >= 55):
    print('C')
elif (Grade >= 45):
    print('D')
else:
    print('E')