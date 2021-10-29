# To be filled by students

# Description
In this project, our group will develop an interactive web application using Streamlit that will read a provided CSV file by the user and perform some exploratory data analysis on it. The web application needs to be containerised with Docker and will be running using python 3.8.2.

# Authors
* [Leah Nguyen](https://github.com/ndleah)
* [Cartier Zhi](https://github.com/cartierz)
* [Jia Ping Kai](https://github.com/caijiaping)
* [Laura Sofia Bayona](https://github.com/Laurabayonaf)

# Structure

# Instructions

Clone the repository

```bash
git clone https://github.com/ndleah/Data_Explorer_Web_App.git
cd steamlit-docker-example
```

Run the Docker container with docker compose

```bash
docker-compose up -d --build
```

The container will start in detached mode and can now be accessed via [[localhost:8501](http://localhost:8501)](http://localhost:8501). 

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