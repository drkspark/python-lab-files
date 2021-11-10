import sys
n = int(input("Enter n : "))
f = 0 #first
s = 1 # second

if(n == 1):
    print(f)
    sys.exit()

print(f,s,end=" ")

for i in range(3,n+1):
    new = f+s
    print(new, end=" ")
    f = s
    s = new