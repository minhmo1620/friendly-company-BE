## Data instructions

First of all, all datasets in this project are collected from [US Department of Labor](https://www.dol.gov/agencies/eta/foreign-labor/performance). We decided to use the LCA database from 2016 to 2021, but excluding 2019 due to its different structure compared to the other datasets. The format for naming is ```LCA_FY<year>_<quarter - optional>.csv```. For example, file ```LCA_FY2020_Q1.csv``` will be the data for quarter 1 of fiscal year 2020. Quarter section is optional based on the original dataset in the website.

Due to the limitation on storage of GitHub repo, only filtered data will be stored in the repo. The original dataset can be found [here](https://drive.google.com/drive/folders/1GaHQP0gJxTbAwrnY6gxkgitYC2mTcdCI?usp=sharing).

From the original dataset, we decided to only keep specific columns in our cleaned data. Those columns are:
```
'CASE_STATUS',
'RECEIVED_DATE',
'DECISION_DATE',
'ORIGINAL_CERT_DATE',
'VISA_CLASS',
'SOC_CODE',
'SOC_TITLE',
'FULL_TIME_POSITION',
'EMPLOYER_NAME',
'EMPLOYER_CITY',
'EMPLOYER_STATE',
'WAGE_RATE_OF_PAY_FROM',
'WAGE_RATE_OF_PAY_TO',
'WAGE_UNIT_OF_PAY', 
'PREVAILING_WAGE',
'PW_UNIT_OF_PAY'
```

To understand the description of each column, please refer to ```data_codebook.pdf```. 

To filter the original data to get the cleaned data, you can run ```drop_columns.ipynb```. 

## Data Analysis

### Company statistics
To get the H1B sponsorship-related statistics of each data (e.g., LCA approval rate, LCA waiting time, average salary range), we used the Jupyter Notebook ```company_stats.ipynb``` to explore the data and use these functions in the backend server to process the request.

### Company name consistency
Only companies that used the same company names throughout the years are used as the main data for the website. This has been reviewed in the Jupyter Notebook ```company_names_analysis.ipynb```. In total, 9,183 companies have consistent names throughout the years and have been selected to be used for the website.

### Company H1B-related data compilation
Along with the above analyses, additional analyses (such as extracting the cities and states that have been mentioned in the datasets) have been conducted to construct ```company_stats_compilation.csv``` that contains each company's entire H1B sponsorship-related data that will be displayed on the website. 
