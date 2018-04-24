def oszto():
    szam=20
    while True:
        if szam%20==0 and szam%19==0 and szam%18==0 and szam%17==0 and szam%16==0 and szam%15==0 and szam%14==0 and szam%13==0 and szam%12==0 and szam%11==0:
            return szam
        else:
            szam=szam+1

print(oszto())