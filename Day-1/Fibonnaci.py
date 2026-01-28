def fibonacci_till(tail):
    a, b = 0, 1
    while a <= tail:
        print(a, end=" ")
        a, b = b, a + b

def main():
    
    num = int(input("Enter a number: "))

    if(num < 0):
        print("Enter a non negative number")
    else:
        fibonacci_till(num)

main()
