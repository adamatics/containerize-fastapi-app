FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . /app

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:5000", "app:app"]
