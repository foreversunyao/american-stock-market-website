#!/bin/bash
while read line;do docker exec -it 8158dab66020 python /crawler/gnp/gnp_search.py $line;done < usstock.list
