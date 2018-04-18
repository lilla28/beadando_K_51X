#1
szoveg=input('Adjon meg egy szöveget: ')
lista=szoveg.split(' ')
print(lista)
for szo in lista:
    print(szo[1:]+szo[0]+'ay',end=" ")
#2
def piglatin(szoveglista):
    for szo in szoveglista:
        print( szo[1:]+szo[0]+'ay',end=' ')
szoveg=input('Adjon meg egy szöveget:')
szoveglista=szoveg.split(' ')
piglatin(szoveglista)


