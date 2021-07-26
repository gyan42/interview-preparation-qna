-- char : finxed length
-- varchar: variable length
-- mediumtext
-- longtext
-- MediumInt
-- Int
-- BigInt
-- Flaot(p, s) 
-- Double(p, s)
-- Date 		 YYYY-MM-DD  		  1000-01-01 to 9999-12-31
-- Datetime  	 YYYY-MM-DD HH:MI:SS  1000-01-01 00:00:00 to 9999-12-31 23:59:59
-- Timestamp  	 YYYY-MM-DD HH:MI:SS  1970-01-01 00:00:00 to 2037-12-31 23:59:59
-- Year  		 YYYY                 1901 to 2155
-- Time  		 HHH:MI:SS            −838:59:59 to 838:59:59

/*

*/
use bank;

drop table person;
CREATE TABLE person
(person_id SMALLINT UNSIGNED,
fname VARCHAR(20),
lname VARCHAR(20),
gender ENUM('M','F'),
birth_date DATE,
street VARCHAR(30),
city VARCHAR(20),
state VARCHAR(20),
country VARCHAR(20),
postal_code VARCHAR(20),
CONSTRAINT pk_person PRIMARY KEY (person_id)
);

desc person;

drop table favorite_food;
 CREATE TABLE favorite_food
 (person_id SMALLINT UNSIGNED,
 food VARCHAR(20),
 CONSTRAINT pk_favorite_food PRIMARY KEY (person_id, food),
 CONSTRAINT fk_fav_food_person_id FOREIGN KEY (person_id)
 REFERENCES person (person_id));
 
 DESC favorite_food;
 
 

ALTER TABLE person MODIFY person_id SMALLINT UNSIGNED AUTO_INCREMENT;

INSERT INTO person (fname, lname, gender, birth_date) VALUES ('William','Turner', 'M', '1972-05-27');

select * from person;


INSERT INTO favorite_food (person_id, food) VALUES (1, 'pizza');
INSERT INTO favorite_food (person_id, food) VALUES (1, 'cookies');
INSERT INTO favorite_food (person_id, food) VALUES (1, 'nachos');

select * from favorite_food;


select food from favorite_food where person_id = 1 order by food;
