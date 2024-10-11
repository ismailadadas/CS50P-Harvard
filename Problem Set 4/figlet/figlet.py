import sys
import random
from pyfiglet import Figlet

def main():
    # Initialize the Figlet object
    figlet = Figlet()

    # Get the list of available fonts
    available_fonts = figlet.getFonts()

    # Check if the user provided 0 or 2 command-line arguments
    if len(sys.argv) == 1:
        # No font specified, use a random font
        font = random.choice(available_fonts)
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        # Check if the specified font is valid
        font = sys.argv[2]
        if font not in available_fonts:
            sys.exit("Invalid usage: Font not found")
    else:
        # Invalid usage, exit with error message
        sys.exit("Invalid usage: Use 0 or 2 command-line arguments")

    # Prompt the user for input text
    user_input = input("Input text: ")

    # Set the desired font and render the text
    figlet.setFont(font=font)
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()
