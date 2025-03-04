plik = open("pi.txt")
wiersze = plik.readlines()

wiersze = [x.strip() for x in wiersze if x.strip() != ""]

ile = 0
ciagi6 = []

for i in range(0, len(wiersze)):
    dlugosc_ciagu = 0
    ciag = wiersze[i]
    
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

    for j in range(i + dlugosc_ciagu, i + 5):
        if j + 1 >= len(wiersze):
            break

        if wiersze[j] > wiersze[j + 1]:
            dlugosc_ciagu += 1
            ciag += wiersze[j + 1]
        else:
            break

    if len(ciag) == 6:
        if int(ciag[0]) < int(ciag[1]) and int(ciag[5]) < int(ciag[4]):
            ile += 1
            ciagi6.append(ciag)

print(ile)
print(ciagi6)