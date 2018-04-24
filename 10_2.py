def oszto():#egy fv letrehozasa
    szam=20 #20 a legkisebb szam amelyrol inditom
    while True:#ciklus ahhoz hogy addig generaljon szamokat amig a feltetelek be nem teljesulnek
        if szam%20==0 and szam%19==0 and szam%18==0 and szam%17==0 and szam%16==0 and szam%15==0 and szam%14==0 and szam%13==0 and szam%12==0 and szam%11==0:#feltetel amely azert van 20-tol 11-ig mivel ezek az egyjegyu szamok tobbszorosei tehat peldaul ha oszthato 14-gyel akkor oszthato 7-tel
            return szam#a felteteleknek megfelelo szam 'visszaadasa'
        else:#ha nem teljesul a feltetel a teendo:
            szam=szam+1#noveljuk a szam erteket

print(oszto())#fuggveny meghivasa
#problema a programmal: a lassu futas es a feltetel 

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
