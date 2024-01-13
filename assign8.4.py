fhand = open("romeo.txt")
words = list()
for line in fhand :
    split_line = line.rstrip().split()
    for word in split_line :
        if word not in words :
            words.append(word)
words.sort()
print(words)
