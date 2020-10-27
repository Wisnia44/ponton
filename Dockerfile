# set base image (host OS)
FROM python:3
ENV PYTHONUNBUFFERED=1

# set the working directory in the container
RUN mkdir /code
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt /code/

# install dependencies
RUN pip install -r requirements.txt

# copy working directory 
COPY . /code/

# command to run on container start
CMD [ "python", "./server.py" ]



