CREATE TABLE `tokens` (
	`client`	TEXT,
	`application`	TEXT,
	`secret`	TEXT,
	`username`	TEXT,
  `token` TEXT,
	`tokenid`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE
);


CREATE TABLE `tokenuse` (
	`min_period`	INTEGER,
	`usage`	INTEGER,
	`tokenid`	TEXT,
	`useid`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE
);