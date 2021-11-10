f1 = open("src.txt","r")
f2 = open("resultant.txt","w")

x = f1.read()
f2.write(x) # Writing  to the file

# Closing the files
f2.close()
f1.close()
