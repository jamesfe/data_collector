CREATE TABLE tokens (
   application TEXT,
   client TEXT,
   secret TEXT,
   username TEXT,
);

CREATE TABLE tokenuse (
   token_use INTEGER,
   min_period INTEGER,
   usage INTEGER,
   start_time TEXT
);