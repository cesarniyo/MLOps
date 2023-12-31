FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

#CMD ["python3", "app.py"]

CMD ["streamlit", "run", "pipeline_inference.py", "--server.port", "8080"]