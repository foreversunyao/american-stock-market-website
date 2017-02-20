# usstock


This project is for interest, it provides a convenient way to watch USA stock data and related articles for stock analysis.

This website project has two main components, one is the daily trend of each stock , the other is the articles of each stock and emotional analysis of these articles, for example , article A is negative of yahoo stock and article B is positive of yahoo stock.

It also has daily top gainers and top losers, and 20%, 5% up proportion and 20% 5% down proportion. Other functions are coding now.






## Installation (Using Docker container)

1. Download project by "git clone https://github.com/foreversunyao/usstock.git "

2. cd usstock/docker

3. docker-compose up

4. docker exec -it $1 sh /crawler/stockinfo_collect/collect_daily.sh 
   docker exec -it $1 python /crawler/elasticsearch_article/article.py



## Quick Example




## FAQ

**Q: ?**<br>
