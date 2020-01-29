# Semistructured-Json-events-Python-pandas-DF-Mysql(DOCKER)

DESC: Using this REPO By executing below commands will turn semistructured json into pandas dataframe and it pushes it to MYSQL database which is built as part of this usecase to DEMO and as part of it it will even query that mysql db at the succesfull job.

* NOTE: If no Docker and just want to try script, still can be executed which gives the output and also throws exception as NO SQL DB AVAILABLE.
If docker and mysql approach is not used, please ignore tests failing on json_mysql_test.py
### Prerequisites
#### Python 3.6.* & Docker & GNU make

See installation instructions at: https://www.python.org/downloads/

See installation instructions Docker -- https://docs.docker.com/

Check you have python3 & Docker installed:

```bash
python3 --version
```

### Dependencies and data

#### Creating a virtual environment

Ensure your pip (package manager) is up to date:

```
pip install --upgrade pip
```

To check your pip version run:

```
pip --version
```

Create the virtual environment in the root of the cloned project:
```bash
python3.6 -m venv .venv
```
```windows
pip install virtualenv
virtualenv .venv
```

#### Activating the newly created virtual environment

You always want your virtual environment to be active when working on this project.

```bash
source ./.venv/bin/activate
```
```windows
.\.venv\Scripts\activate
```

#### Installing Python requirements

```
pip install -r requirements.txt
```

#### Slide event Data Json2Mysql (PANDAS)

#### INPUT

Json files are expected to be placed in input folder

#### Running make command to build and bring up the docker (if no make available please execute below commands manually in teminal under make docker-build) )
```
make docker-build
```
```
docker build ./ -t mysql-dbc
docker run --env="MYSQL_ROOT_PASSWORD=root_password" -p 3306:3306 -d mysql-dbc
```

#### Running tests and main program using 

#### docker(MYSQL LOCAL DATABASE) 

```bash
make RUN-WITH-MYSQL
```
```windows
make WIN-RUN-WITH-MYSQL
```

#### without docker just runs main program which aggrigates and prints on stdout after succesful test and main execution

```bash
make RUN
```
```windows
make WIN-RUN
```

#### Schedulling 
This can be Scheduled in unix(crontab) box following a script which activates virtual environment, pulling dependencies and executing above make commands 

#### Orther Approaches  

If going with on premise better go with pyspark and HDFS to do parallel Processing if expecting more records.

If choose to serverless with cloud technologies like AWS, etc. which in that case can do event processing when arrived using lambda to filter and get the required user_engagement and make them structured data into S3 and at the EOD trigger a (EC2, Fargate, or AWS GLUE) etl job which aggregate and push to sql database.
