# sys is the module to access command-line arguments
import sys


# sys.exit(message) will exit prematurely with an error message
while True:
    try:
        print ("hello, my name is", sys.argv[1])
        break
    except IndexError:
        sys.exit("Add an argument after program name")


# The above code will go into infinite loop if no argument is provided