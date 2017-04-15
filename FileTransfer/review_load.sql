DROP TABLE IF EXISTS Review;

CREATE TABLE Review (
	review_id VARCHAR(25),
	user_id VARCHAR(25),
    business_id VARCHAR(25),
    stars float,
    text int,
    useful int,
    funny int,
    cool int
) CHARACTER SET 'UTF8';

LOAD DATA LOCAL INFILE 'C:\\Users\\Xiaojun(Tony)\\Documents\\GitHub\\yelp-data-challenge\\data\\clean_sample_review.csv'
INTO TABLE Review FIELDS TERMINATED BY ',' optionally enclosed by '"' 
escaped by ''
lines terminated by '\n' ignore 1 lines (funny,user_id,review_id,text,business_id,stars,useful,cool);