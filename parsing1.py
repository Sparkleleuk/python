# Parsing string exercise 

def parse(msg):
    sppos = msg.find(' ')
    atpos = msg.find('@')
    name = msg[sppos+1:atpos]
    return name

msg = raw_input('Enter message: ')
name = parse(msg)
print name

