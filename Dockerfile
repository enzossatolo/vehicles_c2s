FROM python:3.13-slim-bullseye
WORKDIR /app
ENV PYTHONPATH=/app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt
