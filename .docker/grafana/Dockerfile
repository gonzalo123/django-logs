FROM grafana/grafana:6.7.1

COPY ./grafana.ini /etc/grafana/grafana.ini

COPY ./entrypoint.sh .

RUN rm -rf /var/lib/grafana/.init

ENTRYPOINT ["sh", "./entrypoint.sh"]
