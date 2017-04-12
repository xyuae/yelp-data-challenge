DROP TABLE IF EXISTS User_gen;

CREATE TABLE User_gen (
	user_id VARCHAR(25),
    name VARCHAR(50),
    review_count int,
    useful int,
    funny int,
    cool int,
    fans int,
    average_stars float,
    compliment_hot int,
    compliment_more int,
    compliment_profile int,
    compliment_cute int,
    compliment_list int,
    compliment_note int,
    compliment_plain int,
    compliment_cool int,
    compliment_funny int,
    compliment_writer int,
    compliment_photos int,
	type varchar(10),
    user_key integer primary key auto_increment
) CHARACTER SET 'UTF8';

LOAD DATA LOCAL INFILE 'C:\\656\\user_general.csv' 
INTO TABLE User_gen FIELDS TERMINATED BY ',' optionally enclosed by '"' 
escaped by ''
lines terminated by '\r\n' ignore 1 lines (user_id,name,review_count,useful,funny,cool,fans,average_stars,compliment_hot,compliment_more,compliment_profile,compliment_cute,compliment_list,compliment_note,compliment_plain,compliment_cool,compliment_funny,compliment_writer,compliment_photos,type); 
