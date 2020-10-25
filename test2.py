text = "X-DSPAM-Confidence:    0.8475"
beginning = text.find(':')
end = text[-1]
result = float(text[beginning+1 : 50].strip())

print(result)