DROP TABLE IF EXISTS Business_hour;

CREATE TABLE Business_hour (
    business_id VARCHAR(25),
	hour VARCHAR(25),
    hour_id integer primary key auto_increment
    #PRIMARY KEY ( hour_id)
) CHARACTER SET 'UTF8';

LOAD DATA LOCAL INFILE 'C:\\656\\business_hours.csv' 
INTO TABLE Business_hour FIELDS TERMINATED BY ',' optionally enclosed by '"' 
lines terminated by '\n' ignore 1 lines (business_id, hour); 
