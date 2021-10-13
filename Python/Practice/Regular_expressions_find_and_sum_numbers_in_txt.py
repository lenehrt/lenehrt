import re

fname = input("Enter file name: ")
fh = open(fname)

nestedlist = []
empity = []

for line in fh:
    line = line.rstrip()
    linelist = re.findall('[0-9]+', line)
    if linelist != empity:
        nestedlist.append(linelist)

finallist = []
for item in nestedlist:
    for item2 in item:
        item2 = int(item2)
        finallist.append(item2)

i = 0
for index in finallist:
    i += 1

thesum = sum(finallist)

print(f'There are {i} values with a sum={thesum}')
