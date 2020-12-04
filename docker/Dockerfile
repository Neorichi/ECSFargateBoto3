FROM python:3

ADD ./app /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

CMD [ "python", "./app/main.py" ]
