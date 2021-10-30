FROM python:3.8.2

EXPOSE 8501

WORKDIR /project

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/project"

CMD ["streamlit", "run", "app/streamlit_app.py"]

# docker build -t streamlitapp:latest .
# docker run -p 8501:8501 -e PYTHONPATH="${PYTHONPATH}:/project" -it streamlitapp:latest