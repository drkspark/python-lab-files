a = []

n = int(input("Enter number if Elements : "))

for i in range(n):
    b = int(input("Enter element : "))
    a.append(b)

a.sort()
print("Largest element is ",a[n-1])