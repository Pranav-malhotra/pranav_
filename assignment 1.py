#!/usr/bin/env python
# coding: utf-8

#ASSIGNMENT 1

#QUESTION 1
a = int(input("please enter first number : "))
b = int(input("please enter second number : "))
c = int(input("please enter third number : "))
average = ((a+b+c)/3)
print("the average of three numbers is : ")
print(average)

#QUESTION 2
# In[3]:
Gross_income = int(input("please enter gross income : "))
standard_deduction = 10000
dependent_deduction = 3000
number_of_dependents = int(input("please enter no. of dependents : "))
tax_rate = 0.2
Taxable_income = Gross_income - standard_deduction - (dependent_deduction*number_of_dependents)
print(" your taxable income : ")
print(Taxable_income)
tax_ = Taxable_income*tax_rate
print("your tax amount is : ")
print(tax_)

#QUESTION 3
# In[6]:
x = int(input("Enter the number : "))
min = x//60
sec = x%60
print("The minutes :" + str(min) + " , the seconds :" + str(sec) )

# QUESTION 4
# In[11]:
a = 25
b = '25'
c = 25.0

d = a + int(b) + int(c)
print (str(d))

# QUESTION 5
# In[28]:
import math as m

for i in range (0,346,15):
    b = float( i * (m.pi/180))
    print ( "" + str(i) + " --- " + str(round(m.sin(b),4)) + "    " + str(round(m.cos(b),4)))
    # print(round(m.sin(b),4))







