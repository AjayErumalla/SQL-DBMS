Q1 = """SELECT A.id,A.fname,A.lname,A.gender 
FROM Actor AS A
INNER JOIN Cast ON A.id = `Cast`.pid 
INNER JOIN Movie ON `Movie`.id = `Cast`.mid
WHERE `Movie`.name LIKE 'Annie%';"""

Q2 = """SELECT M.id,M.name,M.rank,M.year 
FROM Movie AS M
INNER JOIN MovieDirector ON M.id = MovieDirector.mid
INNER JOIN Director ON `Director`.id = `MovieDirector`.did
WHERE Director.fname = 'Biff' AND Director.lname = 'Malibu' AND M.year IN(1999,1994,2003)
ORDER BY M.rank DESC,M.year ASC;"""

Q3 = """SELECT year,COUNT(id) AS no_of_movies 
FROM Movie
GROUP BY year HAVING AVG(rank) > (SELECT AVG(rank) FROM Movie)
ORDER BY year ASC;
"""

Q4 = """SELECT M.id,M.name,M.year,M.rank 
FROM Movie AS M
WHERE M.year = 2001 AND (rank < (SELECT AVG(rank) FROM Movie WHERE year = 2001))
ORDER BY M.rank DESC LIMIT 10;
"""

Q5 = """SELECT M.id AS movie_id,sum(gender = 'F') AS no_of_female_actors,
sum(gender='M') AS no_of_male_actors
FROM Actor AS A INNER JOIN Cast As C ON C.pid = A.id
INNER JOIN Movie AS M ON M.id = C.mid GROUP BY M.id ORDER BY M.id ASC LIMIT 100;"""


# Q5 = """SELECT `Movie`.id AS movie_id,(SELECT COUNT(gender) GROUP BY gender = 'F' FROM Actor) AS no_of_female_actors,
# (SELECT COUNT(gender) GROUP BY gender = 'M' FROM Actor) AS no_of_male_actors
# FROM Actor INNER JOIN Cast ON `Cast`.pid = `Actor`.id 
# INNER JOIN Movie ON `Cast`.mid = `Movie`.id 
# GROUP BY gender 
# ORDER BY movie_id ASC LIMIT 100; """

# Q5 = """SELECT `Movie`.id AS movie_id,(SELECT COUNT(gender) GROUP BY gender = 'F' FROM Actor) AS no_of_female_actors,
# (SELECT COUNT(gender) GROUP BY gender = 'M' FROM Actor) AS no_of_male_actors
# FROM Actor INNER JOIN Cast ON `Cast`.pid = `Actor`.id 
# INNER JOIN Movie ON `Cast`.mid = `Movie`.id GROUP BY gender ORDER BY movie_id ASC LIMIT 100;"""

# Q5 = """SELECT `Movie`.id AS movie_id,COUNT(gender = 'F') AS no_of_female_actors,
# COUNT(gender = 'M') AS no_of_male_actors
# FROM Actor INNER JOIN Cast ON `Cast`.pid = `Actor`.id 
# INNER JOIN Movie ON `Cast`.mid = `Movie`.id GROUP BY gender ORDER BY movie_id ASC LIMIT 100;"""


# Q5 = """SELECT Movie.id AS movie_id,COUNT(gender = 'F') AS no_of_female_actors,
# COUNT(gender = 'M) AS no_of_male_actors
# FROM Actor INNER JOIN Cast ON Cast.pid = Actor.id 
# INNER JOIN Movie ON Cast.mid = Movie.id LIMIT 100;"""


Q6 = """SELECT DISTINCT pid 
FROM Cast
INNER JOIN Movie ON `Movie`.id = `Cast`.mid 
GROUP BY pid,mid HAVING COUNT(DISTINCT role) > 1 LIMIT 100;"""


Q7 = """SELECT fname,COUNT(fname) AS count 
FROM Director 
GROUP BY fname HAVING count >1;"""

Q8 = """SELECT * FROM Director AS D
WHERE EXISTS (SELECT MD.did FROM Cast C
INNER JOIN MovieDirector MD ON MD.mid = C.mid
WHERE MD.did = D.id GROUP BY MD.did,MD.mid HAVING COUNT(DISTINCT C.pid) >= 100)
AND NOT EXISTS
(SELECT MD.did FROM Cast C
INNER JOIN MovieDirector MD ON MD.mid = C.mid
WHERE MD.did = D.id GROUP BY MD.did,MD.mid HAVING COUNT(DISTINCT C.pid) < 100);"""