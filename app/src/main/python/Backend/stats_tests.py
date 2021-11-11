import pandas as pd
from scipy import stats

from data_processing import test_dat

def regression(test_dat):
    descriptive_labels = ['Mean', 'Standard Deviation']
    mean = pd.DataFrame.mean(test_dat).to_frame().T
    sd = pd.DataFrame.std(test_dat).to_frame().T
    stat = pd.DataFrame(stats.linregress(test_dat)).T

    descriptives = pd.concat([mean, sd], axis = 0, ignore_index = True)
    descriptives.insert(0, 'Statistic', descriptive_labels)
    inferential = stat.rename(columns={0:"slope", 1:"intercept", 2:"r-val", 3:"p-val", 4:"std-err"})
    results = {'d': descriptives, 'i': inferential}
    
    return results