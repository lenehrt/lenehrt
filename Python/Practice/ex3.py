hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)
if h <= 40 :
    pay = h*r
if h > 40 :
    pay = ((h - 40) * (r * 1.5)) + (40 * r)
print(pay)
