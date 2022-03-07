import pandas as pd
import seaborn as sns

from Backend.data_processing import *

sns.set_theme()

def scatter_plt(dat, x, y):
    plt = sns.scatterplot(data = dat, x = x, y = y)
    plt.savefig("ScatterPlt.png")

    return plt

def regression_plt(dat, x, y):
    plt = sns.regplot(x = x, y = y, data = dat)
    plt.savefig("RegPlt.png")

    return plt

def box_plt(dat,x, y):
    plt = sns.boxplot(x = x, y = y, data = dat)
    plt.savefig("BoxPlt.png")

def violin_plot(dat, x, y):
    plt = sns.violinplot(x = x, y = y, data = dat)
    plt.savefig("ViolinPlt.png")