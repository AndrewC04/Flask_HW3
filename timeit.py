# Name: Andrew Chau
# Date: 10 March 2022
# Course: CMPE 131
# Description: This program returns the exact number of seconds it takes to run the function, time_func, in 
# the decorator, calculate_time, using time.time()

import time

def calculator_time(func):
    def wrapper():
        print("Finding total time...")
        func()
    return wrapper


def time_func():
    val = time.time()
    print("Total time:", val)

time_func = calculator_time(time_func)

time_func()

# Output: 
# Finding total time...
# Total time: 1646896069.4594543