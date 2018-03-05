"""
Bo Chen (10190141)
CISC 121 Assignment 3: Recursion
August 4, 2017

This is a Python version 3.6 of the Recursion Assignment.
This program has the following recursive functions: 
breakApart(), numVowels(), multiply(), and numOnes().
This program also has a tester() function which tests the program.
Detailed assignment requirements can be found here: https://goo.gl/WpSWML
"""


"""
The breakApart() function prints the digits of a given integer individually.
The function takes a integer and prints integer(s).
"""
def breakApart(number):
     #base case
    if number <= 0:
        return
    breakApart(number//10) 
    print (number % 10)

"""
The numVowels() function counts the number of vowels in a string.
The function takes a string and returns a integer.
"""
def numVowels(string):
    counter = 0
    vowels = ['a' ,'e', 'i', 'o', 'u']   
    #base case
    if len(string) <= 0:
        return 0      
    elif string[0] in vowels:
        counter = 1
        counter = counter + numVowels(string[1:])
        return counter
    else:
        counter = counter + numVowels(string[1:])
        return counter

"""
The multiply() function finds the product of the numbers from 'low' to 'high' (inclusive)
The function takes a two integers ('low' and 'high') and returns a integer.
"""
def multiply(low, high):
    mid = ((low + high) //2)
    #base case
    if high < low:
        return   
    elif low+1 == high:
        return low*high  
    elif low == mid or low > mid:       
        return low
    else:
        num = (multiply(low, mid) * multiply(mid+1, high))
        return num 

"""
The numOnes() function takes n as input and returns the number 
of 1's in the binary representation of n.
The function takes a nonnegative integer and returns a integer.
"""
def numOnes(n):
    counter = 0
    #base case
    if n <= 0:
        return 0
    elif n % 2 == 1:
        counter = 1
        counter = counter + numOnes(n//2)
        return counter
    else:
        numOnes(n//2)
        counter = counter + numOnes(n//2)
        return counter

"""
The tester() function tests the program.
"this has been done to minimize the output for the TAs to aid in marking."
"""
def tester():
  breakApart(54321)
  print()
  breakApart(987)
  print()
  breakApart(4)
  print()
  print(numVowels("mnsty"))
  print(numVowels(""))
  print(numVowels("annn"))
  print(numVowels("nnnnna"))
  print(numVowels("canoe"))
  print(multiply(4, 7))
  print(multiply(2, 10))
  print(multiply(8, 2))
  print(numOnes(128))
  print(numOnes(127))
  
tester()

