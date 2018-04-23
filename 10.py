def oszthato():
    oszto=1
    szam=1
    while oszto!=20:
        db=0
        if szam%oszto>0:
            szam=szam+1
        if szam%oszto==0:
            db=db+1
            oszto = oszto + 1
        print(db)
        # if db==20:
        #     return szam
oszthato()
# print('A legkisebb pozitív egész szám, amely osztható 1-20-ig:',oszthato())