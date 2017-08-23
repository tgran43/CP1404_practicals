"""Trey Grant"""

def main():
    name = get_name()
    print_parts(name)


def print_parts(name, step=2):
    print(name[::step])


def get_name():
    name = input("Name: ")
    while name == "":
        print("Invalid name.")
        name = input("Name: ")
    return name


main()
