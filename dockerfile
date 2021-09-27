FROM python:3.9-alpine3.14

COPY . /pycode/

RUN pip3 install -r /pycode/requirements.txt
RUN crontab /pycode/crontab

WORKDIR /pycode/
CMD ["crond", "-f"]