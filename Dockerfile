FROM python:3-alpine

WORKDIR /usr/src/app

RUN apk add build-base libxml2-dev libxslt-dev py3-pillow jpeg-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT /usr/src/app/entrypoint.sh

