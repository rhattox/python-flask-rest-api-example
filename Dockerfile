FROM python:3.10-bookworm

WORKDIR /home/python/src

COPY ./src .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["flask", "run"]