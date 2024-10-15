def sorteio():
    import random
    num = None
    num_random = random.randint(1,10)
    while num_random != num:
        num = int(input("digite um valor:"))
        if num_random < num:
            print('Chute mais baixo!')
        elif num_random > num:
            print('Chute mais alto!')
        elif num_random == num:
            print(f'Você descobriu o numero! era o {num}')


