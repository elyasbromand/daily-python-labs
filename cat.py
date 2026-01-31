def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        number = int(input("Enter a number: "))
        if number > 0:
            return number

def meow(times):
    print("Meow\n" * times, end="")


main()
