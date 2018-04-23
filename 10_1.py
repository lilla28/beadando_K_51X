def osthato():
    szam=20
    while True:
        db = 0
        for i in range(1,21):
            if szam%i==0:
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


