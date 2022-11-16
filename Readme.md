swagger:
for consult the swagger 
http://127.0.0.1:5000/swagger-ui

if you need a random joke use = /jokes/
if you need Get a Chuck Norris Jokes use in /jokes/ ?choice=Chuck
if you need Geta Dad jokes use in /jokes/ ?choice=Dad

for the sum the 1 to the number use /sumOne?numer=

for the mcm use = mcnNumbers?numbers= 1,2,3,4,5
all methods use in /jokes/ GET, POST, PUT, DELETE 
The use of sql or non-sql databases must depend on the needs and the type of data, if I am looking to make use of the ACID properties, because the security and consistency of the data is very important, but if what I am looking for is speed, I would use no SQL database

this is a sentence for create table for pryect in sql
CREATE TABLE "jokes" (
	"id"	INTEGER NOT NULL UNIQUE,
	"joke"	TEXT NOT NULL,
	PRIMARY KEY("id")
);

in shell MongoDb for create a base data in mongo is 
shell Mongodb//
use jokes
db.joke.insert({id:1, joke:"newjoke"})


i use SQL with SQLlite3 because it is useful in development and easy to migrate, as well as when performing tests it works well in the development stage.
