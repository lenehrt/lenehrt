

# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
fh = open('mbox_short.txt')
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.rstrip()
    line = float(line.strip('X-DSPAM-Confidence:    '))
    count += 1
    total = total + line
ave = total/count
print(f"Average spam confidence: {ave}")
