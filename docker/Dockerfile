FROM python:3.10

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /code

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY src .

EXPOSE 8000

