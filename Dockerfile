FROM python:3.7

WORKDIR /home/app/trader
COPY . .

RUN pip install -r requirements.txt

CMD python __main__.py