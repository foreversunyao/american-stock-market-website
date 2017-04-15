#!/bin/bash  
docker exec -it $1 sh /crawler/stockinfo_collect/collect_daily.sh
docker exec -it $1 python /crawler/gnp/gnp_search.py GOOG
docker exec -it $1 python /crawler/elasticsearch_article/article.py
docker exec -it $1 python /crawler/elasticsearch_article/article_ana.py

10 * * * * docker exec 58869f6dd7a6 sh /crawler/stockinfo_collect/collect_daily.sh
10 * * * 2 docker exec  58869f6dd7a6 python /crawler/elasticsearch_article/article.py
22 * * * 1 sh /data/usstock/usstock/docker/search_gnp.sh 58869f6dd7a6
10 * * * 2 docker exec 58869f6dd7a6 python /crawler/elasticsearch_article/article_ana.py
