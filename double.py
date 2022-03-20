# Name: Andrew Chau
# Date: 20 March 2022
# Course: CMPE 131
# Description: This program uses a decorator, doubler, to call the function, calling, 
# and use it twice within itself 

def doubler(func):
    def wrapper():
        func()
        func()
    return wrapper

def calling():
    print("Function successfully called")

calling = doubler(calling)

calling()

# Output: 
# Function successfully called
# Function successfully called
