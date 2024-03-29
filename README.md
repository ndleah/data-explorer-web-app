![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

# Data Explorer Web App <img src="/img/computer.jpg" align="right" width="120" />

## 🕹️ Demo

![demo](/img/demo.gif)

## 🛠️ Description
In this project, our group will develop an interactive web application using Streamlit that will read a provided CSV file by the user and perform some exploratory data analysis on it. The web application needs to be containerised with Docker and will be running using python 3.8.2.

## 👤 Authors

* [Leah Nguyen](https://github.com/ndleah)
* [Cartier Zhi](https://github.com/cartierz)
* [Jia Ping Cai](https://github.com/caijiaping)
* [Laura Sofia Bayona](https://github.com/Laurabayonaf)

## 🏗️ Program Structure

### ⚙️ Program flow chart

![flowchart](/img/flowchart.png)

### 📁 File Structure & Description

```
./
│
├── .github/
│   ├── ISSUE_TEMPLATE       
│   │   ├── bug_report.md        <- GitHub issue template for reporting bugs  
│   │   └── feature_request.md   <- GitHub issue template for requesting improvement features
│   │
│   └── PULL_REQUEST_TEMPLATE.md <- GitHub template for pull request
│
├── app/
│   └── streamlit_app.py         <- main script used for displaying the final application in the Docker container
│
├── img/                         <- contains image(s) used in README.md 
│
├── src/
│   ├── test
│   │   ├── test_data.py         <- python script for testing code from data.py
│   │   ├── test_datetime.py     <- python script for testing code from datetime.py
│   │   ├── test_numeric.py      <- python script for testing code from numeric.py
│   │   └── test_text.py         <- python script for testing code from text.py
│   │
│   ├── __init__.py              <- turns src folder into a package for importing in main script
│   ├── data.py                  <- contains the code for displaying the "Overall information" section
│   ├── date_time.py              <- contains the code for displaying the "Information on each datetime" section
│   ├── numeric.py               <- contains the code for displaying the "Information on each numeric column" section
│   └── text.py                  <- contains the code for displaying the "Information on each text column" section
│   
├── .dockerignore                <- avoids unecessary files added up in the process of setting up Docker
├── .gitignore                   <- avoids unecessary files pushed to the repository
├── Dockerfile                   <- file used to build a Docker image
├── docker-compose.yml           <- a YAML file to configure the application's services
├── Pipfile                      <- contain information for the dependencies of the project
├── Pipfile.lock                 <- specify, based on the packages present in Pipfile
└── README.md                    <- a markdown file containing student details, a description of this project and instructions for running the application
```

## ⚙️ Instructions

Clone the repository

```bash
git clone https://github.com/ndleah/Data_Explorer_Web_App.git
cd Data_Explorer_Web_App
```

Run the Docker container with docker compose

```bash
docker-compose up -d --build
```

The container will start in detached mode and can now be accessed via [http://localhost:8501](http://localhost:8501). 

Whenever you change the app/streamlit_app.py the steamlit application will update too. If you want to build upon that example, just add your dependencies to the Dockerfile and rebuild the image using docker-compose.

After you are done, and you want to tear down the application, either

```bash
docker-compose stop
```

to stop the application, or use 

```bash
docker-compose down --rmi all
```

to stop the application, remove the stopped containers and optionally `--rmi all` / remove all images associated in the docker-compose.yml file.