import pandas as pd
from scipy import stats

from Backend.data_processing import *

def mean_sd(test_dat):
    descriptive_labels = ['Mean', 'Standard Deviation']
    mean = pd.DataFrame.mean(test_dat).to_frame().T
    sd = pd.DataFrame.std(test_dat).to_frame().T

    descriptives = pd.concat([mean, sd], axis = 0, ignore_index = True)
    descriptives.insert(0, 'Statistic', descriptive_labels)

    return descriptives

def regression(test_dat):
    td = test_dat
    stat = pd.DataFrame(stats.linregress(test_dat)).T

    inferential = stat.rename(columns={0:"slope", 1:"intercept", 2:"r-val", 3:"p-val", 4:"std-err"})
    results = inferential

    return results

def students_t_test(test_dat):
    td = test_dat
    grp1 = test_dat.columns[0]
    grp2 = test_dat.columns[1]
    
    descriptives = mean_sd(td)
    stat = pd.DataFrame(stats.ttest_ind(a = grp1, b = grp2, equal_var=False)).T

def precision(test_dat):
    return 0
    