# Use Python 3.10 as the parent image
FROM python:3.10-slim-buster

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot.py"]