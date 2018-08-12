FROM python:3-slim
MAINTAINER Deloitte Cyber Risk

ENV INSTALL_PATH /app/directory
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -c "python:config.gunicorn" --reload "directory.app:create_app()"
