name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name) # open the file

counts = {}

for line in handle: # build a list and each line is a item on the list
    line = line.rstrip() # remove the \n at the end of line and make each line a item on the list
    if line.startswith('From: ') : # look for items on the list and the ones that starts with From continue
        words = line.split() #split items that are lines into individual words. Now each line is a list with worst as items.
        email = words[1]  # email = to second item on the list
        counts[email] = counts.get(email,0) +1  #in the dicionary "counts" make the value (key is email) = get an item in the dictionary with email as key if not add the email as key and the value store it as 0 then make it + 1.

largernumber = None
mostusedemail = None

for email, count in counts.items(): # for loop keys and value (email is keys) and (count is value) simontanestly
    if largernumber is None or count > largernumber: # make key equals the largers and value
        mostusedemail = email
        largernumber = count

print(mostusedemail, largernumber)
        