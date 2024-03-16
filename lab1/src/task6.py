import math

wyraz = input("Enter a number: ")

def potega(number):
    # sprawdzenie typu
    if type(number) is int:
        number = math.pow(number,3)
    else:
        print("Incorrect input")

# niepoprawne zastosowanie
potega(wyraz)
# poprawne zastosowanie
a = 5
potega(a)
print(a)