B = [
    [None, 9],
    [None, 2, 12],
    [None, None, None, 10, 14],
    [None, None, None, None, None, None, None, 13, 15],
    [None] * 17
]

C = [
    [None, 10],
    [None, 8, 15],
    [None, 4, None, 12, None],
    [None, None, 6, None, None, None, 13, None, None],
    [None] * 17
]

def A(i, j, tablica):
    print(tablica[i][j])
    if tablica[i + 1][2*j - 1] != None:
        A(i + 1, 2*j - 1, tablica)
    if tablica[i + 1][2*j] != None:
        A(i + 1, 2*j, tablica)

A(0, 1, C)