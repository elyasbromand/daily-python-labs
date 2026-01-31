# Starting point
def main():
    number = get_number()
    meow(number)

# Get a positive integer
def get_number():
    while True:
        number = int(input("Enter a number: "))
        if number > 0:
            return number

# print Meow number times
def meow(times):
    print("Meow\n" * times, end="")


main()
