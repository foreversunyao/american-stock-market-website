DROP USER 'admin'@'%';
CREATE USER 'admin'@'%' IDENTIFIED BY 'admin' ;
GRANT ALL ON *.* TO 'admin'@'%' WITH GRANT OPTION ;
FLUSH PRIVILEGES ;
CREATE DATABASE db_stock2 ;
use db_stock ;
create table t2(id int) ;
insert into t2 values (1) ;
use db_stock2 ;
create table t2(id int) ;
insert into t2 values (13) ;