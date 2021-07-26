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

Wildcard character
 Matches
_  Exactly one character
%  Any number of characters (including 0)

 SELECT lname
FROM employee
 WHERE lname LIKE '_a%e%';



*/
use bank;

drop table if exists person;

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

drop table if exists favorite_food;

 CREATE TABLE favorite_food
 (person_id SMALLINT UNSIGNED,
 food VARCHAR(20),
 CONSTRAINT pk_favorite_food PRIMARY KEY (person_id, food),
 CONSTRAINT fk_fav_food_person_id FOREIGN KEY (person_id)
 REFERENCES person (person_id));
 
 DESC favorite_food;

 #------------------------------------------------------------------------------------------


ALTER TABLE person MODIFY person_id SMALLINT UNSIGNED AUTO_INCREMENT;

INSERT INTO person (fname, lname, gender, birth_date) VALUES ('William','Turner', 'M', '1972-05-27');

select * from person;


INSERT INTO favorite_food (person_id, food) VALUES (1, 'pizza');
INSERT INTO favorite_food (person_id, food) VALUES (1, 'cookies');
INSERT INTO favorite_food (person_id, food) VALUES (1, 'nachos');

select * from favorite_food;

#------------------------------------------------------------------------------------------

select food from favorite_food where person_id = 1 order by food;

UPDATE person SET street = '1225 Tremont St.',  city = 'Boston',
 state = 'MA', country = 'USA', postal_code = '02138'
WHERE person_id = 1;


DELETE FROM person WHERE person_id = 2;


show tables;

#------------------------------------------------------------------------------------------

SELECT concat('DROP TABLE IF EXISTS `', table_name, '`;')
FROM information_schema.tables
WHERE table_schema = 'bank';

SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS `account`;
DROP TABLE IF EXISTS `branch`;
DROP TABLE IF EXISTS `business`;
DROP TABLE IF EXISTS `customer`;
DROP TABLE IF EXISTS `department`;
DROP TABLE IF EXISTS `employee`;
DROP TABLE IF EXISTS `favorite_food`;
DROP TABLE IF EXISTS `individual`;
DROP TABLE IF EXISTS `officer`;
DROP TABLE IF EXISTS `person`;
DROP TABLE IF EXISTS `product`;
DROP TABLE IF EXISTS `product_type`;
DROP TABLE IF EXISTS `transaction`;
SET FOREIGN_KEY_CHECKS = 1;


#------------------------------------------------------------------------------------------

desc customer;

select count(*) from account;

select * from account;

select emp_id from employee WHERE lname = 'Bkadfl';

select fname, lname from employee e; 

select * from department d ;

select emp_id , 'ACTIVE', emp_id * 2, UPPER(fname) from employee e;


select version(), user(), database();


select emp_id , 'ACTIVE', emp_id * 2 as wow, UPPER(fname) as uname from employee e;

SELECT DISTINCT  cust_id from account a ;

select e.emp_id , e.fname , e.lname from (select * from employee) e; 

create view employee_vw as select * from employee e;

SELECT * from employee_vw;




select * from employee e ;
SELECT * from department d ;

SELECT e.emp_id, e.fname , e.lname , d.name from employee e inner join department d on e.dept_id = d.dept_id WHERE e.emp_id > 5 order by e.emp_id;

SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

SELECT d.name, count(e.emp_id) as c from employee e inner join department d on e.dept_id = d.dept_id GROUP by d.name HAVING c > 2;



select * from customer c order by RIGHT (fed_id, 3);

SELECT * FROM employee e ;

SELECT emp_id, fname, lname, start_date
FROM employee
WHERE start_date < '2003-01-01'
 AND start_date >= '2001-01-01';


 SELECT emp_id, fname, lname, start_date
FROM employee
WHERE start_date BETWEEN '2001-01-01' AND '2007-01-01';


 SELECT account_id, product_cd, cust_id, avail_balance
FROM account
WHERE avail_balance BETWEEN 3000 AND 5000;



SELECT account_id, product_cd, cust_id, avail_balance
FROM account
 WHERE product_cd not IN (SELECT product_cd FROM product
 WHERE product_type_cd = 'ACCOUNT');


 SELECT lname
FROM employee
 WHERE lname LIKE '_a%e%';

SELECT cust_id, fed_id
FROM customer
WHERE fed_id LIKE '___-__-____';


SELECT emp_id, fname, lname
FROM employee
WHERE lname REGEXP '^[FG]';


select e.fname , d.name 342from employee e inner join department d on e.dept_id = d.dept_id;


SELECT a.account_id, a.cust_id, a.open_date, a.product_cd
FROM account a, branch b, employee e
WHERE a.open_emp_id = e.emp_id
 AND e.start_date < '2007-01-01'
 AND e.assigned_branch_id = b.branch_id
 AND (e.title = 'Teller' OR e.title = 'Head Teller')
 AND b.name = 'Woburn Branch';



SELECT a.account_id, a.cust_id, a.open_date, a.product_cd
 FROM account a INNER JOIN employee e
 ON a.open_emp_id = e.emp_id
 INNER JOIN branch b
 ON e.assigned_branch_id = b.branch_id
WHERE e.start_date < '2007-01-01'
 AND (e.title = 'Teller' OR e.title = 'Head Teller')
 AND b.name = 'Woburn Branch';



SELECT a.account_id, a.cust_id, a.open_date, a.product_cd FROM account a INNER JOIN
 (SELECT emp_id, assigned_branch_id
  FROM employee
 WHERE start_date < '2007-01-01'
 AND (title = 'Teller' OR title = 'Head Teller')) e
 ON a.open_emp_id = e.emp_id
 INNER JOIN
 (SELECT branch_id
 FROM branch
 WHERE name = 'Woburn Branch') b
 ON e.assigned_branch_id = b.branch_id;


#------------------------------------------------------------------------------------------
CREATE TABLE string_tbl
(char_fld CHAR(30),
vchar_fld VARCHAR(30),
text_fld TEXT
);

 INSERT INTO string_tbl (char_fld, vchar_fld, text_fld)
VALUES ('This is char data',
 'This is varchar data',
 'This is text data');

select * from string_tbl;
UPDATE string_tbl
SET text_fld = 'This string doesn''t work';

#------------------------------------------------------------------------------------------

 SELECT @@global.time_zone, @@session.time_zone;

#------------------------------------------------------------------------------------------

 SELECT DATE_ADD(CURRENT_DATE(), INTERVAL 5 DAY);

#------------------------------------------------------------------------------------------

#non co-related sub query

 SELECT e.emp_id
FROM employee e INNER JOIN branch b
 ON e.assigned_branch_id = b.branch_id
WHERE e.title = 'Teller' AND b.city = 'Woburn';



SELECT e.emp_id
 FROM employee e INNER JOIN branch b
 ON e.assigned_branch_id = b.branch_id
 WHERE e.title = 'Head Teller' AND b.city = 'Woburn';
 
 
SELECT account_id, product_cd, cust_id, avail_balance
 FROM account
 WHERE open_emp_id <> (SELECT e.emp_id
 FROM employee e INNER JOIN branch b
 ON e.assigned_branch_id = b.branch_id
 WHERE e.title = 'Head Teller' AND b.city = 'Woburn');

#------------------------------------------------------------------------------------------
# Joins

select account_id, cust_id from account a ;
SELECT cust_id from customer c ;

SELECT a.account_id, a.cust_id from account a inner join customer c on a.cust_id = c.cust_id ;

SELECT a.account_id, b.name from account a inner join business b on a.cust_id = b.cust_id ;

SELECT a.account_id, b.name from account a left outer join business b on a.cust_id = b.cust_id ;

SELECT a.account_id, a.cust_id, i.fname, i.lname FROM account a LEFT OUTER JOIN individual i ON a.cust_id = i.cust_id;

SELECT a.account_id, b.name from account a right outer join business b on a.cust_id = b.cust_id ;

#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------


