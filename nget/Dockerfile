FROM ubuntu
RUN apt-get update && apt-get install -y nget
COPY services /etc/services
ENTRYPOINT ["nget"]
