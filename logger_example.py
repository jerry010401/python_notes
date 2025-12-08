
# normal print statement:-
"""
def divide(a,b):
    print(f"Dividing {a} by {b}")
    try:
        result = a/b
        print(f"Result:{result}")
        return result
    except ZeroDivisionError:
        print("Error: Tried to divide by zero!")
        return None
divide(10,5)
divide(30,2)
divide(10,0)

"""

# LOGGER is a tool used to record messages from your program while it runs, which can help
# you debug,monitor,and maintain your code more effectively.its part of the built-in logging module in python.

# level - purpose
# 1. "DEBUG"-Details information (for dev only)
# 2. "INFO" - General info (app started,etc.)
# 3. "WARNING" - Something might go wrong.
# 4. "ERROR" - Something went wrong.
# 5. "CRITICAL" -Serious error (app may crash)

# LIMITATION OF USING PRINT()
# -> you can't set levels - example(info vs error)
# -> you can't redirect easily to a file.
# -> you can't filter message (like you show only error)
# -> No timestamps unless you manually add them.
# -> No format control

import logging

# configure logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s -%(message)s",
    filename="app.log",   # you can remove this line to log to console
    filemode="w"
)

def divide(a,b):
    logging.info(f"Dividing {a} by {b}")
    try:
        result = a/b
        logging.debug(f"Result : {result}")
        return result
    except ZeroDivisionError:
        logging.error("Tried to divide by zero!")
        return None

# Test

divide(20,4)
divide(30,0)

"""
interview question:-

✅ 1. What is print?
-> print() is used to display simple output on the screen (console).
   It is mainly used for debugging small programs.
   
   ✅ 2. What is a Logger? (Simple Explanation)

->  A logger is part of Python’s logging module.
    It is used to track, record, and store program events, errors, and system information.

Loggers can:

Save messages to files

Show different levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

Work in production applications (real apps)

"""





