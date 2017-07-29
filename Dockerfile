FROM python:alpine
ENV PYTHONPATH /source
ENV PYTHONUNBUFFERED 1

RUN ["mkdir", "/source"]
WORKDIR /source

ADD ./requirements.txt /source
ADD ./quack /source

RUN ["pip", "install", "-r", "/source/requirements.txt"]
CMD ["python", "/source/server.py"]
