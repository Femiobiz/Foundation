import re

# ## match confirms if the word or ran
# text = 'nigeria'

# result = re.match('[a-z]', text)
# if result:
#     print('Found')
# else:
#     print('Not found')

# ###
# text = input('Enter your Username')

# result = re.match('[a-z]', text)
# if result:
#     print('Found')
# else:
#     print('Not found')

#######
# text = input('Enter your Username')

# result = re.match('^[A-Fa-f]+', text)
# if result:
#     print(result)
# else:
#     print('Not found')

######
# text = input('Enter your Username')

# result = re.match('Ola?', text)
# if result:
#     print(result)
# else:
#     print('Not found')

####### {}-number of characters
# text = input('Enter your Username')

# result = re.match('^[A-Za-z]{8,12}', text)
# if result:
#     print(result)
# else:
#     print('Not found')

text = input('My username is Michael02')

result = re.search('Michael02', text)
if result:
    print('There is a match :', result)
else:
    print('Not found')