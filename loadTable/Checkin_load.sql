DROP TABLE IF EXISTS Checkin;

CREATE TABLE Checkin (
	time TEXT,
    business_id VARCHAR(25),
	type varchar(10),
    checkin_id integer primary key auto_increment
    #PRIMARY KEY ( hour_id)
) CHARACTER SET 'UTF8';

LOAD DATA LOCAL INFILE 'C:\\656\\checkin.csv' 
INTO TABLE Checkin FIELDS TERMINATED BY ',' optionally enclosed by '"' 
lines terminated by '\n' ignore 1 lines (time, business_id); 
