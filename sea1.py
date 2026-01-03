import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
plt.style.use("seaborn-v0_8")
d=sn.load_dataset("diamonds")
print(d.head())