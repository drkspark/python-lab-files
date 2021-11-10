import sys

n = int(input("Enter n : "))

if( n == 0):
    print(1)
    sys.exit()

fac = 1
for i in range (1,n+1): # Remember to start thte loop from 1 to n+1
    fac *= i

print("The factorial is : ",fac)