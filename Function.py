def mult_persistence(n):
    count = 0
    n = str(n)

    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1

    return count


print(mult_persistence(999))
