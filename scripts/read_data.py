import pandas as pd
import mathplotlib.pyplot as plt

# loading and preprocessing data
filename = '../data/WISDM_ar_v1.1_raw.txt'
data = pd.read_csv(filename, sep=',')
data = data[data['activity'] == 'Walking']
data = data[data['user'] == 33][:100]
# print(data[:100])
# print(data.shape)

# %matplotlib inline
