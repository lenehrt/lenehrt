name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = {}

for line in handle:
    if line.startswith('From '):
        line = line.split()
        line = line[5]
        line = line[0:2]
        counts[line] = counts.get(line,0) +1

listoftoples = []

for key, value in counts.items():
    listoftoples.append((key, value))
  
listoftoples.sort()

for key, value in listoftoples:
    print(key, value)
