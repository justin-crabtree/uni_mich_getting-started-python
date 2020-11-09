# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# handle = open("mbox-short.txt")
# counts = dict()
# for line in handle:
#   line = line.rstrip()
#   if not line.startswith('From ') : continue
#   words = line.split()
#   for word in words:
#     counts[word] = counts.get(word,0) + 1
    

# bigcount = None
# bigword = None
# for word,count in counts.items():
#   if bigcount is None or count > bigcount:
#     bigword = word
#     bigcount = count
# print(bigword, bigcount)

# handle = open("mbox-short.txt")
# counts = dict()
# for line in handle:
#   line = line.rstrip()
#   words = line.split()
#   if len(words) < 3 or words[0] != 'From' :
#     continue
#   counts['email'] = words[1]
#   print(counts['email'])

name = open('mbox-short.txt')

email = dict()

for line in name:
  line.rstrip()
  if not line.startswith("From "): continue
  words = line.split()
  email[words[1]] = email.get(words[1], 0) + 1

largest = None
largest_author = None

for key in email:
  if largest is None: largest = email[key]

  if largest < email[key]:
      largest = email[key]
      largest_author = key

print(largest_author, largest)
  
