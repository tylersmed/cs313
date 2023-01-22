
def iter_func(n):
    for item in range(n):
        print(item)
    print("Stop")

# iter_func(3)

# Recursive version
def recursive_func(n):
    if n < 0:
        print("Stop")
    else:
        print(n)
        recursive_func(n-1)
        
# recursive_func(3)

########################################

# factorials

def iter_fact(n):
    tmp = 1
    for item in range(1, n+1):
        tmp = tmp * item
    return tmp

#print(iter_fact(5))

# Recursive version
def recursive_fact(n):
    if n <= 0:
        return 1
    else:
        return n * recursive_fact(n-1)

# print(recursive_fact(5))

########################################

# Fibonacci series

def fibonacci(n):
    """Iterative Implementation of Fibonacci number"""
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

print(fibonacci(10))

# Recursive version
def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)
# This version is inefficient because it recalcultes things it already did

print(fib_recursive(10))
