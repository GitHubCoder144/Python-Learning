print("#")
print("#")
print("#")

for _ in range(3):
    print("#")

def main():
    print_colum(3)
    print_row(4)
    print_square(3)

def print_colum(height):
    for _ in range(height):
        print("#")
#       print ("3\n" * height, ends=""")

def print_row(width):
    print("?" * width)

def print_square(size):
    # For each row in square
    for i in range(size):
        #For each brick in row
        for j in range(size):
            #print brick
            print("#", ends="")
        print()

def print_square(size):
    # For each row in square
    for i in range(size):
    print_row(size)

def print_row(width):
    print("#" * width)


main()

