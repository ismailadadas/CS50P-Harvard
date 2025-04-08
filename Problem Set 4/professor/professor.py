import random

def main():
    score = 0
    level = get_level()
    
    for _ in range(10):
        x, y = generate_integer(level)
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
            print(f"Correct answer: {x + y}")
    
    print(f"Score: {score}/10")


def get_level():
    while True:
        try:
            level = int(input("Level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    else:
        raise ValueError("Invalid level")
    return x, y


if __name__ == "__main__":
    main()