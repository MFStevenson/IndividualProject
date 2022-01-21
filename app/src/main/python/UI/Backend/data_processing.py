# imports
import pandas as pd
import os.path

from stats_tests import *
from visualisations import *

def read_test_data(data_file):
    csv = '.csv'
    file_type = os.path.splitext(data_file)[1]
    
    if file_type == csv:
        # file will need to change to get current directory rather than hard coded in
        file = "Users/miafulustevenson/Documents/CurrentUni/Fourth Year/CS/Project/IndividualProject/app/src/main/python/UI/experimental_data/" + data_file
        dat = pd.read_csv(file)
 
    return dat

def read_exp_design_data():
    # this should read in data about the design so ivs, dvs, etc
    # this data will come from user filling in form
    # could store in dictionary so can access this for later, e.g., reading in

    exp_data = {}
    return exp_data

# for stats tests that have one IV and DV
def test_data(dat, iv, dv):
    test_dat = dat.filter(['iv', 'dv'], axis = 1)

    return test_dat

def multi_test_data(dat, ivs, dv):
    # function will take in a list of ivs and a dv and then filter data according to this
    # length of this list must be at least 2 and can vary in length
    # if length of ivs list is not >=2 then throw error - wrong test selected?
    test_dat = 0

    if len(ivs) < 2:
        print("wrong type of test selected")

    # filter data, need to make sure all ivs are filtered on
    test_data = dat.filter(['iv', 'dv'], axis = 1)
    return test_dat

dat = read_test_data('test_data.csv')

'''

if len(ivs) < 2:
    # birthweight and headcirc should come from user input
    test_dat = test_data(dat, 'Birthweight', 'Headcirc')
else
    test_dat = multi_test_data(dat, ivs, dv)

'''
# check data is good
# could rename cols for consistency

def recommend_desc_test():
    recommendation = []

    return recommendation

def recommend_inf_test():
    recommendation = []

    return recommendation

def recommend_visualisation():
    recommendation = []

    return recommendation

def run(test_dat):
    # in here need to work out how to select the different test to be run
    # logic of this could be to get the test to run previous then use something
    # like a case statement to switch between options and run appropriate suite
    # to do this, would need another func, say decide_test which would look at
    # experimental design procided by user

    # this will be from the user input
    test = ['regression']

    descriptives_stats_tests = {"mean_sd": mean_sd, }
    inferential_stats_tests = {"regression": regression, }
    visualisations = {"scatter_plt": scatter_plt, "regression_plt": regression_plt}

    inferential = recommend_inf_test()
    descriptive = recommend_desc_test()
    vis = recommend_visualisation()

    stats = {'d': None, "i": None}

    # If there are multiple tests/visualisations, then would put these in a list and for each item in the list check this

    for t in descriptives_stats_tests:
        if t in descriptives_stats_tests.keys():
            stats['d'] = descriptives_stats_tests[t]()

    for t in inferential_stats_tests:
        if t in inferential_stats_tests.keys():
            stats['i'] = inferential_stats_tests[t]()
    
    for v in vis:
        if v in visualisations.keys():
            vis = visualisations[v]()

    return stats
# d.to_csv("descriptive.csv", index = False)
# i.to_csv("inferential.csv", index = False)
