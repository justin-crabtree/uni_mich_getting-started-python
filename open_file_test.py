# fname = input("Enter file name: ")
# fh = open(fname)
# print(fh.read().upper().rstrip())


fname = input("Enter file name: ")
fh = open(fname)
added_data = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1 
    num_data = float(line[20:])
    added_data = num_data + added_data

print("Average spam confidence:", added_data / count)