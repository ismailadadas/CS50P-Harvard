import random
# This brings in Python's built-in random module so we can generate random numbers

def main():
    # def main() itu main function / main function, where the program starts running
    score = 0
    # bikin variable score to count how many answers you get right
    level = get_level()
    # We call the function get_level() to ask the user to choose difficulty (Level 1, 2, or 3).
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 0

        while tries < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            tries += 1
        else:
            print(f"{x} + {y} = {x + y}")

    print(score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")


if __name__ == "__main__":
    main() 