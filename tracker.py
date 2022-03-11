# Name: Andrew Chau
# Date: 10 March 2022
# Course: CMPE 131
# Description: This program tracks the number of times the variable, counter, is called within
# the decorator function, func_counter, when the function foo is being decorated.

def func_counter(func):
    def wrapper(y):
        wrapper.counter+=1
        func(y)
    wrapper.counter = 0
    return wrapper


@func_counter
def foo(y):
    x = y+2**3-34
    print("Answer:", x)
    return x

foo = func_counter(foo)
foo(10)
foo(50)

print("Counter:", foo.counter) # expect 2 as output

# Output: 
# Answer: -16
# Answer: 24
# Counter: 2
