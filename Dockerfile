FROM python:3.8.10-alpine3.14

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./server.py" ]
