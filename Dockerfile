FROM python:3-slim
MAINTAINER Deloitte Cyber Risk

ENV INSTALL_PATH /rcs
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -c "python:config.gunicorn" "rcs.app:create_app()
