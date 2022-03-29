import numpy as np
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
        'LCA_FY2016.csv',
        'LCA_FY2017.csv',
        'LCA_FY2018.csv',
        'LCA_FY2020_Q1.csv',
        'LCA_FY2020_Q2.csv',
        'LCA_FY2020_Q3.csv',
        'LCA_FY2020_Q4.csv',
        'LCA_FY2021_Q3.csv',
        'LCA_FY2021_Q2.csv',
        'LCA_FY2021_Q1.csv',
        'LCA_FY2021_Q4.csv',
    ]
    all_data = {}
    for file in file_name:
        year = int(file[6:10])
        my_path = 'app/restfulApi/filtered_columns_data/'
        new_df = clean_data(pd.read_csv(my_path + file))
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
    53: 'Transportation and Material Moving Occupations',
    55: 'Military Specific Occupations'
}

def clean_data(data):

    data = data.rename({'CASE_SUBMITTED': 'RECEIVED_DATE', 'SOC_NAME': 'SOC_TITLE'}, axis=1)
    
    # Deal with erroneous data in SOC_CODE
    print(data.keys())
    # data = data[data['SOC_CODE'].notna()]
    # data = data.replace({np.nan: None})
    # data = data[~data['SOC_CODE'].str.contains("[a-zA-Z]").fillna(False)]
    # data = data[data['SOC_CODE'].apply(lambda x: len(x.split('-')[0])>1)]
    
    # Big group define
    data['BIG_GROUP_CODE'] = [int(str(i)[0:2]) for i in data.SOC_CODE]
    data = data[data['BIG_GROUP_CODE'].isin(big_group_dict.keys())] # drop rows with weird SOC codes
    data['BIG_GROUP_NAME'] = [big_group_dict[i] for i in data.BIG_GROUP_CODE]
    
    data['WAGE_RATE_OF_PAY_FROM'] = [convert_wage_str(i) for i in data.WAGE_RATE_OF_PAY_FROM]
    data['WAGE_RATE_OF_PAY_TO'] = [convert_wage_str(i) for i in data.WAGE_RATE_OF_PAY_TO]
    
    data = data.replace({np.nan: None})
    
    # Calculate average wage
    tmp = []
    for idx, row in data.iterrows():
        if (row.WAGE_RATE_OF_PAY_TO) is None:
            tmp.append(row.WAGE_RATE_OF_PAY_FROM)
        else:
            tmp.append((row.WAGE_RATE_OF_PAY_FROM + row.WAGE_RATE_OF_PAY_TO) / 2)
            
    data['AVERAGE_WAGE'] = tmp
    
    # Uppercase CASE_STATUS & EMPLOYER_NAME
    data['CASE_STATUS'] = data['CASE_STATUS'].str.upper()
    data['EMPLOYER_NAME'] = data['EMPLOYER_NAME'].str.upper()
    
    # Convert datetime
    data.RECEIVED_DATE = pd.to_datetime(data.RECEIVED_DATE)
    data.DECISION_DATE = pd.to_datetime(data.DECISION_DATE)
    data.ORIGINAL_CERT_DATE = pd.to_datetime(data.ORIGINAL_CERT_DATE)
    
    return data

def convert_wage_str(wage_str):
    if wage_str is None:
        return None
    
    # Delete the dollar sign
    wage_str = wage_str[1:]
    
    wage_str = wage_str.replace(',', '')
    return float(wage_str)
