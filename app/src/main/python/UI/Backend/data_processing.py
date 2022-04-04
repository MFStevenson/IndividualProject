# imports
from flask import flash
import pandas as pd
import os.path
from flask import request, redirect, url_for

from Backend.stats_tests import *
from Backend.visualisations import *

def read_test_data(data_file):
    csv = '.csv'
    file_type = os.path.splitext(data_file)[1]
    exp_dir = 'experimental_data/'
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    wd = os.path.join(cur_dir, exp_dir)
    
    if file_type == csv:
        file = wd + data_file
        dat = pd.read_csv(file)
 
    return dat

def read_exp_design():

    significance = request.form.get("significance")

    # need to create these, and look at implementing radio buttons
    dvs = request.form.get("dv")
    ivs = request.form.get("iv")

    exp_design = {'significance': float(significance), 'iv': ivs, 'dv': dvs}

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
        flash("wrong type of test selected")
        return redirect(url_for('create_report'))

    # filter data, need to make sure all ivs are filtered on
    test_data = dat.filter(['iv', 'dv'], axis = 1)
    return test_dat

def run_analysis(exp_design):

    current_dat = exp_design['data_file']
    dat = read_test_data(current_dat)
    dat = dat.rename(columns=str.lower)
    dat.columns = dat.columns.str.replace(" ", "")
    ivs = exp_design['iv']
    dvs = exp_design['dv']
    exp_dat = test_data(dat,ivs, dvs)


    descriptives_stats_tests = {"mean_sd": mean_sd, }
    inferential_stats_tests = {"regression": regression, }
    visualisations = {"scatter_plt": scatter_plt, "regression_plt": regression_plt,}
    metrics = {"precision": precision,}

    finalDesc = request.form.get("desc")
    finalVis = request.form.get("vis")
    finalInf = request.form.get("inf")
    finalMetric = request.form.get("metric")

    global statistics
    statistics = {'d': None, 'i': None}
    results = {'descriptive': None, "inferential": None}
    vis = None

    for t in descriptives_stats_tests:
        if t in descriptives_stats_tests.keys():
            if finalDesc == t:
                statistics['d'] = descriptives_stats_tests[t](exp_dat)
                results['descriptive'] = statistics['d'].to_html()

    for t in inferential_stats_tests:
        if t in inferential_stats_tests.keys():
            if finalInf == t:
                statistics['i'] = inferential_stats_tests[t](exp_dat)
                results['inferential'] = statistics['i'].to_html()
    
    for t in metrics:
        if t in metrics.keys():
            if finalMetric == t:
                statistics['i'] = metrics[t](exp_dat)
                results['inferential'] = statistics['i'].to_html()
    
    for v in visualisations:
        if v in visualisations.keys():
            if finalVis == v:
                vis = visualisations[v](exp_dat, ivs, dvs)
                
        analysis = {"vis": vis, "stats": results}
    # also need to return vis
    return analysis

def get_p():
    p = statistics['i'].iloc[0]['p-val'].item()
    return p