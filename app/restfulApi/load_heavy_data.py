import os
import pandas as pd

data = None

def load_model():
    global data
    data = load_expensive_data()

def get_data():
    if data is None:
        raise Exception("Expensive model not loaded")
    return data

def load_expensive_data():
    file_name = [
        'LCA_FY2021_Q3.csv',
        'LCA_FY2021_Q2.csv',
        'LCA_FY2021_Q1.csv',
        'LCA_FY2021_Q4.csv',
        'LCA_FY2020_Q1.csv',
        'LCA_FY2020_Q2.csv',
        'LCA_FY2020_Q3.csv',
        'LCA_FY2020_Q4.csv',
        'LCA_FY2016.csv',
        'LCA_FY2017.csv',
        'LCA_FY2018.csv',
    ]
    all_data = {}
    for file in file_name:
        year = int(file[6:10])
        my_path = '../data/filtered_columns_data/'
        new_df = pd.read_csv(my_path + file)
        if year in all_data:
            all_data[year] = pd.concat([all_data[year], new_df], ignore_index=True)
        else:
            all_data[year] = new_df
    return all_data

big_group_dict = {
    11: 'Management Occupations',
    13: 'Business and Financial Operations Occupations',
    15: 'Computer and Mathematical Occupations',
    17: 'Architecture and Engineering Occupations',
    19: 'Life, Physical, and Social Science Occupations',
    21: 'Community and Social Service Occupations',
    23: 'Legal Occupations',
    25: 'Educational Instruction and Library Occupations',
    27: 'Arts, Design, Entertainment, Sports, and Media Occupations',
    29: 'Healthcare Practitioners and Technical Occupations',
    31: 'Healthcare Support Occupations',
    33: 'Protective Service Occupations',
    35: 'Food Preparation and Serving Related Occupations',
    37: 'Building and Grounds Cleaning and Maintenance Occupations',
    39: 'Personal Care and Service Occupations',
    41: 'Sales and Related Occupations',
    43: 'Office and Administrative Support Occupations',
    45: 'Farming, Fishing, and Forestry Occupations',
    47: 'Construction and Extraction Occupations',
    49: 'Installation, Maintenance, and Repair Occupations',
    51: 'Production Occupations',
    53: 'Transportation and Material Moving Occupations'
}
