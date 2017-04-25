#!/bin/bash
while read line;do docker exec $1 python /crawler/gnp/gnp_search.py "$line";done < usstock.list
#while read line;do  python gnp_search_local.py $line;done < usstock.list
