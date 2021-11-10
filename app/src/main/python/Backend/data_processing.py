# imports
from scipy import stats
import pandas as pd
import os.path

def get_user_input():
    fiile_name = input("Upload file: ")

def read_data(data_file):
    file_type = os.path.splitext(data_file)[1]
    print(file_type)

read_data("name.csv")