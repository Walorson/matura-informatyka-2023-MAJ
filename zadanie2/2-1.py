def bin(n):
    ilosc_blokow = 0
    block_id = None
    
    while n > 0:
        liczba = n % 2

        if block_id != liczba:
            block_id = liczba
            ilosc_blokow += 1  

        n //= 2

    return ilosc_blokow

print(bin(245))