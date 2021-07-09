print("Type the list you would like sorted and separated each item with a , e.g. Milk, Eggs, Cheese,")
print("The sorted list will be placed in the same location as this program. \nThe file name will be 'List.txt'")
print("***WARNING*** When you create a new list it will overwrite your previous list. \nBe sure to rename or move any previous list(s) you have created.")
title = input("Enter Text: ")
# Breakdown the text into a list of words
words = title.split(", ")
# sort the list
words.sort()
# Write to a file
f = open("List.txt", "w",)
f.write(str(words))
f.close()
# display the words
for word in words:
    f = open("List.txt", "r")
    print(words)
print("Your list has been sorted.")
input("Press Enter to close the program")