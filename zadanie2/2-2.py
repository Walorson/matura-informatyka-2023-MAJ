plik = open("bin.txt")
wiersze = plik.readlines()

def bin(n):
    n = int(str(n), 2) #zamieniam taktycznie na liczbe dziesiętną xD
    ilosc_blokow = 0
    block_id = None
    
    while n > 0:
        liczba = n % 2

        if block_id != liczba:
            block_id = liczba
            ilosc_blokow += 1  

        n //= 2

    return ilosc_blokow


ile = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()

    if bin(int(wiersz)) <= 2:
        ile += 1

print(ile)