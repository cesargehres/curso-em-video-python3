Lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > max(Lista):
        Lista.append(n)
        print(f'O número {n} foi adicionado ao final da lista.')
    else:
        i = 0
        while True:
            if n <= Lista[i]:
                Lista.insert(i, n)
                print(f'O número {n} foi adicionado na posição {i}.')
                break
            i += 1
print(Lista)
