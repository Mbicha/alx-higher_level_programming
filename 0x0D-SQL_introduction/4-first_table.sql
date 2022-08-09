-- create table first_table in current database.
-- the table has id, and name fields.
-- the database should be passed as an argument.
-- if the table already exists, the script should not fail.

CREATE TABLE if not exists first_table(
    id INT,
    name VARCHAR(256)
);
