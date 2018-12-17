fp = open('fixed.txt') # Open file on read mode
lines = fp.read().split("\n") # Create a list containing all lines
fp.close()
fh = open("tweets.txt", "a")
for x in lines:
    if "are" in x and "http" not in x and "RT" not in x and "@" not in x:
        fh.write("\n" +x)
fh.close()
open('fixed.txt', 'w').close()