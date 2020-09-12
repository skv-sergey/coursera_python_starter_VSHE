def rec():
    n = int(input())
    if n != 0:
        if n % 2 == 0:
            print()
        rec()
        if n % 2 != 0:
            print(n)


rec()
