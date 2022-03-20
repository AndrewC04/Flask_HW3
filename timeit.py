# Name: Andrew Chau
# Date: 20 March 2022
# Course: CMPE 131
# Description: This program returns the exact number of seconds it takes to run the function, time_func, in 
# the decorator, calculate_time, using time.time()

import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        ans = func()
        end = time.time()
        val = end - start
        print(f"Total time {val}")
        return ans
    return wrapper

@calculate_time
def time_func():
    for i in range(10000000):
        i * 3

# time_func()

# Output: 
# Total time 4.5731096267700195
