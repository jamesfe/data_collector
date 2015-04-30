DROP TABLE IF EXISTS tokens CASCADE;

DROP SEQUENCE IF EXISTS token_id_seq;
CREATE SEQUENCE token_id_seq;

CREATE TABLE tokens
(
  client VARCHAR,
  application VARCHAR,
  secret VARCHAR,
  username VARCHAR,
  token VARCHAR,
  use_period_secs INTEGER,
  max_uses INTEGER,
  token_id integer NOT NULL DEFAULT nextval('token_id_seq'::regclass)
);

DROP TABLE IF EXISTS token_use CASCADE;

DROP SEQUENCE IF EXISTS use_id_seq;
CREATE SEQUENCE use_id_seq;

CREATE TABLE token_use
(
  application VARCHAR,
  usage_time INTEGER,
  token_id INTEGER,
  use_id INTEGER NOT NULL DEFAULT nextval('use_id_seq'::regclass)
);
