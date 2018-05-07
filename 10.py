#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? 
def oszthato():
    szam=1 #szam amelyet novelunk amig el nem oszthato 1-20ig
    while True:
        db=0 #valtozo,amely az osztok darabszamat tarolja
        for oszto in range(11,21):
            if szam%oszto>0: #feltetel: ha nem oszthato az adott szammal a ciklusbol akkor noveljuk meg az erteket, es kezdi elolrol a ciklust
                szam=szam+1
            else:
                db=db+1 #egyebkent a db szamot noveljuk
        if db==10:
            return szam #a vegso feltetel, amely kiirja a szamot ha osztoja 10(azert 10....)
print('a legkisebb szam, amely osztahato 1-20-ig maradék nélkül:',oszthato())
#kb 40ms futasi ido
