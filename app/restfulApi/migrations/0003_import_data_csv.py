import pandas as pd 
import ast
from django.db import migrations, models

def load_initial_data(apps, schema_editor):
    company_data = apps.get_model("restfulApi", "company_data")
    with open('../data/company_stats_compilation.csv') as csv_file:
        df = pd.read_csv(csv_file) 
        companies = []
        for index, entry in df.iterrows():

            company_name = entry['Company_Name']
            job_industries = ast.literal_eval(entry['Job_Industry'])
            states = ast.literal_eval(entry['State'])
            full_time_options = ast.literal_eval(entry['Full_Time'])
            approval_rates = ast.literal_eval(entry['Approval_Rate'])

            for state in states: 
                for full_time in full_time_options:
                    if full_time == "Full-time":
                        full_time = True
                    elif full_time == "Part-time": 
                        full_time = False
                    
                    for job_industry in job_industries:
                        if job_industries[job_industry] != 0:
                            min_average = job_industries[job_industry][1]
                            max_average = job_industries[job_industry][2]
                            average = job_industries[job_industry][0]
                            approval_rate = approval_rates[job_industry]

                        # #Add the values
                        company = company_data (
                            company_name = company_name,
                            state = state,
                            job_industry = job_industry,
                            full_time = full_time,
                            min_average = min_average,
                            max_average = max_average,
                            average = average,
                            approval_rate = approval_rate
                        )
                        companies.append(company)
    
    company_data.objects.bulk_create(companies)

def reverse_func(apps, schema_editor):
    company_data = apps.get_model("restfulApi", "company_data")

    company_data.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('restfulApi', '0002_company_data'),
    ]

    operations = [
        migrations.RunPython(load_initial_data, reverse_func)
    ]