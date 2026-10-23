#John Cen O. Tero
#BAET 2101

CORRECT_PIN = "1234"
tries = 0
granted = False

while tries < 3 and not granted:
    pin = input("PIN: ")
    if pin == CORRECT_PIN:
        granted = True
    else:
        tries += 1

if granted:
    print("Access granted")
else:
    print("Card blocked")
