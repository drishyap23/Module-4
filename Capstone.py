import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(sns.get_dataset_names())

df = sns.load_dataset('penguins')

print(df.head(10))

print(df.shape)

print(df.tail())