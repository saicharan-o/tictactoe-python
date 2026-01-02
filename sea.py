import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
plt.style.use("classic")
d=sn.load_dataset("car_crashes")
print(d.head())