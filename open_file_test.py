# fname = input("Enter file name: ")
# fh = open(fname)
# print(fh.read().upper().rstrip())

# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.


fname = input("Enter file name: ")
fh = open(fname)
sum_data = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1 
    num_data = float(line[20:])
    sum_data = num_data + sum_data

print("Average spam confidence:", sum_data / count)