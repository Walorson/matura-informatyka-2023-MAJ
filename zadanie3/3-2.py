plik = open("pi.txt")
wiersze = plik.readlines()

wiersze = [x.strip() for x in wiersze if x.strip() != ""]
czlony = []

najmniej = 10000 #10000 to tyle jest liczb po przecinku
najmniej_liczba = None
najwiecej = 0
najwiecej_liczba = None

for i in range(0, 10):
    for j in range(0, 10):
        czlony.append(str(i)+str(j))

pi = "".join(wiersze)
for czlon in czlony:
    ile = pi.count(czlon)
    if ile > najwiecej:
        najwiecej = ile
        najwiecej_liczba = czlon

    if ile < najmniej:
        najmniej = ile
        najmniej_liczba = czlon

#runda druga (która liczba spośród tych najmniej licznych występuje jako pierwsza)
for czlon in czlony:
    if pi.count(czlon) == najmniej:
        najmniej_liczba = czlon
        break

print(najmniej_liczba, najmniej)
print(najwiecej_liczba, najwiecej)
print(pi)