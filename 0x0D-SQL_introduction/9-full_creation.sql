-- Create table second_table if not exists
CREATE TABLE IF NOT EXISTS second_table(
	id INT AUTO_INCREMENT PRIMARY KEY,	-- define id as primary key
	name VARCHAR(256),	-- define name to store strings
	score INT		-- define score to store integers
);
-- Insert data into second_table
INSERT INTO second_table(name, score) VALUES('John', 10);
INSERT INTO second_table(name, score) VALUES('Alex', 3);
INSERT INTO second_table(name, score) VALUES('Bob', 14);
INSERT INTO second_table(name, score) VALUES('George', 8);
