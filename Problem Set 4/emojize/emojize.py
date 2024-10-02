import emoji

answer = input("input: ")

emoji = emoji.emojize(answer, language='alias')

print("Output:", emoji)