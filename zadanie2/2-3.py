plik = open("bin.txt")
wiersze = plik.readlines()

def decimal(n):
    return int(str(n), 2)

najwiekszy = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()

    if decimal(wiersz) > decimal(najwiekszy):
        najwiekszy = wiersz

print(najwiekszy)