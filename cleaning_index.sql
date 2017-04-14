SET SQL_SAFE_UPDATES = 0; 

SET GLOBAL innodb_buffer_pool_size=402653184;

ALTER TABLE `review` ADD INDEX `idx_review_duplicate` (`review_id`) USING BTREE;
ALTER TABLE `review` ADD INDEX `idx_review_useful` (`useful`) USING BTREE;
ALTER TABLE `review` ADD INDEX `idx_review_user` (`user_id`) USING BTREE;
ALTER TABLE `review` ADD INDEX `idx_review_business` (`business_id`) USING BTREE;

ALTER TABLE review ADD UNIQUE (review_id);

DELETE review FROM review
  INNER JOIN
  (SELECT review.user_id
   FROM review
     LEFT JOIN `user`
       ON user.user_id = review.user_id
   WHERE `user`.user_id IS NULL
  ) AS X
    ON review.user_id = X.user_id;

ALTER TABLE `review` ADD INDEX `idx_user_review` (`review_id`) USING BTREE;
ALTER TABLE `review` ADD INDEX `idx_review_` (`yearID`, `lgID`, `teamID`) USING BTREE;

ALTER TABLE `user` ADD PRIMARY KEY (`user_id`);


