## Project Introduction

This is the backend Django application of the project. In this directory, we would create the backend server to get the company statistic based on the data in ```data``` folders.

**Please make sure your current work directory is ```app```**

## Setting up

```bash
# Install Git LFS
$ brew install git-lfs

# Create virtual environment
$ python -m venv env

# Activate virtual environment for MAC/UNIX
$ . env/bin/activate

# Activate virtual environment for WINDOWS
$ venv\Scripts\activate

# Install requirements package
$ pip install -r requirements.txt
```

## Run the project
```bash
# If this is the first time you run the project, make sure to migrate (normally takes 5 mins)
$ python3 manage.py migrate

# Start the project (may take > 5 minutes to be ready)
$ python3 manage.py runserver
```
The backend server is up when the terminal shows
```
System check identified 1 issue (0 silenced).
April 21, 2022 - 19:31:30
Django version 3.2.13, using settings 'backendApi.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
After the Backend server is up, make sure you run the frontend server in the [frontend repo](https://github.com/KareemAlsayed1/friendly-company-FE)
