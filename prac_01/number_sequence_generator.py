from math import sqrt
lower_boundary = int(input("Enter lower boundary number: "))
upper_boundary = int(input("Enter upper boundary number: "))

choice = int(input("1. Show even numbers from x to y\n2. Show odd numbers from x to y\n3. Show the squares from x to y\
                    n4. Enter new boundaries\n5. Exit the program\n"))
while choice != 5:
    if choice == 1:
        for i in range(lower_boundary,upper_boundary + 1):
            if i % 2 == 0:
                print(i,end=" ")

    elif choice == 2:
        for i in range(lower_boundary, upper_boundary + 1):
            if i % 2 == 1:
                print(i, end=" ")

    elif choice == 3:
        for i in range(lower_boundary, upper_boundary + 1):
            if sqrt(i) % 2 == 0 or sqrt(i) % 2 == 1:
                print(i, end=" ")

    elif choice == 4:
        lower_boundary = int(input("Enter lower boundary number: "))
        upper_boundary = int(input("Enter upper boundary number: "))
    else:
        print("Invalid choice")
    choice = int(input(
        "\n1. Show even numbers from x to y\n2. Show odd numbers from x to y\n3. Show the squares from x to y\n4. Enter new boudries\n5. Exit the program\n"))




