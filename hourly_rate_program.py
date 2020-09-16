# hrs = input("Enter Hours: ")
# rate = input("Enter Rate: ")

# pay = float(hrs) * float(rate)

# print("Pay: ", pay)

hours = input("Enter Hours: ")
h = float(hours)
rate = input("Enter your rate per hour: ")
r = float(rate)
overtimeRate = 1.5 * r
hourlyRate = h * r

if h > 40 :
  overtimeHours = h - 40
  overtimeTotal = overtimeHours * overtimeRate + 420
  print(overtimeTotal)
else :
  print("Your pay for the week is:", h * r)