import inflect

p = inflect.engine()

names = []

# Input loop to collect names
while True:
    try:
        name = input("Name: ")
        names.append(name)  # Corrected typo from apppend to append
    except EOFError:  # Control-D (EOF) to stop input
        print()
        break

# Using inflect engine to join names
output = p.join(names)

# Output the result
print("Adieu, adieu, to " + output)
