#Error Handling
# It is important to put programs in 'try' to protect users and programmer from serious incidences
# try:
#     a = 20
#     b = 0
#     rs = a/b
#     print(rs)
# except:
#     print('Error occured')
#
# try:
#     a = 20
#     b = 0
#     print('Hello')
#     rs = a/b
#     print(rs)
# except:
#     print('Error occured')
# finally:
#     print('db.close')
       
# try:
#     a = 20
#     b = 0
#     print('Hello')
#     rs = a/b
#     print(rs)
# except Exception as ex:
#     print('Error occured', ex.__class__)
# finally:
#     print('db.close')
       
## or ##
try:
    a = 20
    b = 0
    print('Hello')
    rs = a/b
    print(rs)
except ZeroDivisionError as ex:
    print('Error occured', ex.__class__)
finally:
    print('db.close')