-- Create table second_table if not exists
CREATE TABLE IF NOT EXISTS second_table(
	id INT PRIMARY KEY,	-- define id as primary key
	name VARCHAR(256),	-- define name to store strings
	score INT		-- define score to store integers
);
-- Insert data into second_table
-- use ignore to avoid error
INSERT IGNORE INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT IGNORE INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT IGNORE INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT IGNORE INTO second_table (id, name, score) VALUES (4, 'George', 8);
