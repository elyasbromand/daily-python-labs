def main(): 
    print_column(3)

def print_column(height):
    # print("#\n" * height, end="")
    for _ in range(height):
        if _ == 1:
            print("#   ", print_rows(3))
        else:
            print("#")
def print_rows(width):
    # print("?" * width)
    string = "?" * width
    return string

main()