#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? 
def oszthato():
    szam=1
    while True:
        db=0
        for oszto in range(11,21):
            if szam%oszto>0:
                szam=szam+1
            else:
                db=db+1
        if db==10:
            return szam
print('a legkisebb szam, amely osztahato 1-20-ig maradék nélkül:',oszthato())
#kb 40ms futasi ido
