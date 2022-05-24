FROM python:3

#ENV SCR_DIR /usr/bin/src/webapp/src

#COPY SRC/* /home/softwarenetic/SCR_DIR

RUN mkdir /code
COPY . /code
WORKDIR /code
#WORKDIR /home/softwarenetic/src

ENV PYTHONUNBUFFERED=1
EXPOSE 5000

CMD [ "python", "simple_server.py" ]



