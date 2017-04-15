DROP TABLE IF EXISTS User;

CREATE TABLE User (
	user_id VARCHAR(25),
	yelping_since VARCHAR(10),
    name VARCHAR(50),
    review_count int,
	friends int,
    useful int,
    funny int,
    cool int,
    fans int,
	elite int,
    average_stars float
) CHARACTER SET 'UTF8';

LOAD DATA LOCAL INFILE 'C:\\Users\\Xiaojun(Tony)\\Documents\\GitHub\\yelp-data-challenge\\data\\clean_sample_user.csv'
INTO TABLE User FIELDS TERMINATED BY ',' optionally enclosed by '"' 
escaped by ''
lines terminated by '\r\n' ignore 1 lines (yelping_since,useful,average_stars,user_id,elite,cool,funny,review_count,name,friends,fans); 
