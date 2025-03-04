plik = open("pi.txt")
wiersze = plik.readlines()

wiersze = [x.strip() for x in wiersze if x.strip() != ""]

ile = 0
for i in range(0, len(wiersze)):
        if i < len(wiersze) - 1 and int(wiersze[i] + wiersze[i+1]) > 90:
            ile += 1

print(ile)