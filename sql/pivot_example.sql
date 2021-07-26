-- https://stackoverflow.com/questions/33017430/how-to-use-pivot-in-sql-server-without-aggregates
-- https://www.hackerrank.com/challenges/occupations/problem?h_r=next-challenge&h_v=zen
CREATE TABLE Occupations (
     NAME VARCHAR(MAX),
     Occupation VARCHAR(MAX)
    )
INSERT  INTO Occupations
VALUES
        ('Samantha','Doctor'),
        ('Julia','Actor'),
        ('Maria','Actor'),
        ('Meera','Singer'),
        ('Ashley','Professor'),
        ('Ketty','Professor'),
        ('Christeen','Professor'),
        ('Jane','Actor'),
        ('Jenny','Doctor'),
        ('Priya','Singer');


-- @Rookie_123 pivot basically groups all of your data that is not aggregated.. adding row number gives each
-- name another "grouping" to make them distinct by occupation so the MAX() aggregate does not just one name per
-- occupation, but instead gets one name per Occupation, Row_number. –

select [Doctor], [Professor], [Singer], [Actor] from (
    select row_number() over(partition by occupation order by name) as rn,
    name, occupation from occupations
) t
PIVOT(
    max(name)
    for occupation in ([Doctor], [Professor], [Singer], [Actor])
) as pt order by rn;