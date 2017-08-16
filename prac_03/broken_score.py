"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))

    print_score(score)


def print_score(score):
    if score > 100 or score < 0:
        print("Invalid Score")
    elif score >= 90:
        print("Excellent Score")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
