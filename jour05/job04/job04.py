def carpet(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                print("+ ", end="")
            elif i == 0 and j == n:
                print("+ ", end="")
            elif i == n and j == 0:
                print("+ ", end="")
            elif i == n and j == n:
                print("+ ", end="")
            elif i == 0 or i == n:
                print("- ", end="")
            elif j == 0 or j == n :
                print("|",end=" ")
            elif i + j == n:
                print("  ", end="")
            elif i == j:
                print("# ", end="")
            else:
                print("# ", end="")
        print()


while True:
    try:
        size = int(input("Entrer la taille du tapis : "))
        break
    except ValueError:
        print("Entrer un nombre entier valide")

carpet(size)