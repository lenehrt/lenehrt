
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
lstword = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
        else:
            continue
lst.sort()
    
print(lst)
    