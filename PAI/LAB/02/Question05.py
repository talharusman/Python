def factoril(n):
    fac = 1
    while n>=1:
        fac *=n
        n-=1

    return fac

print(f"factorial is {factoril(5)}")
