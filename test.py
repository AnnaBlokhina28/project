import warnings
import pandas as pd
import numpy as np
import scipy.stats as stats
import math
from sklearn.linear_model import LinearRegression
from statsmodels.stats.multicomp import pairwise_tukeyhsd

#Однофакторный дисперсионный анализ
f=np.array([173, 175, 180, 178, 177, 185, 183])
h=np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
sh =np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

stats.f_oneway(f,h,sh)

print("test")