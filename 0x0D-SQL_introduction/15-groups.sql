-- script that lists the number of records with the same score in second_table.
SELECT score, count(*) AS number	-- Count of records for each score
FROM second_table			-- table containing data
GROUP BY score				-- Group data by score value
ORDER BY number DESC;			-- sort result by numberin desc
