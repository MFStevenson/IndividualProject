# imports
from numpy import require
import pandas as pd
import os.path
from flask import request
import cgi
import sys

from sympy import im, re
from flask import jsonify

from Backend.stats_tests import *
from Backend.visualisations import *


def read_test_data(data_file):
    csv = '.csv'
    file_type = os.path.splitext(data_file)[1]
    wd = "/Users/miafulustevenson/Documents/CurrentUni/Fourth Year/CS/Project/IndividualProject/app/src/main/python/UI/experimental_data/"
    
    if file_type == csv:
        # file will need to change to get current directory rather than hard coded in
        file = wd + data_file
        dat = pd.read_csv(file)
 
    return dat

def read_exp_design():
    # this should read in data about the design so ivs, dvs, etc
    # this data will come from user filling in form
    # could store in dictionary so can access this for later, e.g., reading in

    significance = 0.05 #request.form.get("significance")

    # need to create these, and look at implementing radio buttons
    dvs = "birthweight" #request.form.get("dv")
    ivs = "headcirc" #request.form.get("iv")

    exp_design = {'significance': significance, 'iv': ivs, 'dv': dvs}

    return exp_design

# for stats tests that have one IV and DV
def test_data(dat, iv, dv):
    test_dat = dat.filter([iv, dv], axis = 1)

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

def run_analysis(exp_design):
    # in here need to work out how to select the different test to be run
    # logic of this could be to get the test to run previous then use something
    # like a case statement to switch between options and run appropriate suite
    # to do this, would need another func, say decide_test which would look at
    # experimental design procided by user

    # this will be from the user input

    current_dat = "test_data.csv"
    dat = read_test_data(current_dat)
    ivs = "birthweight" #exp_design['iv']
    dvs = "headcirc" #exp_design['dv']
    exp_dat = test_data(dat,ivs, dvs)

    descriptives_stats_tests = {"mean_sd": mean_sd, }
    inferential_stats_tests = {"regression": regression, }
    visualisations = {"scatter_plt": scatter_plt, "regression_plt": regression_plt,}

    # need to send this back to user
    inferential = recommend_inf_test()
    descriptive = recommend_desc_test()
    vis = recommend_visualisation()

    # will be data in forms when user presses 'generate report', need to get this from user input
    finalProb = 0.05 #exp_design["significance"]
    finalDesc = "mean_sd"#request.form["desc"]
    finalVis = "regression_plt"#request.form["vis"]
    finalInf = "regression"#request.form["inf"]
    finalMetrics = "" #request.form["metric"]

    stats = {'d': None, "i": None}

    # If there are multiple tests/visualisations, then would put these in a list and for each item in the list check this

    for t in descriptives_stats_tests:
        if t in descriptives_stats_tests.keys():
            if finalDesc == t:
                stats['d'] = descriptives_stats_tests[t](exp_dat).to_html()

    for t in inferential_stats_tests:
        if t in inferential_stats_tests.keys():
            if finalInf == t:
                stats['i'] = inferential_stats_tests[t](exp_dat).to_html()
    
    for v in vis:
        if v in visualisations.keys():
            if finalVis == v:
                vis = visualisations[v](exp_dat)

    # also need to return vis

    print(stats)


def output():
    # should deal with outputs from program, will format this in front end
    # so output should just be results gained from data_rpocessing
    # outputs:
        # results from tests,
        # visualisations,
        # summary of results, this summary could come from a selection of 
        # predefined phrases, could be based on p-val
    return 0
# d.to_csv("descriptive.csv", index = False)
# i.to_csv("inferential.csv", index = False)