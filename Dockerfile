FROM python:3.6-alpine

RUN adduser -D for_twenty

WORKDIR /home/psalter

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

COPY app app
COPY migrations migrations
COPY for_twenty.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP for_twenty.py

RUN chown -R for_twenty:for_twenty ./
USER for_twenty

EXPOSE 8765
ENTRYPOINT ["./boot.sh"]
