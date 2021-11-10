
n = int(input("Enter the number of primes : "))
i = 2

while n:
    c = 0
    for j in range(2,i+1):
        if i%j == 0:
            c += 1 # This stores number of times the number was divided
    
    # If it was divided only once, then it will be a Prime
    if c == 1 :
        print(i, end = " ")
        n -= 1
    
    i += 1