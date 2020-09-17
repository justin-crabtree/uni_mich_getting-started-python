# hrs = input("Enter Hours: ")
# rate = input("Enter Rate: ")

# pay = float(hrs) * float(rate)

# print("Pay: ", pay)



# hours = input("Enter Hours: ")
# h = float(hours)
# rate = input("Enter your rate per hour: ")
# r = float(rate)
# overtimeRate = 1.5 * r
# hourlyRate = h * r

# if h > 40 :
#   overtimeHours = h - 40
#   overtimeTotal = overtimeHours * overtimeRate + 420
#   print(overtimeTotal)
# else :
#   print("Your pay for the week is:", h * r)



hours = float(input("Enter Hours: "))
rate = float(input("Enter your rate per hour: "))
overtimeRate = 1.5 * rate

def computepay(hours, rate):
  if hours > 40 :
    overtimeHours = hours - 40
    overtimeTotal = overtimeHours * overtimeRate + 420
    print("Pay", overtimeTotal)
    return
  else :
    print("Pay", hours * rate)
    return

computepay(hours, rate)