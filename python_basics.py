from typing import Sequence


x = 10 
print(x)
x = "sourav"
print(x)    
x = 10+5j
print(x)

# user = input("enter user name ")
# pwd = input(" enter password")
# if user=="sourav" and pwd == "python" : 
#     print("valid user ")
# else : 
#     print("invalid user ")

x = 10
list = [10,20,30] 
if x in list : 
    print("present ")
else : 
    print("not present")

print(10,20,30,40,sep='-')

print(10,end=" ")
print(20,end=" ")
print(30)  #prints in new line to avoid that use end

# 10:20:30:A:B:C is our requirement 
print(10,20,30,sep=':',end=":")
print('A','B','C',sep=':')

name='sourav'
marks=100
salary=1000000
print('name:{},marks:{},salary:{}'.format(name,marks,salary)) #{} is used as replacement optr

del name

l=[] #creates an empty list
l.append(10) #adds 10 to the list
print(l)
l.remove(10)
print(l)

l = [ x*x for x in range(1,10) if x%2==0]
print(l)

# [ expression for item in Sequence if condition ] 

s = set() #declares an empty set  s = {} is not set but a dictionary focus on syntax
s.add(10)
s.add(20)
s.add(30)
print(s)

d = {} #empty dictionary 
# d[key] = value 
# del d[key]   to delete on key value 
# if key is already available old value will be replaced 
# d.get(key)  to get the value corresponding 

# def f(name='sourav',*a) :
#     print('hare krishna ')
#     return 10,20,30 
#  #write a function only once use it multiple times 
# #  multiple values can return in form tuple  biggest benefits
# #  can provide default values 
# # f(10,name="soruav") 
# # here 10 is called positional arguments and name is called keyword argument positional arg should come first 
# # keyword argument 
# # variable length should always come at last other wise we need to specify

s = lambda x:x*x   #lambda functions
print(s(4))

    