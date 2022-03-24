FROM python:3.7

WORKDIR /usr/src/app

RUN apt-get update -y
RUN apt-get install -y libgdal-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python -m main
