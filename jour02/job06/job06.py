def est_premier(nombre):
    if nombre <= 1:
        return False
    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            return False
    return True

for i in range(2, 1001):
    if est_premier(i):
        print(i)