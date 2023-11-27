FROM python

RUN pip3 install flask

EXPOSE 5001

COPY ./app1.py ./app/app1.py

WORKDIR /app

CMD python3 app1.py