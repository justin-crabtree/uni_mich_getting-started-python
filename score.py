score = float(input("Enter Score: "))


if score < 0.0 or score > 1.0 :
  print("Error: Please print a score between 0.0 and 1.0")
elif score >= 0.9 :
  print("A")
elif score >= 0.8 :
  print("B")
elif score >= 0.7 :
  print("C")
elif score >= 0.6 :
  print("D")
elif score < 0.6 :
  print("F")