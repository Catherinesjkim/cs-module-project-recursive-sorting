""" 
Recursion is a Fn which calls itself 
Function Call Stack: return - very important to understand recursion!
The fn at the top of the stack is the current running fn
Must have a base case and a recursive case
What is my base case? What is my recursion case? 

Base Case? 
- Add recursion case
- How do you get to base? 

Runtime Complexity in Recursion - Total O(N) - runtime of code in the fn x number of times fn is called
Space Complexity in Recursion - Amount of frames O(N) even though no space in the code

big_O: pip install big-o

"""
# fn which prints every number from N to zero
# def print_numbers(n):
#     for i in range(n, 0, -1):
#         print(i)

# O(N), the fn gets called N times
def print_num(n):
    print(n) # Constant Time
    # we need a base case (i.e. the code that tells us to stop running this function)
    if n == 0: # we terminate with this condition - Constant Time
        return # the Fn returns and never calls itself again - break/soft return is only for loops, Not for Fn
    
    # recursive case (i.e. the case which takes us to the next subproblem)
    print_num(n-1) # add the new item onto the stack - fn call - Constant Time
    return  # n=1 O(1), n=2 O(1), n=3 O(1), n=4 O(1) gets popped from the stack 
    
# print_num(4)


# 15 functions up on the stack - 2^N
def double_print_num(n):
    # print(n)  # prints 3
    if n == 0: # if 0, we pop the top and return 0 twice
        return
    
    double_print_num(n-1) # 2, 1, 0, 0, 1, 0, 0 --> 2^N
    double_print_num(n-1) # 2, 1, 0, 0, 1, 0, 0 --> 2^N
    return # it terminated the base case 


# Fibonacci Sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

# Fib(n) = Fib(n-1) + Fib(n-2) 
# Same Fn called twice on two different results

# Base case: 
# at n = 0  Fib(0) == 0 
# at n = 1  Fib(1) == 1 

# O(2^N) - too many duplications - recursion is not the best solution in this case
# any function can be solved with iterative solution
def fibonacci(n):
    # Base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case
    result = fibonacci(n-1) + fibonacci(n-2) # how many times is it going to be called? 
    return result

print(fibonacci(20))

