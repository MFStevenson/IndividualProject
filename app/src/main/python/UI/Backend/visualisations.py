import pandas as pd
import seaborn as sns
import base64
import io
import matplotlib.pyplot as plt

from Backend.data_processing import *

sns.set_style("white")

wd = "/Users/miafulustevenson/Documents/CurrentUni/Fourth Year/CS/Project/IndividualProject/app/src/main/python/UI/media/"
def scatter_plt(dat, x, y):
    sns.scatterplot(data = dat, x = x, y = y)
    img = io.BytesIO()
    plt.savefig(img, format = 'png')
    plt.close()
    img.seek(0)
    plt_url = base64.b64encode(img.getvalue()).decode('utf-8')
    return plt_url

def regression_plt(dat, x, y):
    sns.regplot(x = x, y = y, data = dat)
    img = io.BytesIO()
    plt.savefig(img, format = 'png')
    plt.close()
    img.seek(0)
    plt_url = base64.b64encode(img.getvalue()).decode('utf-8')
    return plt_url

def box_plt(dat,x, y):
    sns.boxplot(x = x, y = y, data = dat)
    img = io.BytesIO()
    plt.savefig(img, format = 'png')
    plt.close()
    img.seek(0)
    plt_url = base64.b64encode(img.getvalue()).decode('utf-8')
    return plt_url

def violin_plot(dat, x, y):
    sns.violinplot(x = x, y = y, data = dat)
    img = io.BytesIO()
    plt.savefig(img, format = 'png')
    plt.close()
    img.seek(0)
    plt_url = base64.b64encode(img.getvalue()).decode('utf-8')
    return plt_url