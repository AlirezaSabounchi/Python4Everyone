import re
print(sum([int(i) for i in re.findall('[0-9]+' , open("regex_sum_42.txt").read())]))
