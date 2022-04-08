import pandas as pd
import seaborn as sns
import base64
import io
import matplotlib.pyplot as plt

from Backend.data_processing import *

# available visialisations
sns.set_style("white")

def scatter_plt(dat, x, y):
    return sns.scatterplot(data = dat, x = x, y = y)

def regression_plt(dat, x, y):
    return sns.regplot(x = x, y = y, data = dat)

def box_plt(dat,x, y):
    return sns.boxplot(x = x, y = y, data = dat)

def violin_plt(dat, x, y):
    return sns.violinplot(x = x, y = y, data = dat)