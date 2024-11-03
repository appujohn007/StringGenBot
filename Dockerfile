FROM python 3.10

RUN apt-get update -y && apt-get upgrade -y

RUN pip3 install -U pip

EXPOSE 8080

COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt

CMD bash start
