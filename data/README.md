## Data instructions

First of all, all datasets in this project are collected from [US Department of Labor](https://www.dol.gov/agencies/eta/foreign-labor/performance). We decided to use the LCA database from 2016 to 2021. The format for naming is ```LCA_FY<year>_<quarter - optional>.csv```. For example, file ```LCA_FY2020_Q1.csv``` will be the data for quarter 1 of fiscal year 2020. Quarter section is optional based on the original dataset in the website.

Due to the limitation on storage of GitHub repo, only filtered data will be stored in the repo. The original dataset can be found [here](https://drive.google.com/drive/folders/1GaHQP0gJxTbAwrnY6gxkgitYC2mTcdCI?usp=sharing)

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
'AGENT_REPRESENTING_EMPLOYER',
'LAWFIRM_NAME_BUSINESS_NAME',
'WAGE_RATE_OF_PAY_FROM',
'WAGE_RATE_OF_PAY_TO',
'WAGE_UNIT_OF_PAY', 
'PREVAILING_WAGE',
'PW_UNIT_OF_PAY'
```

To filtered the original data to get the cleaned data, you can run ```drop_columns.ipynb```. We drop database for FY 2019 because this data has different structure when compared to other years.

## Company statistics
To get the company statistic, we use the Jupyter Notebook ```company_stats.ipynb``` to explore the data and use these function in backend server to process the request.
