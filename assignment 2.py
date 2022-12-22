#!/usr/bin/env python
# coding: utf-8

#ASSIGNMENT 2

#question 1
# In[15]:
string = "python is a case sensitive language"
x = len(string)
print(x)

b= string[::-1]
print(b)

string_obj = slice(10,27)
print(string[string_obj])

print(string.replace("a case sensitive","object oriented"))

print(string.find('a'))

print(string.replace(" ",""))


#question 2
# In[34]:


name = "Pranav"
sid = 22105036
department = "ECE"
cgpa = input(" please enter your cgpa :")
print("hey,%s here!"%(name))
print("My SID is %d"%(sid))
print(" I am from %s department and my CGPA is %s"%(department ,cgpa))

#question 3
# In[1]:


a = 56
b = 10
print("a & b =", a&b)
print("a | b =", a|b)
print("a ^ b =", a^b)
print("Left shifting both a and b with 2 bits =", a<<2, "=", b<<2)
print("Right shifting a with 2 bits and b with 4 bits =", a>>2, "=", b<<4)


#question 4
# In[7]:


a = int(input("please enter first number :"))
b = int(input("please enter second number :"))
c = int(input("plleaee enter third number :"))
if(a>b and a>c):
                print("the greatest number is ",a)
elif(b>a and b>c):
                print("the greatest number is",b)
else:
     print("the greatest number is :",c)
    
        

#question 5
# In[6]:


a = input("please enter the string :")
if "name" in a:
    print("Yes!")
else:
    print("No!")


#question 6
# In[2]:


len1 = float(input("Enter length of side 1: "))
len2 = float(input("Enter length of side 2: "))
len3 = float(input("Enter length of side 3: "))
if len1 + len2 > len3 and len2 + len3 > len1 and len1 + len3 > len2:
    print("Yes")
else:
    print("No")







