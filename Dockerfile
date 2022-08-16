FROM python:3.10

WORKDIR /app

COPY ./api  /app/api
COPY ./main.py /app/api
COPY ./.env /app/.env
COPY ./datas.json /app/datas.json
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "main.py"]