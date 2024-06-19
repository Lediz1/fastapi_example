FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /api
RUN mkdir user-api



COPY user-api/requirements.txt app/

RUN pip install --upgrade pip
RUN pip install -r app/requirements.txt


COPY user-api ./user-api
COPY user-api/tests ./user-api/tests