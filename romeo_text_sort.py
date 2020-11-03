# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.

fileHandle = open('romeo.txt')
lst = list()
for line in fileHandle:
  words = line.rstrip().split()
  lst.append(words)
lst = lst[0] + lst[1] + lst[2] + lst[3]
lst.sort()
new_list = list(dict.fromkeys(lst))
print(new_list)

