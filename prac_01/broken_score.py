"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score > 100 or score < 0:
    print("Invalid Score")
elif score >= 90:
    print("Excellent Score")
elif score >= 50:
    print("Passable")
else:
    print("Bad")

