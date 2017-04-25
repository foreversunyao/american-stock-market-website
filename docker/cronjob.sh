#!/bin/bash  
###collect stock value every day
docker exec -it $1 sh /crawler/stockinfo_collect/collect_daily.sh
###search search stock articles  by google news search
docker exec -it $1 sh /crawler/gnp/gnp_search.sh
###load article to elasticsearch
docker exec -it $1 python /crawler/elasticsearch_article/article.py
###analyse article by emoiton
docker exec -it $1 python /crawler/elasticsearch_article/article_ana.py

