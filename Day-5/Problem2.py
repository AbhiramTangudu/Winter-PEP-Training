''' sample problem 
Input: 'Abhineha
output: ['a]'''

x = (input("Enter a string: "))

result = []

for i in x:
    if x.count(i) > 1 and i not in result:
        result.append(i)

print("Repeated chars: ", result)


     