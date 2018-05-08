#Write function that translates a text to Pig Latin and back. English is translated to Pig Latin by taking the first letter of every word, moving it to the end of the word and adding ‘ay’. “The quick brown fox” becomes “Hetay uickqay rownbay oxfay”.
#1. megoldas 
a=input('A:english to piglatin or B:piglatin to english(A/B):')
a=a.upper()
if a=='A':
    szoveg=input('Adjon meg egy szöveget angolul: ')
    lista=szoveg.split(' ')
    #print(lista)
    for szo in lista:
        print(szo[1:]+szo[0]+'ay',end=" ")
elif a=='B':
    szoveg = input('Adjon meg egy szöveget pig latin nyelven: ')
    lista = szoveg.split(' ')
    #print(lista)
    for szo in lista:
        szo=szo[0:len(szo)-2]
        print(szo[-1]+szo[0:len(szo)-1],end=' ')
else:
    print('érvénytelen karakter')

