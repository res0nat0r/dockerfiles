FROM kennethreitz/pipenv as build

ADD . /app
WORKDIR /app

RUN pipenv install

ENTRYPOINT [ "pipenv", "run", "/app/imdb.py" ]
