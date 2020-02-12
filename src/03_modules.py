"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for (index, arg) in enumerate(sys.argv):
    print(f"Command Line Argument #{index + 1}: {arg}\n")

# Print out the OS platform you're using:
print(f"Current Platform: {sys.platform}\n")

# Print out the version of Python you're using:
print(f"Current Python version: {sys.implementation.version}\n")


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# Returns the `Effective Group` id of the current process
print(f"Current EG process ID: {os.getegid()}\n")

# Returns the `Real Group` id of the current process
print(f"Current RG process ID: {os.getgid()}\n")

# Print the current working directory (cwd):
# YOUR CODE HERE

# Print out your machine's login name
# YOUR CODE HERE
