fhand = open('romeo.txt')
counts = dict()
for line in fhand:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
  newtuple = (val, key)
  lst.append(newtuple)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
  print(key, val)