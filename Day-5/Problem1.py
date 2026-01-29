'''replace the selected letter by another letter
take input str from user 
ask user, "which character you want to replace.
which value it should be replaced with
print the final replaced string
str = "abcdefgh
output = "abcxefgh'''

str = (input("Enter a string: "))
a = (input("letter you want to replace: "))
r = input("Replace with: ")

x = str.replace(a, r)

print(x)