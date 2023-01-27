#!/usr/bin/env python
# coding: utf-8

# In[3]:


num=int(input("please enter marks : "))

if num>=80:
    print("Your grade is A")

elif num>=60:
    print("Your grade is B")
elif num>=50:
    print("Your grade is C")
elif num>=45:
    print("Your grade is D")
elif num>=25:
    print("Your grade is E")
else:
    print("Your grade is F")
     


# In[1]:


year=int(input("Please enter the year: "))
if year%4==0 and year%100!=0:
    print("It's a leap year")
elif (year%400==0 and year%100==0):
    print("It's a leap year")
else:
    print("it's not a leap year")


# In[2]:


import random
for i in range(1,11):
    a=random.randint(1,10)
    b=random.randint(0,10)
    print("Question"+str(i)+":",a,"x",b,"= ")
    c=int(input())
    if c==a*b:
        print("Right!")
    else:
        print("Wrong. The correct answer is", a*b)


# In[2]:


x=0 
for x in range(0,200):
     if (x%5==2 and x%6==3 and x%7==2):
        print("the number of candies are : ",x)
    


# In[ ]:




