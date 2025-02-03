## program to find whether a number is prime or not

'''
n=1
e=int(input("enter any number:"))
c=0
while(n<=e):
  if(e%n==0):
    c+=1
  n+=1
if(c==2):
  print(e,"is a prime number")
else:
  print(e,"is not a prime number,no of factors are:",c)  
  '''
'''  
n=1
e=int(input("enter any number:"))
c=0
while(n<=e):
   if(e%n==0):
      c=c+1
   n=n+1  
if(c==2):
  print(e,"is a prime number")
else:
  print(e,"is not a prime number,no of factors are:",c)  

  n=1
e=int(input("enter any nummber:"))
c=0
while(n<=e):
  if(e%n==0):
    c=c+1
  n+=1
if(c>2):
  print(e,"is not prime number and no of factors are:",c)  
else:
  print(e,"is a prime number")  

n=1
e=int(input("enter any number :"))
c=0
while(n<=e):
  if(e%n==0):
    c+=1
  n+=1
if(c==2):
  print(e,"is a prime number")
else:
  print(e,"is not a prime number and the no of factors are",c)  
  ''' 
    
## program to find the grade in exams
'''
s1=int(input("enter the marks obtained in python:"))
s2=int(input("enter the marks obtained in java:"))
s3=int(input("enter the marks obtained in FDS: "))
s4=int(input("enter the marks obtained in DC:"))
s5=int(input("enter the marks obtained in DS:"))
total=s1+s2+s3+s4+s5
avg=total/5
print(avg)
if(s1<24 or s2<24 or s3<24 or s4<24 or s5<24):
  print("fail")
elif(30<avg<40):
  print("E grade")
elif(40<avg<50):
  print('D grade')
elif(50<avg<55):
  print("C grade")
elif(55<avg<65):
  print("B grade")
elif(65<avg<70):
  print("A grade")
elif(70<avg<=75):
  print("A+ grade") 
else:
  print("enter the correct marks")
'''
## program to find the course and fees

'''
cname=input("enter the course name:")
sname=input("enter the student name:")
cfees=int(input("enter the course fee:"))
if(cname=="java"):
  cfees=cfees+2000
  print("fees for",cname,"course is",cfees)
else:
  print("fees for",cname,"course is",cfees)
'''
## program to print a message multiple times using while loop
'''
message=input("enter the message:")
r=int(input("enter the range:"))
s=1
while(s<=r):
  print(message+"\n")
  s=s+1
 '''
 ## program to print numbers using while loop
'''
n=1
e=int(input("enter the number upto where numbers has to be printed:"))
while(n<=e):
  print(n)
  n=n+1
    
n=0
e=int(input("enter the range:"))
while(n<=e):
  if(n%2==0):
    print(n)
  n+=1  

n=0
e=int(input("enter the range:"))
while(n<=e):
  if(n%2!=0):
    print(n)
  n+=1  
'''
## program to find vowels in a character
'''
char=input("enter any word:")
vowels=['a','e','i','o','u']
s=0
e=len(vowels)
flag=0
while(s<e):
  if(char.lower==vowels[s].lower):
    flag=1
  s+=1
if(flag==1):
  print("charcter is found")
else:
  print("char not found")    
 '''
 ## program to find whether course is found in a list or not
''' 
cou=input("enter the course:")
course=["python","java","web delpoment","angular"]
s=0
e=len(course)
flag=0
while(s<e):
  if(cou.lower==course[s].lower):
    flag=1
  s=s+1
if(flag==1):
  print("course found")
else:
  print("course not found") 
  '''   
  ## program to find the course is found in a list
'''
course=input("enter any course:")
a=["Python","Java","Angular","React","Web"]
s=0
e=len(a)
flag=0
while(s<e):
  if(course.lower()==a[s].lower()):
    flag=1
  s+=1
if(flag==1):
  print("course found")
else:
  print("course not found")    
  '''
## program to find the fruits in a list
'''
list=["apple","banana","pineapple","guava","strawberry"]
f=input("enter any fruit name:")
s=0
e=len(list)
flag=0
while(s<e):
  if(f.lower()==list[s].lower()):
    flag=1
  s+=1
if(flag==1):
  print("fruit found")
else:
  print("fruit not found")   
'''
## program to find the students are  in a list or not
'''
students=["sai","raghu","srinu","rajendra","saireddy","masthan","balaji"]
v=input("enter student name:")
s=0
e=len(students)
flag=0
while(s<e):
  if(v.lower()==students[s].lower()):
    flag=1
  s+=1
if(flag==1):
  print("student is found in the class")
else:
  print("student is not found in the class")    
'''
## program to find the sum of numbers in a list
'''
mylist=[1,2,3,4,5,6,7,8,9,10]
n=0
e=len(mylist)
sum=0
while(n<e):
  sum+=mylist[n]
  n+=1
print(sum)
'''
#program to convert celsius to Fahrenheit
'''
t=float(input("enter the temperature on celsius:"))
c=(t*9/5) + 32
print(t,"celsius in Fahrenheit is",c,"Fahrenheit") 
'''
##program to convert Fahrenheit to celsius
'''
t=float(input("enter the temperature in  Fahrenheit:"))
c=(t-32)*5/9
print(t,"Fahrenheit in celsius is",c,"celsius")
'''

##program to print prime numbers in the given range
'''
s=1
range=int(input("enter the range:"))
while(s<=range):
  divisor=1
  c=0
  while(divisor<=s):
    if(s%divisor==0):
      c=c+1
    divisor+=1
  if(c==2):
    print(s)
  s=s+1
  '''

##FOR LOOP
#index based
#value based
#index based:syntax=
#range(starting value,length,increment or decrement)


#example programs
#program to print 1 to 10 numbers  using for loop
'''
s=1 
e=10
for s in range(s,e+1):
  print(s)
'''
#program to print odd numbers from 1 to 10 using for loop
'''
s=1
e=10
for s in range(s,e+1):
  if(s%2!=0):
    print(s)
'''
#program to print even numbers from 1 to 10 using for loop
'''
s=1
e=10
for s in range(s,e+1):
  if(s%2==0):
    print(s)
'''
#program to print sum of numbers from 1 to 10 using for loop
'''
s=1
n=int(input("enter the range:"))
sum=1
for s in range(s,n):
  s+=1
  sum=s+sum
print(sum)
''' 
#program to know greater number between two numbers
'''
n1=int(input("enter any number:"))
n2=int(input("enter any number:"))
if(n1>n2):
  print(n1,"is greater number")
else:
  print(n2,"is greater number")
'''
##program to know greater number between three numbers
'''
n1=int(input("enter any number:"))
n2=int(input("enter any number:"))
n3=int(input("enter any number:"))
if(n1>n2):
  print(n1,"is greater number")
elif(n2>n3):
  print(n2,"is greater number")
else:
  print(n3,"is greater number")
'''
'''

f=input("enter any course:")
a=["python","web develpoment","java","c"]
i=0
l=len(a)
flag=0
while(l<i):
  if(f.lower()==a[i].lower):
    flag=1
  i=i+1
if(flag==1):
  print(f,"is found")
else:
  print(f,"is not found")    
'''
##program to print a tabel
'''
s=int(input("enter starting number:"))
e=int(input("enter the ending number:"))
t=int(input("enter the table:"))
for s in range(s,e+1):
  print(t,"*",s,"=",t*s)
  '''

#program to find sum of even and odd numbers
'''
s=int(input("enter starting number:"))
e=int(input("enter the ending number:"))
esum=0
osum=0
for s in range(s,e+1):
  if(s%2==0):
    esum=esum+s
  else:
    osum=osum+s
print("esum is",esum)
print("osum is",osum)    
'''
##tuple is an immutable and heterogenous
##tuple has only two functions index and count
##tuple  is faster than list
##example
'''
t1=(1,2,3,"hi",2,0.1)
print(len(t1))
print(t1[0])
print(t1[-1])
print(t1.index("hi"))
print(t1.count(2))
'''

##program to find whether a given number is prime or not using for loop
'''
import time
t1=time.time()
s=1
e=int(input("enter any number:"))
c=0
for s in range (s,e+1):
   if(e%s==0):
      c+=1
   if c>2:
    break
if(c==2):
   print(e,"is a prime number")
else:
   print(e,"is not a prime number and no of factors are:",c) 
print(t1-time.time())    
'''
# program to reverse a number
'''
n=int(input("enter any  number:"))
st=''
while(n>0):
  st=st+str(n%10)
  n=n//10
print(st)  

n=int(input("enter any number:"))
st=''
while(n>0):
  st=st+str(n%10)
  n=n//10
print(st)
'''
#program to find a nummber is palindrome or not
'''
n=int(input("enter any  number:"))
t=n
st=''
while(n>0):
  st=st+str(n%10)
  n=n//10
print(st)
if st==str(t):
  print("palindrome")
else:
  print("not a palindrome")

n=int(input("enter any number:"))
t=n
st=''
while(n>0):
  st=st+str(n%10)
  n=n//10
print(st)
if(st==str(t)):
  print(t,"is a palindrome")
else:
  print(t,"not a palindrome")  

  # r=5
# c=5
# for i in range(r):
#   for j in range(c):
#     print('*',end=' ')
#   print()  
'''
# r=5
# for i in range(r):
#   for j in range(i+1):
#      print('*',end=' ')
#   print()

# r=9
# for i in range(r):
#   for j in range(i+1):
#     print(j+1,end=' ')
#   print()  
  

# c=5
# r=6
# for i in range(c):
#   for j in range(r):
#     print('*',end=' ')
#   print()  
# print('-------------------------------------')
# r=5
# for i in range(r):
#   for j in range(i+1):
#     print('*',end=' ')
#   print()  

# print('-------------------------------------')
# r=6
# for i in range(r):
#   for j in range(i):
#     print(j+1,end=' ')
#   print()  

#   '''

# #program to find the factorial of a given number
# '''
# n=int(input("enter any number:"))
# s=1
# f=1
# for i in range(s,n+1):
#   f=f*i
# print('factorial of number',n,':',f)  
# '''

# #program to print prime numbers in a given range
# '''
# s=int(input('enter the starting range:'))
# e=int(input('enter the ending range:'))
# for n in range(s,e+1):
#   if n>1:
#     for i in range(2,n):
#       if n%i==0:
#         break
#     else:
#       print(n)  
#  '''     

# '''
#program to print square shape using stars 

# r=65
# c=91
# for i in range(r):
#   for j in range(c):
#     print(char(j),end='')
#   print()


# r=5
# for i in range(r):
#   for j in range(i+1):
#     print('*',end=' ')
#   print()  

# r=5
# for i in range(r):
#   for j in range(i+1):
#     print(j+1,end=' ')
#   print()  

# SET{AT LEAST ONE VALUE MUST PRESENT}
# IT IS MUTABLe
# it does not allow duplicates
# it is an unordred listit musty contain contain atleast one value
# operations in a set
# 1.pop()
# 2.remove(value)
# 3.discard(value)
# 4.add(value)
# 5.union --> it joints two sets and avoid duplicates 
# 6.intersection --> it joints commom elements from two sets
# 7.difference --> it shows additional features from another set
# 8.isdisjoint --> no relation has to be maintained  and it returns true or False
# 9.issubset --> it means all elements must contain in another set
# 10.issuperset --> it means all elements must contain in aother set 

#example
'''
s1={1,2,3,4,3,2,'a','b','c','a','e','f',7,8,9,10}
s2={1,2,3,4,'a','b','c','d','e'}
print(s1)
s1.pop()
print(s1)
s1.remove('c')
print(s1)
s1.discard('d')
print(s1)
s1.add('sai')
print(s1)
s3=s2.union(s1)
print(s3)
s3=s2.intersection(s1)
print(s3)
s3=s1.difference(s2)
print(s3)
print(s1.isdisjoint(s2))
print(s2.issubset(s1))
print(s2.issuperset(s1))
'''

##DICTIONARY{}
# it is immutable
# it is  an unordered list
# it does not allow duplicates
# it has key value pairs 
# it is 2 dimensional

#functions in dictionary
# 1.get(key): it returns the value of the key
# 2.values(): it returns the values of the dictionary
# 3.items(): it returns the key value pairs of the dictionary
# 4.keys(): it returns the keys of the dictionary
# 5.update(key:value): it updates the value of the key
# 6.pop(key): it removes the key value pair from the dictionary
# 7.popitem(): it removes the last key value pair from the dictionary
# 8.copy: it copies the dictionary
#exapmle of functions in dictionary

student={
  'sname':'sai',
   'course':'python',
   'fee':50000,
   'city':'Guntur',
   'sage':25
 }
# print(student)
# #1.keys
# print(student.keys())
# #2.values
# print(student.values())
# #3.items
# print(student.items())
# #4.get
# print(student.get('sage'))
# print(student['sname'])
# #5.update
# student.update({'section':'DS'})
# print(student)
# #6.pop
# student.pop('section')
# print(student)
# #7.popitem
# student.popitem()
# print(student)
# #8.copy
# student1=student.copy()
# print(student1)

'''
employee={
  'ename':'bob',
  'city':'Guntur',
  'salary':50000
}
print(employee)
employee['city']='Hyderabad'
print(employee)

employee = {
  4447:['sai','DS',50000],
  4448: ['raghu','java',60000],
  4449:['srinu','python',70000],
  4450:['rajendra','angular',80000],
  4451:['sai reddy','web',90000]
}
print(employee)


student={
  'sname':'sai',
  'course':'python',
  'fee':50000,
  'city':'Guntur',
  'sage':25
}
print(student)
'''


#using for loop in dictionary to display the key value pairs in dictionary in a formatted way
'''
for i in student:
  # print('{} \t \t {}'.format(i,student[i]))
    print('{:<15}{}'.format(i,student[i]))


for i in student:
   print('{:<15} {}'.format(i,student[i]))


employee = {
  'Sno': ['EName','Designation','Salary'],
  4447:['sai','manager',85000],
  4448: ['raghu','java developer',80000],
  4449:['srinu','python developer',70000],
  4450:['rajendra','angular developer',80000],
  4451:['sai reddy','web develeoper',90000]
}
# 
print('------------------------------------------------------------------------------')
print('Employee table')
print('------------------------------------------------------------------------------')
for i in employee:
  print('{:<10}{:<20}{:<25}{}'.format(i,employee[i][0],employee[i][1],employee[i][2]))
print('------------------------------------------------------------------------------')
'''
'''
student={
  'Rno':['Sname','Course','Fee','AdmissionType','Stay','City'],
  4447:['sai','DS',70000,'jvd','dayscholar','Guntur'],
  4448:['raghu','DS',70000,'management','hosteller','Hyderabad'],
  4449:['srinu','DS',70000,'jvd','dayscholar','Guntur'],
  4450:['rajendra','DS',70000,'management','hosteller','Tenali'],
  4451:['sai reddy','DS',70000,'jvd','dayscholar','Guntur'],
  4452:['masthan','DS',70000,'jvd','hosteller','Etukuru'],
  4453:['balaji','DS',70000,'jvd','hosteller','Chavali'],
  4454:['satish','Ds',70000,'jvd','hosteller','Tenali'],
  4455:['sai kumar','DS',70000,'management','hosteller','Guntur'],
  4456:['saireddy','DS',70000,'managemt','dayscholar','Tenali'],
  4457:['krishna','DS',70000,'jvd','hosteller','Guntur'],
  4458:['yuggu','DS',70000,'jvd','dayscholar','Chpet'],
  4459:['CR','DS',70000,'jvd','hosteller','Tenali'],
  4460:['janaki','DS',70000,'management','dayscholar','Vijayawada'],
  4461:['tarun','DS',70000,'jvd','hosteller','Kurnool'],
  4462:['naveen','DS',70000,'managemet','dayscholar','KAkinada'],
}
print('-------------------------------------------------------------------------------------')
print('Student table')
print('-------------------------------------------------------------------------------------')
for i in student:
   print('{:<10}{:<20}{:<15}{:<15}{:<15}{:<15}{}'.format(i,student[i][0],student[i][1],student[i][2],student[i][3],student[i][4],student[i][5]))
print('-------------------------------------------------------------------------------------')   
'''
'''
student={
  'Rno':['Sname','Course','Fee','AdmissionType','Stay','City'],
  4447:['sai','DS',70000,'jvd','dayscholar','Guntur'],
  4448:['raghu','DS',70000,'management','hosteller','Hyderabad'],
  4449:['srinu','DS',70000,'jvd','dayscholar','Guntur'],
  4450:['rajendra','DS',70000,'management','hosteller','Tenali'],
  4451:['sai reddy','DS',70000,'jvd','dayscholar','Guntur'],
  4452:['masthan','DS',70000,'jvd','hosteller','Etukuru'],
  4453:['balaji','DS',70000,'jvd','hosteller','Chavali'],
  4454:['satish','Ds',70000,'jvd','hosteller','Tenali'],
  4455:['sai kumar','DS',70000,'management','hosteller','Guntur'],
  4456:['saireddy','DS',70000,'managemt','dayscholar','Tenali'],
  4457:['krishna','DS',70000,'jvd','hosteller','Guntur'],
  4458:['yuggu','DS',70000,'jvd','dayscholar','Chpet'],
  4459:['CR','DS',70000,'jvd','hosteller','Tenali'],
  4460:['janaki','DS',70000,'management','dayscholar','Vijayawada'],
  4461:['tarun','DS',70000,'jvd','hosteller','Kurnool'],
  4462:['naveen','DS',70000,'managemet','dayscholar','KAkinada'],
}
print('-------------------------------------------------------------------------------------')
print('Student table')
print('-------------------------------------------------------------------------------------')
for i in student:
   print('{:<10}{:<20}{:<15}{:<15}{:<15}{:<15}{}'.format(i,student[i][0],student[i][1],student[i][2],student[i][3],student[i][4],student[i][5]))
print('-------------------------------------------------------------------------------------')   
'''
# pandas: data visualisstion and data manipulationa and data analysis
# Series: it is a one dimensional array(list,tuple)
# dataFrame: it is a two dimensional array(dictionary)
# panel: it is a three dimensional array
#DataFrame:it converts the dictionary into a table format
import pandas as pd
'''
student={
   'adminNo':[4447,4448,4449,4450,4451,4452,4453,4454,4455,4456,4457,4458,4459,4460,4461,4462],
   'SName':['sai','raghu','srinu','rajendra','sai reddy','masthan','balaji','satish','sai kumar','saireddy','krishna','yuggu','CR','janaki','tarun','naveen'],
   'Course':['DS','DS','DS','ECE','DS','CSE','DS','DS','AIML','DS','DS','CSE','DS','ECE','DS','AIML'],
    'Fee':[70000,70000,70000,800,70000,80000,70000,70000,90000,70000,70000,80000,70000,80000,70000,90000]
    }

import pandas as pd
stable=pd.DataFrame(student)
print(stable)
'''

'''
employee={
  'ename':['sai','raghu','srinu','rajendra','sai reddy'],
  'Role':['manager','asst manager','team lead','developer','tester'],
  'salary':[85000,80000,70000,80000,90000],
  'city':['Guntur','Hyderabad','Guntur','Tenali','Guntur'],
  'age':[25,26,27,28,29]
}
print('--------------------------------------------------------------------')
print('Employee table')
print('--------------------------------------------------------------------')
import pandas as pd
etable=pd.DataFrame(employee)
print(etable)
print('--------------------------------------------------------------------')
'''

student={
 'sname':['sai','raghu','srinu','rajendra','sai reddy'],
 'course':['python','java','angular','react','web'],
  'fee':[50000,60000,70000,80000,90000],
  'city':['Guntur','Hyderabad','Tenali','Guntur','Vijayawada'],
  'age':[25,26,27,28,29]

}
'''
print('--------------------------------------------------------------------')
print('Student table')
print('--------------------------------------------------------------------')
import pandas as pd
stable=pd.DataFrame(student)
print(stable)
print('--------------------------------------------------------------------')
'''

#series: it is a one dimensional array
# it is a list or tuple
# it is a one dimensional array
'''
d={'a':1,'b':2,'c':3,'d':4}
s=pd.Series(data=d, index=['a','b','c','d'])
print(s)

d1={'a':'sai','b':'raghu','c':'srinu','d':'rajendra'}
ser=pd.Series(data=d1, index=['a','b','c','d'])
print(ser)


d={1:'sai',2:'raghu',3:'srinu',4:'rajendra'}
s=pd.Series(data=d,index=[1,2,3,4])
print(s)
'''

#constructing series from list with copy=false
'''
r=[1,2,3,4,5]
#copy:bool,default=False
#copy input data only effects Series or Id ndarray input
ser=pd.Series(r,copy=False)
ser.iloc[0]=999
#iloc:it is used to access the element of the series
print(ser)
'''

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

#Python Tuples()
# Tuple
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
#example
'''
mytuple=('apple','banana','cherry')
print(mytuple)
'''

#functions
#static functions

def showAddress():
  print('Guntur')
  print('Hyderabad')
#showAddress()

def employee():
  print('Ename        : sai')
  print('salary       : 50000')
  print('city         : Guntur')
  print('designation  : developer')
#employee()   

                                                                                      
#dynamic functions or parameter function or restricted functions
def student(sname,course,fee,city):
  print('Sname:',sname)
  print('Course:',course)
  print('Fee:',fee)
  print('City:',city)                                                                     
  '''
print('--------------------------------------------------------------------')
print('Student detais')
print('--------------------------------------------------------------------')
student('sai','python',50000,'Guntur')
print('--------------------------------------------------------------------')
student('raghu','java',60000,'Hyderabad')
print('--------------------------------------------------------------------')
student('srinu','angular',70000,'Tenali')
print('--------------------------------------------------------------------')
student('rajendra','react',80000,'Guntur')
print('--------------------------------------------------------------------')
student('sai reddy','web',90000,'Vijayawada')
print('--------------------------------------------------------------------')
'''

#create a function student,
#take 3 parameters subject name,total marks and average    
# def student(Subjectname,marks,average):
#   print('Subjectname :',Subjectname)
#   print('Marks       :',marks)
#   print('Average     :',average)

def student(subject_name, total_marks, average):
    """
    Function to display student subject details.

    Parameters:
        subject_name (str): The name of the subject.
        total_marks (int or float): Total marks obtained in the subject.
        average (float): Average marks for the subject.

    Returns:
        None
    """
    print(f"Subject Name: {subject_name}")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average:.2f}")

# Example usage
student("Mathematics", 450, 75.0)
