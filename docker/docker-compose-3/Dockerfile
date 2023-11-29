FROM python

RUN wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.6.1.tar.gz \
    && rm dockerize-linux-amd64-v0.6.1.tar.gz

COPY . ./app

WORKDIR ./app

RUN pip install mysql-connector-python

RUN pip install flask

RUN pip install python-dotenv

EXPOSE 4000

CMD python3 api.py