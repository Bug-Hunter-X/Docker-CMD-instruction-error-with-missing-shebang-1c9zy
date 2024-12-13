FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3-pip
COPY . /app
WORKDIR /app
RUN chmod +x server.py
CMD ["python3", "/app/server.py"]