Q1 = "SELECT COUNT(name) FROM Movie WHERE year < 2000;"

Q2 = "SELECT AVG(rank) FROM Movie WHERE year IN (1991);"

Q3 = "SELECT MIN(rank) FROM Movie WHERE year IN (1991);"

Q4 = "SELECT fname,lname FROM Actor INNER JOIN Cast ON id = pid WHERE mid = 27;"

Q5 = "SELECT COUNT(pid) FROM Actor INNER JOIN Cast ON id = pid WHERE fname = 'Jon' AND lname = 'Dough';"

Q6 = "SELECT name FROM Movie WHERE name LIKE 'Young Latin Girls%' AND year BETWEEN 2003 AND 2006;"

Q7 = """SELECT fname,lname FROM Director INNER JOIN MovieDirector ON Director.id = did 
         INNER JOIN Movie ON Movie.id = mid WHERE name LIKE 'Star Trek%';"""

Q8 = """SELECT name FROM Movie 
        INNER JOIN MovieDirector ON `Movie`.id = `MovieDirector`.mid 
        INNER JOIN Director ON `Director`.id = `MovieDirector`.did 
        INNER JOIN Cast ON `Cast`.mid =`MovieDirector`.mid 
        INNER JOIN Actor ON `Actor`.id = `Cast`.pid WHERE (Actor.fname = 'Jackie (I)' and 
        Director.fname = 'Jackie (I)') and (Actor.lname = 'Chan' and Director.lname = 'Chan') 
        ORDER BY name ASC;"""

Q9 = """SELECT fname,lname FROM Director INNER JOIN MovieDIRECTOR ON `Director`.`id`=did 
        INNER JOIN Movie ON `Movie`.`id`=mid WHERE year = 2001 GROUP BY did HAVING COUNT(mid)>=4 
        ORDER BY fname ASC,lname DESC;"""

Q10 = "SELECT gender,COUNT(gender) FROM Actor GROUP BY gender ORDER BY gender ASC;"

Q11 = """SELECT DISTINCT m1.name,m2.name, m1.rank, m1.year 
         FROM Movie AS m1 INNER JOIN Movie AS m2
         ON m1.id > m2.id WHERE m1.year = m2.year AND m1.rank = m2.rank 
         ORDER BY m1.name ASC LIMIT 100;"""

Q12 = """SELECT fname,year,rank 
         FROM Cast JOIN Actor ON Actor.id=pid
         JOIN Movie ON Movie.id = mid 
         ORDER BY fname ASC,year DESC LIMIT 100;"""
         
Q13 = """SELECT `Actor`.`fname`, `Director`.`fname`, AVG(rank) AS score 
         FROM MovieDirector 
         INNER JOIN Director ON `Director`.`id` = `MovieDirector`.`did` 
         INNER JOIN Movie ON `Movie`.`id` = `MovieDirector`.`mid` 
         INNER JOIN Cast ON `Cast`.`mid` = `MovieDirector`.`mid` 
         INNER JOIN Actor ON `Actor`.`id` = `Cast`.`pid` 
         GROUP BY `Actor`.`id`, `Director`.`id` 
         HAVING COUNT(`Movie`.`id`) >= 5 
         ORDER BY score DESC, `Director`.`fname` ASC, `Actor`.`fname` DESC LIMIT 100;"""

# Q13 = """SELECT Actor.fname, Director.fname, AVG(rank) AS score 
#          FROM Movie 
#          INNER JOIN Cast ON `Movie`.`id` = `Cast`.`mid' 
#          INNER JOIN Actor ON `Actor`.`id` = `Cast`.`pid` 
#          INNER JOIN MovieDirector ON `MovieDirector`.`mid` = `Cast`.`mid` 
#          INNER JOIN Director ON `Director`.`id` = `MovieDirector'.`did` 
#          GROUP BY Actor.id,Director.id HAVING COUNT(Movie.id) >= 5 
#          ORDER BY score DESC,Director.fname ASC, Actor.fname DESC;"""

#Q8 = """SELECT name FROM Movie INNER JOIN Cast ON `Movie`.id = `Cast`.mid INNER JOIN Actor ON `Actor`.id = `Cast`.pid INNER JOIN MovieDirector ON `MovieDirector`.mid =`Cast`.mid INNER JOIN Director ON `Director`.id = `MovieDirector`.mid WHERE (actor.fname = 'Jackie (I)' and director.fname = 'Jackie (I)') and (actor.lname = 'Chan' and director.lname = 'Chan') order by name ASC;"""
#Q8 = """SELECT name FROM Movie INNER JOIN MovieDirector ON `Movie`.id = `MovieDirector`.mid INNER JOIN Director on `Director`.id = `MovieDirector`.did INNER JOIN Cast ON `Cast`.mid =`MovieDirector`.mid INNER JOIN Actor ON `Actor`.id = `Cast`.pid WHERE (Actor.fname = 'Jackie (I)' and Director.fname = 'Jackie (I)') and (Actor.lname = 'Chan' and Director.lname = 'Chan') ORDER BY name ASC;"""




