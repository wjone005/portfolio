FROM alpine:latest
MAINTAINER Willie David Jones III "Williejones005@gmail.com"

RUN apk add --no-cache python3-dev \
 && pip3 install --upgrade pip

WORKDIR /

COPY . .

RUN pip3 --no-cache-dir install -r requirements.txt


EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["application.py"]
