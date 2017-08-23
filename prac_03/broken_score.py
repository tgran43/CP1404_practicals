"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))

    print(return_score(score))


def return_score(score):
    if score > 100 or score < 0:
        return ("Invalid Score")
    elif score >= 90:
        return ("Excellent Score")
    elif score >= 50:
        return ("Passable")
    else:
        return ("Bad")


main()
