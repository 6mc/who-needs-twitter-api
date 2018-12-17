import sys
print(sys.argv[1])

fp = open(sys.argv[1]+'tweets.txt') # Open file on read mode
lines = fp.read().split("\n") # Create a list containing all lines
fp.close()
fh = open(sys.argv[1]+"fixed.txt", "a")
for x in lines:
    words = x.split(" ")
    if sys.argv[1] in x:    
         for y in words:
             if "http" not in y and "RT" not in y and "@" not in y: 
                 fh.write(" " +y)
         fh.write("\n")
fh.close()
# open(sys.argv[1]+'tweets.txt', 'w').close()





import random

fp = open(sys.argv[1]+'fixed.txt') # Open file on read mode
lines = fp.read().split("\n") # Create a list containing all lines
fp.close()

straw = lines[random.randint(0,len(lines)-1)]    
berry = lines[random.randint(0,len(lines)-1)] 

fh = open(sys.argv[1]+'tweet2send.txt', 'w')
fh.write(straw.split(sys.argv[1])[0]+sys.argv[1]+berry.split(sys.argv[1])[1])
fh.close()