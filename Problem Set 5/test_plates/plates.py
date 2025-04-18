def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Length must be between 2 and 6
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: First two characters must be letters
    if not s[:2].isalpha():
        return False

    # Rule 3: Numbers must come at the end (if present)
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0':
                return False  # First number cannot be 0
            if not s[i:].isdigit():
                return False  # All characters after first number must be digits
            break

    # Rule 4: No periods, spaces, or punctuation allowed
    if not s.isalnum():
        return False

    return True


if __name__ == "__main__":
    main()
