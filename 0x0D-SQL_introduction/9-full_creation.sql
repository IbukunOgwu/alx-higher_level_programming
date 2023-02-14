--Creates and fills second_table with attributes id, name and score in MYSQL server with multiple rows.
CREATE TABLE IF NOT EXISTS 'second_table' ('id' INT, 'name' VARCHAR(256), 'score' INT);
CREATE INTO 'second_table' ('id', 'name', 'score') VALUES (1, "John", 10);
CREATE INTO 'second_table' ('id', 'name', 'score') VALUES (2, "Alex", 3);
CREATE INTO 'second_table' ('id', 'name', 'score') VALUES (3, "Bob", 14);
CREATE INTO 'second_table' ('id', 'name', 'score') VALUES (4, "George", 8);
