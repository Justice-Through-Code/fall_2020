import pandas as pd
import numpy as np

import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return(result_str)

productA = pd.DataFrame({'product':['Product A']*100, 
						 'rating': np.random.uniform(low=0, high = 5, size = 100)})

productB = pd.DataFrame({'product':['Product B']*100, 
						 'rating': np.random.uniform(low=0, high = 3, size = 100)})

productC = pd.DataFrame({'product':['Product C']*100, 
						 'rating': np.random.uniform(low=2, high = 5, size = 100)})

ids = []

for i in range(300):
	ids.append(pd.util.testing.rands(6))


products = pd.concat([productA, productB, productC])
products['user_id'] = ids

products.to_csv('../../datasets/product_tests.csv', index = True)