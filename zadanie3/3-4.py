plik = open("pi.txt")
wiersze = plik.readlines()

wiersze = [x.strip() for x in wiersze if x.strip() != ""]

ile = 0
najwiekszy = ""
miejsce_najwiekszy = 0

for i in range(0, len(wiersze)):
    dlugosc_ciagu = 0
    ciag = wiersze[i]
    miejsce = i + 1
    
    for j in range(i, i + 6):
        if j + 1 >= len(wiersze):
            break

        if wiersze[j] <= wiersze[j + 1]:
            dlugosc_ciagu += 1
            ciag += wiersze[j + 1]
        else:
            break

    if dlugosc_ciagu == 0: #ciąg nie jest rosnący już na starcie, nie ma sensu szukać dalej (przejdźmy do kolejnej iteracji)
        continue

    for j in range(i + dlugosc_ciagu, len(wiersze)):
        if j + 1 >= len(wiersze):
            break

        if wiersze[j] > wiersze[j + 1]:
            dlugosc_ciagu += 1
            ciag += wiersze[j + 1]
        else:
            break

    if len(ciag) > len(najwiekszy):
        najwiekszy = ciag
        miejsce_najwiekszy = miejsce

print(najwiekszy, miejsce_najwiekszy)