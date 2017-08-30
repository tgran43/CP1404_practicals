COLOUR_CODES = {"gray": "#bebebe", "gray1": "#030303", "gray10": "#1a1a1a", "gray11": "#1c1c1c", "gray12": "#1f1f1f",
                "gray13": "#212121", "gray14": "#242424", "gray15": "#262626", "gray16": "#292929", "gray17": "#2b2b2b"}
colour = input("Enter colour name: ").lower()
while colour != "":
    if colour in COLOUR_CODES:
        print(colour, "is", COLOUR_CODES[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour name: ").lower()
for color, colour_code in COLOUR_CODES.items():
    print("{:6} is {}".format(color, colour_code))

