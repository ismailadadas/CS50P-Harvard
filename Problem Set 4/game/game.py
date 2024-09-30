import random 

keepLooping = True
while keepLooping :
    try:
        n = int(input("Level: "))
        num = random.randint(1, n)
        guess = int(input("Guess "))

        if num < guess:
            print("too large!")

        elif num > guess:
            print("too small!")

        elif num == guess: 
            print("just right!")
            keepLooping = False

    except ValueError:
        continue 
