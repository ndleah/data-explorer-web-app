FROM python:3.8-slim-buster

# exposing default port for streamlit
EXPOSE 8501

# making directory of app
WORKDIR /app

# copy over requirements
COPY requirements.txt ./requirements.txt

# installing required packages
RUN pip3 install -r requirements.txt

# Create an entry point to make our image executable
ENTRYPOINT ["streamlit", "run"]

# cmd to launch app when container is run
CMD ["main_leah.py"]