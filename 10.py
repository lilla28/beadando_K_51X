#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? 
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
