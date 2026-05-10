def setOrNot(num, n):
    if (num & (1 << (n - 1))):
        print("\n SET")

    else:
        print("\n NOT SET")

num = int(input("Enter a number: "))
n = int(input("Enter the bit position to check: "))

setOrNot(num, n)
