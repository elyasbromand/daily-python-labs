try:
    x = int(input("What's x? "))
    
except ValueError:
    print ("X is not a valid integer.")

print(f"X is {x}")


# In the code above if the input from the user is something other than integer then we will have the value error in the except 
# block and the program will print "X is not a valid integer." and then it will try to print the value of x but since x is not 
# defined in the except block it will raise another error which is UnboundLocalError. To avoid this we can initialize x with a 
# default value before the try block.