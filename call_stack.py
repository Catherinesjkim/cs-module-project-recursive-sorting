"""
Function Call Stack: 
Computer needs to know what Fn that I'm running/calling now? 
Every new fn adds a new element on top of the stack
The fn at the top of the stack is the current running fn
Return is very important to understand in Recursive Fn!

Stack Overflow (Python's stack limit): default is 996 - not the memory, the times you can call until you get a recursion error. 

Check the recursion limit with sys.getrecursionlimit: print(sys.getrecrusionlimit())

Change the recursion limit with sys.setrecrusionlimit(1500)

RecursionError: maximum recursion depth exceeded while calling a Python object

RecursionError == Stack Overflow

"""

def print_a():
    letter = "A"
    print(letter)
    return # important relationship with the call stack - the call fn on top of stack gets popped - back to print_all() - pause mode --> it knows to print_b()
    
def print_b():
    letter = "B"
    print(letter)
    
def print_c():
    letter = "C"
    print(letter)

def print_all():
    print_a()
    print_b()
    print_c()
    return

print_all()
