"""Trey Grant"""
def main():
    name = get_name()
    print(name[1::2])


def get_name():
    name = input('Please enter your name: ')
    while name == "":
        name = input('Please enter your name: ')
    return name


main()