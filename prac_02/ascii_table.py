# LOWER_BOUNDARY = 33
# UPPER_BOUNDARY = 127
#
# letter = input('Enter a character: ')
# ascii_code = ord(letter)
# print('The ASCII code for {} is {}'.format(letter,ascii_code))
#
# ascii_number = int(input('Enter a number between {} and {}'.format(LOWER_BOUNDARY,UPPER_BOUNDARY)))
# while ascii_number < 33 or ascii_number > 127:
#     ascii_number = int(input('Enter a number between {} and {}'.format(LOWER_BOUNDARY, UPPER_BOUNDARY)))
# ascii_letter = chr(ascii_number)
# print('The character for {} is {}'.format(ascii_number,ascii_letter))

for i in range(33,128):
    character = chr(i)
    print('{0:<3}{1:>3}'.format(i,character))
