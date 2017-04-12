DROP TABLE IF EXISTS Review_gene;

CREATE TABLE Review_gene (
	review_id VARCHAR(25),
	user_id VARCHAR(25),
    business_id VARCHAR(25),
    stars float,
    date DATE,
    text mediumtext,
    useful text,
    funny text,
    cool text,
	type varchar(15),
    primary key(review_id)
) CHARACTER SET 'UTF8';

LOAD DATA LOCAL INFILE 'C:\\656\\review.csv' 
INTO TABLE Review_gene FIELDS TERMINATED BY ',' optionally enclosed by '"' 
escaped by ''
lines terminated by '\n' ignore 1 lines;