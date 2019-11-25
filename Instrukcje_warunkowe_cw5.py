#Twierdzenie Pitagorasa
t1 = int(input("Podaj długość pierwszego boku: "))
t2 = int(input("Podaj długość drugiego boku: "))
t3 = int(input("Podaj długość trzeciego boku: "))
a,b,c = 0,0,0
if t1>t2 and t1>t3:
    c = t1
    a = t3
    b = t2
elif t2>t3:
    c = t2
    a = t1
    b = t3
else:
    c = t3
    b = t2
    a = t1
if c < a+b:
    if (a**2 + b**2) == c**2:
        print("Trójkąt jest pitagorejski!")
        if a%3 == 0 and b%4 == 0 and c%5 == 0:
            print("Trójkąt jest egipski")
    else:
        print("Trójkąt nie jest pitagorejski")
else:
    print("Z podanych boków nie można zbudować trójkąta")
        
