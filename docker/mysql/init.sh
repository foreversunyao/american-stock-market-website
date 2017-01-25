#!/bin/bash
/usr/bin/mysqld_safe --skip-grant-tables &
sleep 5
mysql -e "create database test"
mysql test < /etc/mysql/load_data.sql
