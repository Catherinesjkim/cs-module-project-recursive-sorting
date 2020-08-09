"""
Recursion

Handy for solving algo problems

Example: Inception, tree structures, stem of broccoli, serpinski triangle

Definition:

1. A base case ( or cases) that specify when the recursion terminates

2. A rule ( or rules) that reduce all other cases towards a base case

"""
# easier to parse & more elegant
# given some int n, multiply every num preceding that num down to 1 (if n = 4, factorial of 4 --> 4 * 3 * 2 * 1)
def recurse_factorial(n): # 1. n == 4, skip the base case --> last line
    if n == 0: # 3. base case satisfied? - stop factorial function here - n is a positive int right before 0
        return 1 # 4. base case
    return n * recurse_factorial(n - 1) # 2. moving towards the base cases - run this function with 3, 2, 1

def iter_factorial(n):
    answer = 1
    for i in range(n, 0, -1): # starts at n, goes down to 0 but skips 0, & steps through it backwards
        answer *= i
    return answer

"""
When to use recursion:

1. "...compute the nth term of..."
2. "...list the first n terms of..."
3. "...generate all possible permutations of sth..."


Pros and Cons

Pros
1. Intuitive - easier to parse
2. Clean - elegant
3. Starting Point - a tangible starting point - figure out base cases and how to get to those base cases

Cons
1. Mind-bending 
2. Not Performant - no fine grained control like for loops
"""

"""
Recursive Sorting Algorithms - Merge & Quick sort algorithms

Merge Sort
1. Divide in half until you have subarrays of length 1 (list of length 1 are sorted!)
2. Merge sorted lists together 

Quick Sort
1. Choose a pivot (we'll choose the 1st element)
2. Move all elements less than the pivot to its LHS
3. Move all elements greater than the pivot to its RHS
4. Repeat steps 1-3 until array sorted

