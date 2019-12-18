# docker run --rm -v `pwd`:/tmdb/moviez tmdb

FROM python:2

ARG KEY
ENV KEY=$KEY

ADD requirements.txt /
ADD tmdb.py /tmdb/tmdb.py

RUN pip install -r /requirements.txt

CMD [ "python", "/tmdb/tmdb.py" ]