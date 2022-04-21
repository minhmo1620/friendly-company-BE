# Visualizing H1B-Friendly Companies

This project builds a website that compiles and visualizes H1B sponsorship-related data for international users wishing to work in the US to easily search and access.

## Project Description

This is a data analysis and visualization project that displays H1B sponsorship-related data of companies based in the US through a locally hosted website. The source of the data is the annual Labor Condition Application (LCA) Disclosure Data released by the US Department of Labor of which the 2016, 2017, 2018, 2020, and 2021 data were used. 

The major search functions of the website that the users can perform include:
- Users can use search filters to access a relevant and customized set of data by using search filters. The filters they can set include the job industry they wish to work in, the US state they wish to work in, and whether they wish to work as a full-time or part-time employer.
- Users can also directly search the name of the company and access the searched company's H1B sponsorship-related data.

The H1B sponsorship-related data per company that the users can access include:
- The company's H1B LCA approval rate over the years
- The company's waiting time for H1B LCA over the years
- The number of applicants sponsored by the company per job industry in 2021 (most recent data)
- The average salary of the jobs sponsored by the company in 2021 (most recent data)

## Run the project

This website is hosted locally. To run locally, please refer to the details of the [frontend](https://github.com/KareemAlsayed1/friendly-company-FE/blob/main/README.md) and [backend](https://github.com/minhmo1620/friendly-company/blob/main/app/README.md') server instructions. 

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10
* Please make sure you install Git LFS before cloning the repo
```bash
# Install Git LFS
$ brew install git-lfs
```

### Starting the Backend Server

* Run the following code inside the main directory to run the backend server
```
$ cd app

# Create virtual environment
$ python -m venv env

# Activate virtual environment for MAC/UNIX
$ . env/bin/activate

# Activate virtual environment for WINDOWS
$ venv\Scripts\activate

# Install requirements package
$ pip install -r requirements.txt

# Start the project
$ python3 manage.py runserver
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details
