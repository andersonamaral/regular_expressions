import re
hand = open('/home/anderson/Desktop/mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if re.search('^From:', line) :
        print (line)

