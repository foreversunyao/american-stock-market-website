#!/bin/bash
today=$(date -d "-1 day" +"%Y%m%d")
yesterday=$(date -d "-2 day" +"%Y%m%d")
echo $today $yesterday
/usr/bin/python2.7 stockinfo_collect.py $yesterday $today
if [ $? -eq 0 ]
then
	echo "success"
fi

