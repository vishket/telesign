# telesign

REST API service to maintain collection of words

## Getting Started

**Pre requisites**

The app uses the Flask framework, the psycopg2 package to connect to DB
and the dotenv to load database connection strings

These dependencies can be installed using the requirements file 

```
pip install -r requirements.txt
```

**Download this project**

*Build from source:*

```
git clone -b v1 git@github.com:vishket/telesign.git

```

Alternatively, 

*Download telesign distribution*

```
wget -O FILE https://github.com/vishket/telesign/blob/v1/dist/telesign-0.1.1.tar.gz
gunzip FILE
tar -xzf FILE
```

## Configure database

Edit the .env file. Enter your PostgreSQL database connection settings

## Run

```
python telesign/telesign/app.py
```

This should start the application on the default port 5000

## Examples

POST new words

```
curl -H 'Content-Type: application/json' -X POST -d '["cat", "act", "bat", "eye", "eye", "Bit", "b33", "21324", "b%s"]' -i http://localhost:5000/v1/words
```

GET words count

```
curl -i http://localhost:5000/v1/words/count
```

GET palindrome count

```
curl -i http://localhost:5000/v1/palindromes/count
```

## Tests

*Unit Tests*

Can be executed by simply running

```
pytest test_telesign.py 
```

*Concurrency test*

abs_concurrent_requests.sh is a shell script that uses apache bench to
send concurrent requests to the application

To execute, 

```
./abs_concurrent_requests.sh
```

## Design considerations 

Framework: Flask

- Flask is a lightwight microframework that allows you to quickly develop 
web applications

- It provides a neat way to map routes to functions

- It support concurrent requests by setting the threading parameter to 
True

Database: PostgreSQL

- Provides great concurrency and data integrity tools by using the 
multiversion model to maintain consistency when multiple sessions attempt 
writing to the same data

- Allows creating an index for a column for faster lookups

- Using PostgreSQL allows data persistence, so sessions can see updates
from other sessions

Helper Functions

- Having all the helper/utility functions in a separate package prevents 
writing the same code for each calling function and also a nicer way to
extending the set of functions in the future
   
## Tradeoffs and justifications

SQLlite v PostgreSQL

- While SQLite was my first choice for the backend database due to it 
being lightweight and would have got the job done, there were limitations 
around handling concurrent requests. PostgreSQL is better at managing it

Flask v Django

- Flask is a microframework and is probably not best for large scale 
applications. It lacks handling high concurrent requests and doesn't scale
up well. But I felt like it would still be good enough for this use case
and allowed me to quickly develop the app. And I am also more 
comfortable working with Flask 

## Weaknesses in implementation 

- Exponential time complexity to check if word exists in collection 
before adding it into collection

- Storing entire database column locally in memory(collection array) 

## Future enhancements

- Security

Add support for Basic or OAuth2.0 to authenticate users trying to 
access endpoints 

- Caching

Enable response caching for resources that will not change often to 
improve performance

- More efficient checks for existing data

Checking if a word already exists in the database before inserting it is 
currently exponential in terms of complexity. I will have to figure out 
a more efficient way to bring it down to linear time complexity
