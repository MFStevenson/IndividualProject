import pandas as pd
import seaborn as sns

from data_processing import test_dat

sns.set_theme()

def scatter_plt(dat, x, y):
    plt = sns.scatterplot(data = dat, x = x, y = y)
    plt.savefig("ScatterPlt.png")

    return plt

def regression_plt(dat, x, y):
    plt = sns.regplot(x = x, y = y, data = dat)
    plt.savefig("RegPlt.png")

    return plt