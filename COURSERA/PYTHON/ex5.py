hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)

def computepay(h, r):
    if h <= 40 :
        result = h*r
    if h > 40 :
        result = ((h - 40) * (r * 1.5)) + (40 * r)
    return result

p = computepay(h, r)

print("Pay", p)
