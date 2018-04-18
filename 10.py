def oszthato():
    n=1
    szam=1
    db=0
    while n!=20:
        if szam%n>0:
            szam=szam+1
        elif szam%n==0:
            db=db+1
            n = n + 1
            break
        return szam

print('A legkisebb pozitív egész szám, amely osztható 1-20-ig:',oszthato())