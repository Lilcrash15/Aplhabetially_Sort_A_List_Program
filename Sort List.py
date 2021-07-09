title = input("Enter Text: ")
# Breakdown the text into a list of words
words = title.split(", ")
# sort the list
words.sort()
# Write to a file
f = open("GameList.txt", "w",)
f.write(str(words))
f.close()
# display the words
for word in words:
    f = open("GameList.txt", "r")
    print(words)