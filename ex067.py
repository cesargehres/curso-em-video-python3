count = 0
while True:
    t = int(input(f'Qual tabuada você quer ver?'))
    if t < 0:
        break
    while True:
        count += 1
        mult = t * count
        print(f'{t} x {count} = {mult}')
        if count == 10:
            count = 0
            break
