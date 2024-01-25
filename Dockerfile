FROM python:3.8

WORKDIR /usr/animate/
COPY . . 

EXPOSE 5000

WORKDIR ./src

CMD [ 'python3', 'test.py' ]