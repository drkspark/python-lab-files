x = input("Enter file name : ")
f = open(x,"r")
for i in f:
    print(i[ : : -1])