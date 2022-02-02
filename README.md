# Sales Data Reporting & Visulization using Django

![PYTHON](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![DJANGO](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![BOOTSTRAP](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![PANDAS](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![JSON](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)
![JAVASCRIPT](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)





![This is an image](https://github.com/princexoleo/Generate_and_visulaize_sales_data/blob/main/img_ss/reports_home.png)

## Overview
This is Django based web projects. The codebase shows the authentication feature of django. How people can upload a csv file in their project and how to interpreate with that file. Addditionally there is a feature available that can read the data from databases according to the date range and visulaize that retrive information with seaborn tools. Finaaly people can generate the report file, also can export it into pdf formatterd. The key featiure of this projects are given below

* Authentication
* File Uploading (csv)
* Search (date range)
* Visulaization Data (pandas, seaborn)
* Generate Report (pdf)
* Profile (user profile)
* Admin Panel (default django admin panel)


## Installation
Run below command to clone this project.
```
git clone "https://github.com/princexoleo/Generate_and_visulaize_sales_data.git"
```
Change the directory to the project directory.
```
cd reports_project
```
You can see the project directories like,
```
reports_projects
  |--src
  |--requirements.txt

```

The installation packages are given in the `reports_project/requirements.txt` files. Before that you have to install Python in your system. To install the Python check out the official websites [Python](https://www.python.org/). After installation Python, now install the `virtualenv` and creates a virtual environments name as you preferred. Activate the virtualenv & run below command to install require packages for this project. 
```
pip install -r requirements.txt

```
This will install all the requirements file for this project.


## Run
To run this project in your local machine, go to the `src` folder and run below command.
```
cd src/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```
Now if you browes the (https://127.0.0.1:8000/) in the browser, you can see the login page.

## Conclusion


## Author


## Acknowlegement