#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from AutomationFlow.AutomationFlow import Runner
import time

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
END = "\033[00m"

def red(s): return RED + s + END

def green(s): return GREEN + s + END

def yellow(s): return YELLOW + s + END

def get_input():

    while True:
        print("Please enter a number (0 < number <= 100.)")
        inp = input(">> ")

        try:
            number = int(inp)
        except:
            print(red("Wrong input."))
            continue

        if 0 < number <= 100:
            print(yellow(f"number is: {number}"))
            return number

def countdown(state, n):

    if isinstance(n, str):
        n = int(n)

    for i in range(n):
        s = yellow("{}...".format(n-i))
        print(s, end="\r")
        time.sleep(1)

def progress_bar(state, n, _sleep=0.3):

    if isinstance(n, str):
        n = int(n)

    for i in range(0, n+5, 5):
        s = "{}/{} [{}]".format(
            i, # numerator
            n, # denominator
            ("#" * i) + (" " * (n - i)) # increasing # as progress bar moves ahead
        )

        if i < n / 4:
            s = red(s)
        elif i < (n / 3)*2:
            s = yellow(s)
        else:
            s = green(s)

        print(s, end="\r")
        time.sleep(_sleep)

    print()

if __name__ == "__main__":

    r = Runner(script_fpath="script.md",
           _context = {
               "countdown" : countdown,
               "get_input" : get_input,
               "progress_bar" : progress_bar,
               "name" : "bob"
           }
    )
     
    r.run()
