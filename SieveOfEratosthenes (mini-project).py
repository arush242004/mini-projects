def lstprod(n):
    lst = []
    for i in range(n):
        lst.append(i)
    lst.pop(1)
    lst.pop(0)
    return lst


def sieve(lon):
    for n in lon:
        for n1 in lon:
            if n1%n==0 and n1!=n:
                lon.remove(n1)
    return lon

print(sieve(lstprod(n))) ## <------- Type in the number up till which you want all the prime factors to. 

## DO NOT TYPE IN LARGE NUMBERS THOUGH (unless NASA let you borrow their computer).
## (And I'm talking about 5 to even +12 digit long numbers!!!).              
