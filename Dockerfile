FROM alpine:3.8
RUN mkdir /app
COPY requirements.txt /app
RUN apk add -U --no-cache python3 py3-pip python3-dev bash \
  && apk add -U --no-cache --virtual .build-deps alpine-sdk \
  && pip3 install -r /app/requirements.txt \
  && apk del .build-deps \
  && rm -rf /var/cache/apk/*
COPY tilty_dashboard /app/tilty_dashboard
COPY config /app/config
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD []
