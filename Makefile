docker-build:
	docker build ./ -t mysql-dbc
	docker run --env="MYSQL_ROOT_PASSWORD=root_password" -p 3306:3306 -d mysql-dbc
	sleep 10