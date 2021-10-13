largest = -1
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    if smallest is None :
        smallest = num
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
