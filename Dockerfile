FROM python:3.10.5-slim-bullseye

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./server.py" ]
