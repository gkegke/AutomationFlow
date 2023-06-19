#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from AutomationFlow.AutomationFlow import Runner
import time
import random

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
END = "\033[00m"

def red(s): return RED + s + END

def green(s): return GREEN + s + END

def yellow(s): return YELLOW + s + END

def get_number():

    while True:
        print("Please enter a number (0 < number < 1001.)")
        inp = input(">> ")

        try:
            number = int(inp)
        except:
            print(red("Wrong input."))
            continue

        if 0 < number < 1001:
            print(yellow(f"number is: {number}"))
            return number


def bs_simulate(state, n):
    numbers = list(range(1,1001))

    user_number = int(n)
    
    # Checking if the user number is valid
    if user_number < 0 or user_number > 1000:
        print("Invalid number. Please try again.")
    else:

        lo = 0
        hi = len(numbers) - 1
        steps = 0
    
        # Looping until the user number is found or the search space is exhausted
        while lo <= hi:
            
            # Incrementing the steps counter
            steps += 1
    
            # Finding the middle index using bisect.bisect_left

            mid = (lo + hi) // 2

            print(f"Step {steps}: Found {numbers[mid]} at index {mid}")
    
            # Checking if the value at the middle index is equal to the user number
            if numbers[mid] == user_number:
                # Printing a success message and breaking the loop
                print()
                print(green(f"Congratulations! You found your number in {steps} steps."))
                return

            print(f"{numbers[mid]} is not the target number")
            print(f"Possible options left: {hi - lo}")
            print()

            # Checking if the value at the middle index is greater than the user number
            if numbers[mid] > user_number:
                # Updating the high index to be one less than the middle index
                hi = mid - 1
            # Checking if the value at the middle index is less than the user number
            else:
                # Updating the low index to be one more than the middle index
                lo = mid + 1

            time.sleep(1)

    return -1
    

if __name__ == "__main__":

    r = Runner(script_fpath="script.md",
           _context = {
               "get_number" : get_number,
               "bs_simulate" : bs_simulate,
               "random_list" : lambda: print(random.choices(range(100), k=random.randint(5,20)))
           },
           print_delay=0.005
    )
     
    r.run()
