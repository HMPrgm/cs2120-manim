def isPrime(x):
    if x < 2: return False
    
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
A = {4, 6, 8}

def ExistentialQuantifier(A, predicate):
    for x in A:
        if predicate(x):
            return True
    return False


hasPrime = ExistentialQuantifier(A,isPrime)
print(hasPrime)