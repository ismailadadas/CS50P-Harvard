def main():
    greeting = input("Greeting: ").strip().lower()
    compromise(greeting)

def compromise(greeting):
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h") and not greeting.startswith("hello") :
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()

