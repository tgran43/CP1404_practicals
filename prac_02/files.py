user_name = input("Please enter your name: ")
out_file = open('name.txt', 'w')
print(user_name, file=out_file)
out_file.close()

in_file = open('name.txt', 'r')
print("Your name is ", in_file.read())
in_file.close()

sum_of_numbers = 0
in_file = open('numbers.txt', 'r')
for i in in_file.readlines():
    sum_of_numbers += int(i)
print(sum_of_numbers)
