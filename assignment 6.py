#!/usr/bin/env python
# coding: utf-8
#assignment 6

#question 1
x = int(input("Please enter a number : \n"))



def perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return "It is a perfect number"
    else:
        return "It is not a perfect number"
    
print(perfect_number(x))

#question 2
print("PROGRAM TO CHECK PALINDROME")

y = input("Enter a word, phrase, sequence or number : \n")
def is_palindrome(string): 
  
    string = string.lower() 
  
    reverse_string = string[::-1] 
  
    if string == reverse_string: 
        return True
    return False


print(is_palindrome(y))


#question 3
n = int(input("Enter the number of rows : \n"))

def pascalsTriangle(n):
  for row in range(1, n+1):
    c = 1
    for i in range(1, row+1):
      print(c, end=" ")
      c = int(c * (row-i)/i)
    #   print("c = ",c , end=",")
    print("")

pascalsTriangle(n)

#question 4
x= input("Enter the string : ")

def is_pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string.lower():
            return False
    return True

is_pangram(x)


#question 5
a=input("Enter a string seperated by hyphens(-)")
a=a.replace("-"," ")
list_1=list(a.split())
list_1.sort()
b="-".join(list_1)
print(b)




