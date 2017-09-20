from prac_07.guitars import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Bob", 2010, 3)

print("{} get_age() - Expected 95. Got {}".format(guitar.name, guitar.get_age()))
print("{} get_age() - Expected 7. Got {}".format(guitar2.name, guitar2.get_age()))

print("{} is_vintage - Expected True. Got {}".format(guitar.name, guitar.is_vintage()))
print("{} is_vintage - Expected False. Got {}".format(guitar2.name, guitar2.is_vintage()))
