def main(): 
    while True:
        x = get_number()
        if x < 0:
            print("Negative numbers are not allowed.")
            break
        else:
            print(f"You entered: {x}")
def get_number():
    return int(input("Enter a number: "))


main()