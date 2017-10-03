# usstock


This project is for interest, it provides a convenient way to watch USA stock data and related articles for stock analysis.

This website project has two main components, one is the daily trend of each stock , the other is the articles of each stock and emotional analysis of these articles, for example , article A is negative of yahoo stock and article B is positive of yahoo stock.

It also has daily top gainers and top losers, and 20%, 5% up proportion and 20% 5% down proportion. Other functions are coding now.






## Installation (Using Docker container)

1. Download project by "git clone https://github.com/foreversunyao/usstock.git "

2. cd usstock/docker

3. docker-compose up





## Quick Example  
###### cron job   
docker exec -it dockerid sh /crawler/stockinfo_collect/collect_daily.sh --collect stock data (price volume and so on)  

sh /data/usstock/usstock/docker/search_gnp.sh dockerid --search alphabet news by google  

docker exec -it dockerid python /crawler/elasticsearch_article/article.py --load article to elasticsearch  

docker exec -it dockerid python /crawler/elasticsearch_article/article_ana.py --analyze article by "SentimentIntensityAnalyzer"  

###### demo web  
http://127.0.0.1:8888/index  

###### search result
images:
   ![alt tag](https://github.com/foreversunyao/american-stock-market-website/blob/master/website1.png)
   
   ![alt tag](https://github.com/foreversunyao/american-stock-market-website/blob/master/website2.png)
## FAQ

**Q: ?**<br>
