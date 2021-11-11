# imports
import pandas as pd
import os.path

from stats_tests import *
from visualisations import *

def read_data(data_file):
    csv = '.csv'
    file_type = os.path.splitext(data_file)[1]
    
    if file_type == csv:
        dat = pd.read_csv(data_file)

    return dat


def test_data(dat):
    test_dat = dat.filter(['Birthweight', 'Headcirc'], axis = 1)

    return test_dat   

dat = read_data('test_data.csv')
test_dat = test_data(dat)

visualisation = regression_plt(test_dat)
stats_result = regression(test_dat)
descriptives = stats_result['d']
inferential = stats_result['i']

d.to_csv("descriptive")
i.to_csv("inferential")
