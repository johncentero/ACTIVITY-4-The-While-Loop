#John Cen O. Tero
#BAET 2101

n = int(input("Enter n: "))

# Keep asking while n is not positive
while n <= 0:
    n = int(input("Enter n: "))

# Count down from n to 1 on one line
while n >= 1:
    print(n, end=" ")
    n -= 1

print("Liftoff!")