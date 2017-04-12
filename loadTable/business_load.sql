DROP TABLE IF EXISTS business;

CREATE TABLE business (
	business_id VARCHAR(25),
	name TEXT, 
    neighborhood TEXT, 
    address TEXT, 
    city TEXT, 
    state varchar(10), 
    postal_code varchar(10), 
    latitude float,
	longitude float, 
    stars float,
    review_count float,
    is_open boolean, 
    type varchar(10),
    primary key(business_id)
    #hour_id integer primary key auto_increment
    #PRIMARY KEY ( hour_id)
) CHARACTER SET 'UTF8';

LOAD DATA LOCAL INFILE 'C:\\656\\business.csv' 
INTO TABLE business FIELDS TERMINATED BY ',' 
optionally enclosed by '"' 
escaped by ''
lines terminated by '\r\n' ignore 1 lines;  