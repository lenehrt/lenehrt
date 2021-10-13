fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
output = list()

for line in fh:
    line = line.rstrip()
    if line.startswith('From: ') :
        words = line.split()
        email = words[1]
        print(email)
        output.append(email)
    else:
        continue
    
count = len(output)

print("There were", count, "lines in the file with From as the first word")
