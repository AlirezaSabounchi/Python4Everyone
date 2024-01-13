fhand = open("mbox-short.txt")
dic = dict()
for line in fhand :
    if line.startswith("From") and not line.startswith("From:"):
        word = line.split()
        if word[1] not in dic.keys() :
            dic[word[1]] = 1
        else :
            dic[word[1]] += 1
temp = 0
for key,value in dic.items():
    if value > temp :
        max = key
        temp = value
    else :
        continue
print (max , temp)
