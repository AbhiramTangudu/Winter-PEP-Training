def recu(a, b, limit):
    #a,b = 0, 1
    if (a > limit):
        return
    print(a, end=" ")
    recu(b, a+b, limit)

n = int(input("enter the number: "))
recu(0, 1, n)