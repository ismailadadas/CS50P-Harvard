#user input
jawaban = input("the Great Question of Life, the Universe and Everything? ")

#print Yes kalo user inpu 42 atau forty-two / forty two
if jawaban.strip() == "42":
    print("Yes")
elif jawaban.lower().strip() == "forty-two":
    print("Yes")
elif jawaban.lower().strip() == "forty two":
    print("Yes")

# Otherwise output No
else :
    print("No")
