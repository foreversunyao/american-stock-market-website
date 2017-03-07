#!/bin/bash  
docker exec -it $1 sh /crawler/stockinfo_collect/collect_daily.sh
docker exec -it $1 python /crawler/gnp/gnp_search.py GOOG
docker exec -it $1 python /crawler/elasticsearch_article/article.py
docker exec -it $1 python /crawler/elasticsearch_article/article_ana.py

10 * * * * docker exec -it 8158dab66020 sh /crawler/stockinfo_collect/collect_daily.sh
10 * * * 2 docker exec -it 8158dab66020 python /crawler/elasticsearch_article/article.py
22 * * * 1 sh /home/ubuntu/usstock/docker/gnp_search.sh
10 * * * 2 docker exec -it 8158dab66020 python /crawler/elasticsearch_article/article_ana.py
