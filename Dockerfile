# docker from docker refs: https://tomgregory.com/running-docker-in-docker-on-windows/
FROM python:3.9.13-alpine3.16

WORKDIR /usr/src/app

# install the required packages
RUN apk update && \
    apk add mariadb-client

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

# run docker as non-root user
# RUN adduser -D 13angs

# # run as 13angs
# USER 13angs
ENV TZ=Asia/Bangkok

VOLUME [ "/usr/src/app/data/backup" ]
VOLUME [ "/usr/src/app/data/restore" ]

CMD [ "python3", "./main.py" ]