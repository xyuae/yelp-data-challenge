DROP TABLE IF EXISTS Tip;

CREATE TABLE Tip (

    text TEXT,
    date TEXT,
    likes TEXT,
    business_id VARCHAR(25),
    user_id VARCHAR(25),
	type varchar(10),
    tip_id integer primary key auto_increment
    #PRIMARY KEY ( hour_id)
) CHARACTER SET 'UTF8';

LOAD DATA LOCAL INFILE 'C:\\656\\tip.csv' 
INTO TABLE Tip FIELDS TERMINATED BY ',' optionally enclosed by '"' 
escaped by ''
lines terminated by '\n' ignore 1 lines (text,date,likes,business_id,user_id,type); 
