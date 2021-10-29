FROM python:3.8.2
WORKDIR /project
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONPATH "${PYTHONPATH}:/project"
CMD ["streamlit", "run", "app/streamlit_app.py"]