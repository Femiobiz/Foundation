# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.


# creat a set
thisset = {"apple", "banana", "cherry"}
print(thisset)
print(len(thisset))

# set items - Data types
# String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
print(type(set1))

#A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}
print(set1)