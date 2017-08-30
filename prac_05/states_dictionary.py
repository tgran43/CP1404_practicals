"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# # TODO: Reformat this file so the dictionary code follows PEP 8 convention
# STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
#                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# # print(STATE_NAMES)
#
# state = input("Enter short state: ").upper()
# while state != "":
#     if state in STATE_NAMES:
#         print(state, "is", STATE_NAMES[state])
#     else:
#         print("Invalid short state")
#     state = input("Enter short state: ").upper()
#
# for short_state,state in STATE_NAMES.items():
#     print("{:3} is {}".format(short_state,state))
#
COLOUR_CODES = {"gray: #bebebe", "gray1: #030303", "gray10: #1a1a1a", "gray11: 1c1c1c", "gray12: #1f1f1f",
                "gray13: #212121", "gray14: #242424", "gray15: #262626", "gray16: #292929", "gray17: #2b2b2b"}
colour = input("Enter colour name: ").lower()
while colour != "":
    if colour in COLOUR_CODES:
        print(colour, "is", COLOUR_CODES[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour name: ").lower()
for color,colour_code in COLOUR_CODES.items():
     print("{:3} is {}".format(color,colour_code))