FROM python:3.14.2

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY ./src /src

CMD ["python", "/src/app.py"]