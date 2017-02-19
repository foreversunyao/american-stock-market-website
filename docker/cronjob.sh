#!/bin/bash  
docker exec -it $1 sh /crawler/stockinfo_collect/collect_daily.sh
docker exec -it $1 python /crawler/elasticsearch_article/article.py
