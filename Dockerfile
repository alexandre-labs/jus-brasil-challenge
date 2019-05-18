FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /tmp/app

EXPOSE 8080

WORKDIR /tmp/app

RUN make install

CMD uvicorn jus_brasil:app --host 0.0.0.0 --port 8080
