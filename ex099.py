def Maior(* num):
    if len(num) > 0:
        M = num[0]
        print('Foram informados os valores: ', end='')
        for n in num:
            print(f'{n} ', end='')
            if n > M:
                M = n
        print()
        print(f'Foram informados ao todo {len(num)} valores')
        print(f'O maior valor informado foi {M}.')
    else:
        print('Nenhum valor foi informado.')


Maior(1, 3, 2, 77, 23, 0)
