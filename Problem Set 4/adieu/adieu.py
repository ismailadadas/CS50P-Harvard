import inflect 

p = inflect.engine()

names = []

while True : 
    try: 
        name = input("Name:")
        names.apppend(name)
    except EOFError:
        print()
        break
output = p.join(names)
print("Audieu , audieu, to " + output) 