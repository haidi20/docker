FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install nano
RUN python -m pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .