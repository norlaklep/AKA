import numpy as np
import os

os.makedirs('data', exist_ok=True)
size = [1000, 2000, 3000, 4000, 5000]

def random_number():
    for n in size:
        array = list(np.random.randint(1, 5000,  n))
        name = 'rand' + str(n) + '.dat'
        np.savetxt('data/'+name, array, fmt=['%i'])


random_number()
