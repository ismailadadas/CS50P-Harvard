def main():
    user_input = input("Input: ")
    print("Output:", shorten(user_input))


def shorten(word):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in word if char not in vowels])


if __name__ == "__main__":
    main()
