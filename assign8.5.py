fhand = open("mbox-short.txt")
count = 0
adress = list()
for line in fhand:
    if line.startswith("From") and not line.startswith("From:"):
        ad = line.split()[1]
        print(ad)
        count += 1
#        if ad not in adress :
#            adress.append(ad)

print("There were" , count, "lines in the file with From as the first word")
