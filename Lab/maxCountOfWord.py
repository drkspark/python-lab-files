count  = 0
word = ""
maxCount = 0
words = []
file1 = input("Enter file Name : ")
file = open(file1,"r")

for i in file:
    string = i.lower().replace(',',' ').replace('.',' ').split(' ')

    for s in string:
        words.append(s)

# print(words)    
uniqueWords = []

for x in words:
    if x not in uniqueWords:
        uniqueWords.append(x)

# print(uniqueWords)
for  i in uniqueWords:
    if i == ' ':
        continue
    count = 0
    for j in range(len(words)):
        if i == words[j]:
            count += 1
    
    if count > maxCount:
        maxCount = count
        word = i

print("The most frequent word is ",word)
file.close()