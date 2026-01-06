import random

hanguls = list('가나다라마바사아자차카타파하')

with open('info.txt', 'w') as file:
    for i in range(1000):
        name = (random.choice(hanguls) + random.choice(hanguls) + random.choice(hanguls))
        weight = random.randint(40, 140)
        height = random.randint(140, 230)
        file.write('{}, {}, {}\n'.format(name, weight, height))