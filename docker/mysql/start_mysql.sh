#!/bin/bash

/usr/bin/mysqld_safe --defaults-file=/data/my.cnf &
sleep 10s
/usr/sbin/mysqld --initialize --datadir=/data/mysql/data --basedir=/data/mysql
echo "GRANT ALL ON *.* TO root@'%' IDENTIFIED BY 'admin' WITH GRANT OPTION; FLUSH PRIVILEGES" | mysql
#sh /data/load.sh
killall mysqld
sleep 10s
/usr/bin/mysqld_safe --defaults-file=/data/my.cnf
