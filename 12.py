def prim(n):
    db=1
    for i in range(1,(n//2)+1):
        if n%i==0:
            db=db+1
    if db==2:
        return True
    return False
# print(prim(11))
def number():
    hanyadik=0
    szam=1
    while True:
        if hanyadik == 10001:
            return szam
        if prim(szam):
            hanyadik=hanyadik+1
            szam=szam+1
        else:
            szam=szam+1

print(number())
