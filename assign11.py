import re
sum = 0
fhand = open('regex_sum_1590640.txt')
for line in fhand :
    number = re.findall('[0-9]+' , str(line.split()))
    if number :
        for i in range(len(number)) :
            sum += int(number[i])
print(sum)
