def main():
    name = input("Enter your name: ")
    hello(name)

def hello(to = "World"):
    print("Hello,", to)

main()