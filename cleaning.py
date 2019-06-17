import pandas as pd
import numpy as np

df = pd.read_csv("trial.txt", header=None, delimiter=",")
print(df)

df.to_csv('clean1.csv')
