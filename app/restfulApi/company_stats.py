import numpy as np

from .load_heavy_data import get_data, big_group_dict

def get_all_charts(company_name):
    data = get_data()

    new_data = get_data_on_company(data, company_name)

    approval_rate_over_years, approval_rate_years = get_approval_rate_over_years(new_data)

    waiting_time, waiting_time_years = get_waiting_time_over_years(new_data)

    applications_count, groups = get_no_applicants_per_job_industry(new_data[2021])

    average_wage_on_job = get_average_wage_per_job(new_data[2021])

    return {
        "approval_rate": {
            "series": {
                "data": approval_rate_over_years,
                "name": "Approval rate over years"
            },
            "options": {
                "xaxis": {
                "categories": approval_rate_years,
              }
            }
        },
        "waiting_time": {
            "series": {
                "data": waiting_time,
                "name": "Waiting time over years"
            },
            "options": {
                "xaxis": {
                "categories": waiting_time_years,
              }
            }
        },
        "applications_count_groups": {
            "series": {
                "data": applications_count,
                "name": "Number of applicants per job industry"
            },
            "options": {
                "xaxis": {
                "categories": groups,
              }
            }
        },
        "average_wage_on_job": average_wage_on_job
    }

def filter_data_by_company_name(data, company_name):
    return data[(data.EMPLOYER_NAME.str.contains(company_name)) & (data.VISA_CLASS == 'H-1B')]

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

def get_no_applicants_per_job_industry(data):
    # Find all uniques groups inside the data
    unique_groups = set(data.BIG_GROUP_CODE)
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

def get_average_wage_per_job(data):
    # print(data.head())
    unique_groups = set(data.BIG_GROUP_CODE)
    groups = {}

    for group_code in unique_groups:
        jobs, average_on_job = calculate_average_wage_per_job(data, group_code)
        group_name = big_group_dict[group_code]
        groups[group_name] = {
            "series": {
                "data": average_on_job,
                "name": "Number of applicants per job type"
            },
            "options": {
                "xaxis": {
                "categories": jobs,
              }
            }
        }
    
    return groups

def calculate_average_wage_per_job(data, group_code):
    # Filter all applications with the same group code
    data = data.loc[data.BIG_GROUP_CODE == group_code]
    
    # Find all uniques job_code
    unique_job_titles = set(data.SOC_TITLE)
    
    # Get the job title based on job_code - later, if necessary
   
    # Calculate salary stats for each job code
    average_on_job = []
    jobs = []
    for job_title in unique_job_titles:
        jobs.append(job_title)
        average_on_job.append(calculate_salary_stats(job_title, data))
    
    return jobs, average_on_job

def calculate_salary_stats(job_title, data):
    # Find all applications of specific job code
    new_data = data.loc[data.SOC_TITLE == job_title]
    # Collect all salaries
    salaries = new_data.AVERAGE_WAGE
    
    # Mean
    mean_salaries = np.round(np.mean(salaries))
    
    # Median
    median_salaries = np.round(np.median(salaries))
    
    # Min, Max
    min_salaries = min(salaries)
    max_salaries = max(salaries)
    
    # 95 Confidence Interval
    
    return mean_salaries
