#John Cen O. Tero
#BAET 2101

count = 0
total = 0.0

price = float(input("Price (0 to stop): "))

# 0 is the sentinel value

while price != 0:
    count += 1
    total += price
    price = float(input("Price (0 to stop): "))

print(f"Items: {count}  Total: {total:.2f}")

if count > 0:
    print(f"Average: {total / count:.2f}")
else:
    print("Average: 0.0")
