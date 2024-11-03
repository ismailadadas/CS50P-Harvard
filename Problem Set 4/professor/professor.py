import random


def main():
    score = 0 
    no_of_tries = 0
    i = 0
    level = get_level()


def get_level():
    while True:

        try:
            level = int(input("Level: "))
            if level in [1,2,3,4]:
                return level
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):
    if level == 1: 
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.random.randint(100,999)
        y = random.random.randint(100,999)

if __name__ == "__main__":
    main() 