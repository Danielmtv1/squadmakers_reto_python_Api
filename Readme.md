swagger:

http://127.0.0.1:5000/swagger-ui



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
