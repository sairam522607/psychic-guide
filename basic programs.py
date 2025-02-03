#project-1
cart={}
srno=0
while True:
  choice=input("Do you want to add items to cart? (yes/no): ")
  if choice=="yes":
    item=[]
    srno+=1
    pname=input("Enter product name: ")
    item.append(pname)
    qty=int(input("Enter quantity: "))
    item.append(qty)
    price=int(input("Enter price: "))
    item.append(price)
    cart[srno]=item
  else:
    print("----------------------------------------------------")
    print("{:<10} {:<20} {:<10} {:<10} ".format('Sr No','Product','Quantity','Price'))
    print("----------------------------------------------------")
    total=0
    qsum=0
    
    print(cart)
    for i in cart:
      print("{:<10} {:<20} {:<10} {:<10}".format(i,cart[i][0],cart[i][1],cart[i][2]))
      total+=cart[i][1]*cart[i][2]
      qsum+=cart[i][1]
    print("----------------------------------------------------")
    break
print("Total quantity: ",qsum)
print("Total amount: ",total)
print("----------------------------------------------------")
print("Thank you for shopping with us")



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

# print(fruits)
# #If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# fruits[1:4]=['watermelon','orange','mango','kiwi']