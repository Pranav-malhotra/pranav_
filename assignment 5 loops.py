#!/usr/bin/env python
# coding: utf-8



#question 1
s = input("Enter a string : ")

i = len(s)
a = 1
b=""
# print(i)
while a <=i :
    q = s[-a]
    b += q
    a += 1
    # print(b)

print(b)


#question 2
num1 = int(input("Enter the Number : "))
r1 = int(input("Range starts from :"))
r2 = int(input("Range ends to :"))


for a in range(r1,r2):
    if num1 % a == 0:
        print( num1, "is divisible by", a)
        


#question 3
a = int(input("Enter the First side of the triangle"))
b = int(input("Enter the Second side of the triangle"))
c = int(input("Enter the Third side of the triangle"))

s = (a+b+c)/2
print(s)
a = (s*(s-a)*(s-c)*(s-b))**1/2
print("Area =", str(a))




#question 4
odd = int(input("Enter an odd number : "))


if odd % 2 == 0 :
    print("Error !!!")
    
else:
    a = int((odd+1)/2)
    for c in range(1,a+1):
        print("*" * c )

    for e in range(a-1, 0 , -1):
        print("*" * e)


#question 5
r1 = int(input("Enter Start of range : \n"))
r2 = int(input("Enter End of range : \n"))

for a in range(r1,r2+1):
    for j in range(2,a):
        if a % j == 0:
            break
    else:
        print( a , end=" ")
        

#question 6
r1 = int(input("Enter Start of range : \n"))
r2 = int(input("Enter End of range : \n"))

for a in range(r1,r2+1):
    for j in range(2,a):
        if a % j == 0:
            break
    else:
        print( a , end=" ")


#question 7
for a in range(1,500+1):
    if a % 7 == 0 and a% 11 == 0:
        print(a)




#question 8
num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
num3 = int(input("Enter 3rd Number : "))
num4 = int(input("Enter 4th Number : "))
num5 = int(input("Enter 5th Number : "))
num6 = int(input("Enter 6th Number : "))
num7 = int(input("Enter 7th Number : "))
num8 = int(input("Enter 8th Number : "))
num9 = int(input("Enter 9th Number : "))
num10 = int(input("Enter 10th Number : "))

list = [ num1 , num2,num3,num4,num5,num6,num7, num8,num9,num10]

p_num = []
n_num = []
even = []
odd = []
occur = []


for a in range (10):
    i = list[a]
    if i >= 0:
        p_num.append(i)
    if i <= 0:
        n_num.append(i)
    if i % 2 == 0 :
        even.append(i)
    if i %2 != 0:
        odd.append(i)
    
      
    
print("positive numbers : " , p_num)
print("positive numbers : " ,n_num)
print("even numbers : " ,even)
print("odd numbers : " ,odd)
# print(occur)

for a in range (10):
    i = list[a]
    x = p_num.count(i)
    y = n_num.count(i)
    z = even.count(i)
    w = odd.count(i)
    print ( i ,"occurs", x+y+z+w, "times")


#question 9
my_list = []
i=True
while i == True:
    x = input("Enter a word :\n ")
    my_list.append(x)
    y = input("Do you want to enter more names :\n")
    if y == "y" or y == "Y" or y == "YES" or y =="yes":
        i = True
    elif y == "n" or y == "N" or y == "NO" or y =="no":
        i = False
    else:
        break


# print(my_list)
print("")

my_dic = {}

for word in my_list:
    if word in my_dic:  
        b = my_dic[word] 
        b += 1
        my_dic[word]=b
    else:
        my_dic[word]=1

print(my_dic)

