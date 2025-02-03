# List[]
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data.
# Lists are created using square brackets:[]
# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.
'''
#creating a list of students
'''
fruits=['apple','banana','pineapple','guava','strawberry','apple']
print(fruits)
print(len(fruits))
print(type(fruits))
list1=[1,2,3,'sai',True,0.1]
print(list1)
thislist=list(('apple','banana','pineapple','guava','strawberry'))
print(thislist)
'''

#methods in list
# 1.append()	Adds an element at the end of the list
# 2.clear()	Removes all the elements from the list
# 3.copy()	Returns a copy of the list
# 4.count()	Returns the number of elements with the specified value
# 5.extend()	Add the elements of a list (or any iterable), to the end of the current list
# 6.index()	Returns the index of the first element with the specified value
# 7.insert()	Adds an element at the specified position
# 8.pop()	Removes the element at the specified position
# 9.remove()	Removes the first item with the specified value
# 10.reverse()	Reverses the order of the list
# 11.sort()	Sorts the list

#example of methods in list
# fruits=['apple','banana','pineapple','guava','strawberry','apple']
# cars=['bmw','audi','benz','toyota','honda']
# n=[3,1,4,5,63,17,8,92,10]
# '''
# #1.append
# fruits.append('pineapple')
# print(fruits)
# #2.clear
# fruits.clear()
# print(fruits)
# #3.copy
# fruits1=fruits.copy()
# print(fruits1)
# #4.count
# y=fruits.count('guava')
# print(y)
# #5.extend
# fruits.extend(cars)
# print(fruits)
# #6.index
# i=fruits.index('guava')
# print(i)
# #7.insert
# fruits.insert(0,'strawberry')
# print(fruits)
# #8.pop
# fruits.pop(4)
# print(fruits)
# #9.remove
# fruits.remove('guava')
# print(fruits)
# #10.reverse
# fruits.reverse()
# print(fruits)
# #11.sort
# n.sort()
# print(n)
# '''

# #accessing list elements
# '''
# print(fruits[0])
# print(fruits[4])
# #negative indexing
# print(fruits[-4])
# '''
# # Range of Indexes
# # You can specify a range of indexes by specifying where to start and where to end the range.
# # When specifying a range, the return value will be a new list with the specified items.
# #Note: The search will start at index 1 (included) and end at index 4 (not included).
# '''print(fruits[1:4])'''
# # #This example returns the items from the beginning to, but NOT including, "kiwi":
# '''print(fruits[:5])'''
# # #This example returns the items from "guava" to the end:
# '''print(fruits[3:])'''

# # Range of Negative Indexes
# # Specify negative indexes if you want to start the search from the end of the list:
# #This example returns the items from "banana" (-5) to, but NOT including "strawberry" (-2):
# '''print(fruits[-5:-2])'''

# # Check if Item Exists
# # To determine if a specified item is present in a list use the in keyword:
# '''
# if 'appl' in fruits:
#   print("yes apple is in the list")
# else:
#     print("not present in the ;ist")
# '''

# fruits=['apple','banana','pineapple','guava','strawberry','kiwi']
# #Change Item Value
# #To change the value of a specific item, refer to the index number:  
# ''' 
# fruits[0]='pineapple'
# print(fruits)
# '''

# #Change a Range of Item Values
# #To change the value of items within a specific range, define a list with the new values, 
# #and refer to the range of index numbers where you want to insert the new values:
# '''
# fruits[1:4]=['watermelon','orange','mango']
# print(fruits)
# '''

# #If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# fruits[1:4]=['watermelon','orange','mango','kiwi']
# print(fruits)
fruits=['apple','banana','pineapple','guava','strawberry','apple','kiwi','ornge']
#Insert Items
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
#The insert() method inserts an item at the specified index:
'''
fruits=['apple','banana','pineapple','guava','strawberry','apple']
fruits.insert(2,'blackcurrent')
print(fruits)
'''

#Python - Loop Lists
'''
fruits=['apple','banana','pineapple','guava','strawberry','apple']
for i in fruits:
  print(i)

fruits=['apple','banana','pineapple','guava','strawberry','apple']
for i in range(len(fruits)):
  print(fruits[i])
'''

#Using a While Loop
#You can loop through the list items by using a while loop.
#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
#Remember to increase the index by 1 after each iteration.
'''
i=0
while i < len(fruits):
  print(fruits[i])
  i+=1
'''

#List Comprehension
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#Example:
#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#Without list comprehension you will have to write a for statement with a conditional test inside:
'''
newlist=[]
for x in fruits:
  if 'a' in x:
    newlist.append(x)
print(newlist) 
'''
#With list comprehension you can do all that with only one line of code:
'''
newlist=[x for x in fruits]
print(newlist)

newlist=[x for x in fruits if x!='banana']
print(newlist)

newlist=[x for x in fruits if x!='apple']
print(newlist)
'''

#Iterable
#The iterable can be any iterable object, like a list, tuple, set etc.
'''
newlist=[x for x in range(11,21)]
print(newlist)

newlist=[x for x in range(11) if x%2==0]
print(newlist)


newlist=[x.upper() for x in fruits]
print(newlist)
'''
#Sort List Alphanumerically
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
'''
fruits.sort()
print(fruits)

newlist=[10,21,3,5,22,43,5,7,444,765,9]
newlist.sort()
print(newlist)
'''

#Sort Descending
#To sort descending, use the keyword argument reverse = True:
'''
fruits.sort(reverse=True)
print(fruits)
newlist=[10,21,3,5,22,43,5,7,444,765,9]
newlist.sort(reverse=True)
print(newlist)
'''
#Reverse Order
#What if you want to reverse the order of a list, regardless of the alphabet?
#The reverse() method reverses the current sorting order of the elements.
newlist=[10,21,3,5,22,43,5,7,444,765,9]
#Example
#Reverse the order of the list items:
'''
fruits.reverse()
print(fruits)
'''

#Join Two Lists
#There are several ways to join, or concatenate, two or more lists in Python.
#One of the easiest ways are by using the + operator.
'''
list1=fruits+newlist
print(list1)
'''

