FROM python:3.7-slim
RUN mkdir /app
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY config /app/config
COPY tilty_dashboard /app/tilty_dashboard
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD []
