import numpy as np
import random
from timeit import default_timer as timer

tablica_1 = []
tablica_2 = []
tablica_3 = []

for i in range(0,5000):
    liczba = random.randint(1,10)
    tablica_1.append(liczba)
    tablica_2.append(liczba)
    tablica_3.append(liczba)

print(tablica_1)

def zadanie_1(tablica_1):

    i = len(tablica_1) - 1
    while(i > 0):
        if(tablica_1[i]- tablica_1[i-1] >= 0):
            i=i-1
        elif(tablica_1[i] - tablica_1[i-1] < 0):
            tablica_1[i], tablica_1[i-1] = tablica_1[i-1], tablica_1[i]
            i = len(tablica_1)-1


def zadanie_2(tablica_2):
    for i in range(0,len(tablica_2)):
        najmniejszy = 5000
        indeks = 0
        for j in range(i,len(tablica_2)):
            if(tablica_2[j] < najmniejszy):
                indeks = j
                najmniejszy = tablica_2[j]
        tablica_2[indeks] = tablica_2[i]
        tablica_2[i] = najmniejszy

def zadanie_3(tablica):

    mniejsze = []
    rowne = []
    wieksze = []

    if (len(tablica) > 1):
        pivot = tablica[0]

        for liczba in tablica:
            if liczba < pivot:
                mniejsze.append(liczba)
            if liczba == pivot:
                rowne.append(liczba)
            if liczba > pivot:
                wieksze.append(liczba)
        return zadanie_3(mniejsze) + rowne + zadanie_3(wieksze)
    else:
        return tablica






start = timer()
#zadanie_1(tablica_1)
end = timer()
print("Zadanie 1: ", " bardzo dużo ", "sekund")
print(tablica_1)

start = timer()
zadanie_2(tablica_2)
end = timer()
print("Zadanie_2: ", end - start, "sekund")
print(tablica_2)

start = timer()
zadanie_3(tablica_3)
end = timer()
print("Zadanie_3: ", end - start, "sekund")
print(zadanie_3(tablica_3))

