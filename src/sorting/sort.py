"""
Divide and Conquer
- take a hard problem
- break into smaller sub-problems
- sorting problem is hard and best solution is O(N^2)

Quick Sort
1. Choose a pivot: any random number in the list
2. Move all elements < pivot to the left of the pivot
   all elements >= pivot, move to the right of the pivot
3. repeat step 1 & 2 on left and right

TimSort: doesn't always choose recursion sort - uses merger sort or insertion sort sometimes because it's faster
   
"""
import time

# O(N Log(N)) Solution - the problem becomes smaller almost every time
# Worst case is O(N^2) - Hard to get worst case - what would the input be? Sorted & reverse sorted
# helper fn
def partition(numbers):
    # this function breaks numbers into a lefft, pivot and right
    left = []
    pivot = numbers[0] # start from 5
    right = []
    
    # partition the numbers correctly into left and right arrays
    for num in numbers[1:]: # 2. start our loop from the second index to separate it, & don't add it to the left or right - figured out how to divide
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)
        
    return left, pivot, right

def quicksort(numbers):
    # base case
    # what is the easiest array to sort?
    # "Conquer" step, it's just so easy
    if len(numbers) <= 1:
        return numbers
    
    # divide
    # figure out how to properly split our data
    left, pivot, right = partition(numbers)

    sorted_array = quicksort(left) + [pivot] + quicksort(right)
    return sorted_array
    
print(quicksort([5, 9, 3, 7, 2, 8, 1, 6]))
    
    





