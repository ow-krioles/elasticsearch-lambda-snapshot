FROM elasticsearch

RUN plugin install mobz/elasticsearch-head
RUN plugin install cloud-aws

EXPOSE 9200 9300

CMD ["elasticsearch"]
