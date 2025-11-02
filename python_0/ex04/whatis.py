import sys

args = sys.argv

if (len(args) < 2):
    exit (1)
elif (len(args) > 2):
    print("more than one argument is provided")
    exit (1)
try:
    nbr = int(args[1])
except:
    print("argument is not an integer")
    exit (1)

if (nbr % 2 == 0):
    print("I'm Even")
else:
    print("I'm Odd")
    

print(nbr)