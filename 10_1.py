def osthato():
    szam=20 #szam amelytol indulni fog a szamlalas
    while True:# ciklus amely addig fut amig a megfelelo erteket meg nem talalja
        db = 0 # valtozo az osztok darabszamanak szamlalasara
        for i in range(1,21):#osztas ciklusa
            if szam%i==0:#feltelek:
                db=db+1
            if szam%i>0:
                szam=szam+1
        if db==20:
            return szam

# print(osthato())
def main():
    print(osthato())
if __name__ == '__main__':
    main()
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

