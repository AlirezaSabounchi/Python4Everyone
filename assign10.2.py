fhand = open("mbox-short.txt")
hours = dict()
for line in fhand :
    if line.startswith("From") and not line.startswith("From:"):
        words = line.split()
        time = words[5]
        hour = time[:2]
        hours[hour] = hours.get(hour , 0) + 1
[print(k,v) for k,v in sorted(hours.items())]
