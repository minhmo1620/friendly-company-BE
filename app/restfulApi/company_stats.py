import numpy as np

from .load_heavy_data import get_data, big_group_dict

def get_all_charts(company_name):
    data = get_data()

    new_data = get_data_on_company(data, company_name)

    approval_rate_over_years, years = get_approval_rate_over_years(new_data)

    waiting_time, years = get_waiting_time_over_years(new_data)

    applications_count, groups = get_no_applicats_per_job_industry(new_data)

    get_average_wage_per_job(job_industry=None)

    return approval_rate_over_years, years




def filter_data_by_company_name(data, company_name):
    return data[(data.EMPLOYER_NAME == company_name) & (data.VISA_CLASS == 'H-1B')]

def get_data_on_company(data, company_name):
    new_data = {}
    for k, v in data.items():
        new_data[k] = filter_data_by_company_name(v, company_name)
    return new_data

def get_approval_rate_over_years(data):
    return calculate_approval_rate_over_years(data)

def approval_number(data):
    return len(data[data.CASE_STATUS == 'CERTIFIED']) + len(data[data.CASE_STATUS == 'CERTIFIED-WITHDRAWN'])

def approval_rate(data):
    return approval_number(data) / len(data) if len(data) > 0 else 0

def denial_number(data):
    return len(data[data.CASE_STATUS == 'DENIED'])

def calculate_approval_rate_over_years(data):
    approval_rate_over_years = []
    years = []
    for year, data_year in data.items():
        approval_rate_res = approval_rate(data_year)
        years.append(year)
        approval_rate_over_years.append(approval_rate_res)
    return approval_rate_over_years, years

def get_waiting_time_over_years(data):
    waiting_time, years = [], []
    for year, data_year in data.items():
        years.append(year)
        waiting_time.append(calculate_waiting_time(data_year))
    return waiting_time, years

def calculate_waiting_time(data):
    result = []
    for index, row in data.iterrows():
        if row.CASE_STATUS == 'CERTIFIED-WITHDRAWN':
            result.append((row.ORIGINAL_CERT_DATE - row.RECEIVED_DATE).days)
        elif row.CASE_STATUS == 'CERTIFIED':
            result.append((row.DECISION_DATE - row.RECEIVED_DATE).days)
    return np.mean(result)

def get_no_applicats_per_job_industry(data):
    # Find all uniques groups inside the data
    unique_groups = set(data[2021].BIG_GROUP_CODE)
    # Results
    applications_count = []
    
    # For each group, count how many applications
    for group_code in unique_groups:
        count = count_applications_on_CODE(group_code, data)
        applications_count.append(count)
        
    # Present the results
    groups = [big_group_dict[i] for i in unique_groups]
    return applications_count, groups

def count_applications_on_CODE(group_code, data):
    return sum(data.BIG_GROUP_CODE == group_code)

def get_average_wage_per_job(job_industry):
    pass
