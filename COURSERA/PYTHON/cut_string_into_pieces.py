a = "I'm glad I know sign language, it's pretty handy."

atpos = y.find(' ')
sppos = y.find('.', atpos)

host = y[atpos+1 : sppos]
print(host)
