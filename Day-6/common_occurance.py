'''
give a string , which is the company name in lowerrcase leters, your task is to find the top three most common letters in the string.
print the three most common characters along with their occurence sount.
sort in descending order of occurence count.
if the occurrence countis the same, sort the chars in alphabetical order.

input format:
aabbbccdef

output format:
b 3
a 2
c 2
'''

a = input()

frequency = {}

for ch in a:
    frequency[ch] = frequency.get(ch, 0) + 1

result = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))

for i in range(3):
    print(result[i][0], result[i][1])
