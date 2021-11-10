import sys
a = sys.argv[1]

b = open(a, "r")

l=w=c=0

for i in b:
    words = i.split(" ")
    l += 1
    w += len(words)
    c += len(i)

print("Lines : ",l)
print("Words : ",w)
print("Characters : ",c)
