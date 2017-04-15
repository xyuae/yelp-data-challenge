drop table if exists business;

create table business (
    city varchar(50),
    neighborhood varchar(60),
    name varchar(80),
    business_id char(22),
    longitude varchar(30),
    state varchar(5),
    postal_code varchar(20),
    stars char(3),
    address varchar(100),
    latitude varchar(30),
    review_count char(20),
    type char(8),
    is_open char(1),
    primary key (business_id)
)character set 'UTF8';

load data infile '/Users/Rui/Desktop/656/a1/q3/yelp_academic_dataset_business.csv' into table business
fields terminated by ','
ignore 1 lines;


drop table if exists user;

create table user(
    yelping_since char(10),
    useful varchar(10),
    compliment_photos varchar(10),
    compliment_list varchar(5),
    compliment_funny varchar(10),
    funny varchar(10),
    review_count varchar(10),
    fans varchar(10),
    type char(4),
    compliment_note varchar(10),
    compliment_plain varchar(10),
    compliment_writer varchar(10),
    compliment_cute varchar(10),
    average_stars char(4),
    user_id char(22),
    compliment_more varchar(10),
    compliment_hot varchar(10),
    cool varchar(10),
    name varchar(35),
    compliment_profile varchar(10),
    compliment_cool varchar(10),
    primary key (user_id)
)character set 'UTF8';

load data infile '/Users/Rui/Desktop/656/a1/q3/yelp_academic_dataset_user.csv' into table user
fields terminated by ','
ignore 1 lines;


drop table if exists checkin;

create table checkin(
    business_id char(22),
    time varchar(6),
    type char(7),
    foreign key (business_id) references business(business_id)
)character set 'UTF8';

load data infile '/Users/Rui/Desktop/656/a1/q3/yelp_academic_dataset_checkin.csv' into table checkin
fields terminated by ','
ignore 1 lines;


drop table if exists tip;

create table tip(
    user_id char(22),
    text text,
    business_id char(22),
    likes char(3),
    date char(10),
    type char(3),
    foreign key (user_id) references user(user_id),
    foreign key (business_id) references business(business_id)
)character set 'UTF8';

load data infile '/Users/Rui/Desktop/656/a1/q3/yelp_academic_dataset_tip.csv' into table tip
fields terminated by ','
ignore 1 lines;


drop table if exists attributes;

create table attributes(
    business_id char(22),
    attribute text,
    foreign key(business_id) references business(business_id)
)character set 'UTF8';

load data infile '/Users/Rui/Desktop/656/a1/q3/yelp_academic_dataset_attributes.csv' into table attributes
fields terminated by ','
ignore 1 lines;


drop table if exists categories;

create table categories(
    business_id char(22),
    category text,
    foreign key(business_id) references business(business_id)
)character set 'UTF8';

load data infile '/Users/Rui/Desktop/656/a1/q3/yelp_academic_dataset_categories.csv' into table categories
fields terminated by ','
ignore 1 lines;


drop table if exists elite;

create table elite(
    user_id char(22),
    elite text,
    foreign key(user_id) references user(user_id)
)character set 'UTF8';

load data infile '/Users/Rui/Desktop/656/a1/q3/yelp_academic_dataset_elite.csv' into table elite
fields terminated by ','
ignore 1 lines;


drop table if exists hours;

create table hours(
    business_id char(22),
    Monday char(11),
    Tuesday char(11),
    Wednesday char(11),
    Thursday char(11),
    Friday char(11),
    Saturday char(11),
    Sunday char(11),
    foreign key (business_id) references business(business_id)
)character set 'UTF8';

load data infile '/Users/Rui/Desktop/656/a1/q3/yelp_academic_dataset_hours.csv' into table hours
fields terminated by ','
ignore 1 lines;


drop table if exists friends;

create table friends(
    user_id char(22),
    friend_id char(22),
    foreign key (user_id) references user(user_id)
)character set 'UTF8';

load data infile '/Users/Rui/Desktop/656/a1/q3/yelp_academic_dataset_friends.csv' into table friends
fields terminated by ','
ignore 1 lines;


drop table if exists review;

create table review(
    funny char(5),
    user_id char(22),
    review_id char(22),
    text text,
    business_id char(22),
    stars char(3),
    date char(10),
    useful varchar(10),
    type char(6),
    cool varchar(10),
    primary key (review_id),
    foreign key (business_id) references business(business_id),
    foreign key (user_id) references user(user_id)
)character set 'UTF8';

load data infile '/Users/Rui/Desktop/656/a1/q3/yelp_academic_dataset_review.csv' into table review
fields terminated by ','
ignore 1 lines;
