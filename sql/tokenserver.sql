CREATE TABLE `tokens` (
	`client`	TEXT,
	`application`	TEXT,
	`secret`	TEXT,
	`username`	TEXT,
  `token` TEXT,
  `use_period` INTEGER,
	`tokenid`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE
);


CREATE TABLE `tokenuse` (
  `application` TEXT,
	`usage_time` REAL,
	`tokenid`	TEXT,
	`useid`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE
);