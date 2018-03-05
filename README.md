This is a Python version 3.6 of the Recursion Assignment.
This program has the following recursive functions: 
breakApart(), numVowels(), multiply(), and numOnes().
This program also has a tester() function which tests the program.

Assignment:
"Write recursive functions that solve each of the following problems. Your functions must be recursive -- that is, they should have a base case and, in each recursive call, your problem should be reduced to an identical problem of a smaller size. You should have no loops in your code. Your solutions should not be using built-in functions with the exception of len().

1. Write a function called "breakApart" that prints the digits of a given integer individually.  This function should not return anything.  For example, breakApart(37921) would print the following:

3
7
9
2
1

2. Write a recursive function that counts the number of vowels in a string.   Call this function "numVowels".

3. Write a recursive function called "multiply" that finds the product of the numbers from n to m (inclusive) by recursively splitting the list in half and finding the product of the first half of the list then the product of the second half of the list and multiplying them together.   The following solution, although it solves the problem, is not acceptable as it does not split the list in half repeatedly. 

def multiply(n, m):
    print(n, m)
    if n > m:
        return None
    if n == m:
        return m
    return n * multiply(n+1, m)

>>>print(multiply(3, 6))
360   #this is what would be printed
4. Write a recursive function numOnes() that takes a nonnegative integer n as input and returns the number of 1's in the binary representation of n.  Use the fact that this is equal to the number of 1's in the representation of n//2 (integer division) plus 1 if n is odd. 

>>numOnes(0)
0 
>>numOnes(1) 
1
>>numOnes(14)
3
Add the following testing function to your code. This should be the only code that runs when we execute your program -- so you will need to add a call to "tester" to make it run. Please note that this function breaks all rules in terms of "user friendliness" -- this has been done to minimize the output for the TAs to aid in marking.

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
  print(numOnes(127))"
