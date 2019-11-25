# Choinka z trójkątów
tree = int(input("Podaj liczbę poziomów choinki: "))
for i in range(3,tree+3):
    for j in range(i):
        print("#" * (j+1))


