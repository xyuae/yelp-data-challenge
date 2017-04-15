DROP TABLE IF EXISTS Business;

CREATE TABLE Business (
	business_id VARCHAR(30),
	name TEXT, 
    neighborhood TEXT, 
    address TEXT, 
    city TEXT, 
    state TEXT, 
    postal_code varchar(50), 
    latitude float,
	longitude float, 
    stars float,
    review_count int,
    is_open int, 
    type varchar(20),
    primary key(business_id)
    #hour_id integer primary key auto_increment
    #PRIMARY KEY ( hour_id)
) CHARACTER SET 'UTF8';

LOAD DATA LOCAL INFILE 'C:\\Users\\Xiaojun(Tony)\\Documents\\GitHub\\yelp-data-challenge\\data\\clean_sample_business.csv'
INTO TABLE Business FIELDS TERMINATED BY ',' 
optionally enclosed by '"' 
escaped by ''
lines terminated by '\n' ignore 1 lines 
(business_id,name,neighborhood,address,city,state,postal_code,latitude,longitude,stars,review_count,is_open,type);  
