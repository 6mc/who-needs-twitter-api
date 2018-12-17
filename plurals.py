import random

fp = open('fixed.txt') # Open file on read mode
lines = fp.read().split("\n") # Create a list containing all lines
fp.close()

straw = lines[random.randint(0,len(lines)-1)]    
berry = lines[random.randint(0,len(lines)-1)] 

fh = open('tweet2send.txt', 'w')
fh.write(straw.split("are")[0]+'are'+berry.split("are")[1])
fh.close()