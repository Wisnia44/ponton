FROM python:3
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN apt-get -y update && apt-get install -y cron
RUN pip install -r requirements.txt

CMD [ "python" "manage.py" "runserver" "0.0.0.0:8000" ]
