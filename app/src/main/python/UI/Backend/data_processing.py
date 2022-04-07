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

def run_analysis(exp_design):

    current_dat = exp_design['data_file']
    dat = read_test_data(current_dat)
    dat = dat.rename(columns=str.lower)
    dat.columns = dat.columns.str.replace(" ", "")
    ivs = exp_design['iv']
    dvs = exp_design['dv']
    exp_dat = test_data(dat, ivs, dvs)

    # dictionaries with tests available
    descriptives_stats_tests = {"mean_sd": mean_sd, }
    inferential_stats_tests = {"regression": regression, "students_t_test": students_t_test,}
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

    # compare user input to available tests, if test exists then run
    # update the results dict to hold the results of the tests as html tables
    if finalDesc in descriptives_stats_tests.keys():
        statistics['d'] = descriptives_stats_tests[finalDesc](exp_dat)
        results['descriptive'] = statistics['d'].to_html()

    if finalInf in inferential_stats_tests.keys():
        statistics['i'] = inferential_stats_tests[finalInf](exp_dat)
        results['inferential'] = statistics['i'].to_html()
    
    if finalMetric in metrics.keys():
        statistics['i'] = metrics[finalMetric](exp_dat)
        results['inferential'] = statistics['i'].to_html()
    
    if finalVis in visualisations.keys():
        visualisations[finalVis](exp_dat, ivs, dvs)
        # code to generate url for visualisation modified from: 
        # https://stackoverflow.com/questions/34492197/how-to-render-and-return-plot-to-view-in-flask
        # modified code shown in answer with 8 votes at time of writing 
        # included that relating to saving the plot, we produce the visualisation in 
        # visualisations.py and save this result
        img = io.BytesIO()
        plt.savefig(img, format = 'png')
        plt.close()
        img.seek(0)
        plt_url = base64.b64encode(img.getvalue()).decode('utf-8')
                
        analysis = {"vis": plt_url, "stats": results}

    return analysis

def get_p():
    p = statistics['i']
    if p is None:
        p = 0
    else:
        p = statistics['i'].iloc[0]['p-val'].item()
    return p