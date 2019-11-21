# sortowanie liczb
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = float(input("Podaj trzecią liczbę: "))
mx = 0
if a > b and a > c:
    mx = a
elif b > c:
    mx = b
else:
    mx = c
print (mx)
