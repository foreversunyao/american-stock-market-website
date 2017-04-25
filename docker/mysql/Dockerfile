FROM mysql
ENV MYSQL_ROOT_PASSWORD=admin \
  MYSQL_DATABASE=db_stock \
  MYSQL_USER=admin \
  MYSQL_PASSWORD=admin
COPY load_data.sql /docker-entrypoint-initdb.d/load_data.sql
EXPOSE 3306
