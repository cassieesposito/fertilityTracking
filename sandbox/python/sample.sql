BEGIN TRANSACTION;
CREATE TABLE people (id integer PRIMARY KEY, first_name text NOT NULL, last_name text NOT NULL, age integer );
INSERT INTO "people" VALUES(1,'John','Doe',33);
COMMIT;
