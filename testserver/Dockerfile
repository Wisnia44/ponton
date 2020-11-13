FROM python:3.8

RUN mkdir -p /testserver

WORKDIR /testserver

ADD . /testserver

VOLUME ["/testserver"]

COPY testserver/requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "testserver/server.py" ]