fname = input("Enter file name: ")
fhand = open(fname)
count = 0
accu = 0
for line in fhand :
    if line.startswith("X-DSPAM-Confidence:") :
        count += 1
        accu += float(line[19:].rstrip())
        print(accu , count)
avg = accu / count
print("Average spam confidence: " , avg)
