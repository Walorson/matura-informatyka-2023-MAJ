plik = open("bin.txt")
wiersze = plik.readlines()

def decimal(n):
    return int(str(n), 2)

for wiersz in wiersze:
    wiersz = wiersz.strip()

    print(str(bin(decimal(wiersz) ^ decimal(wiersz) // 2))[2:])