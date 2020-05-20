t1 = "CREATE TABLE Student(student_id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(200),email VARCHAR(250));"

t2 = """CREATE TABLE Project(project_id INTEGER PRIMARY KEY AUTOINCREMENT,title VARCHAR(200),student_id INT,
      FOREIGN KEY(student_id) REFERENCES Student(student_id));"""
      
p1  = "SELECT * FROM Student;"
p2 = "SELECT * FROM Project;"

CREATE TABLE Project(project_id INTEGER PRIMARY KEY AUTOINCREMENT,title VARCHAR(200),student_id INT,FOREIGN KEY(student_id) REFERENCES Student(student_id));


Detecting E Banking Phishing Websites Using Associative Classification


CREATE TABLE Employee (employee_id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(100), salary FLOAT);


CREATE TABLE Project(project_id INTEGER PRIMARY KEY AUTOINCREMENT,title VARCHAR(100));
                      
                      
CREATE TABLE EmployeeProjects(project_id INTEGER NOT NULL, employee_id INTEGER NOT NULL, project_details_id INTEGER PRIMARY KEY AUTOINCREMENT,FOREIGN KEY (employee_id)REFERENCES Employee (employee_id), FOREIGN KEY (project_id)REFERENCES Project (project_id));
               
               
                      
                      
CREATE TABLE Owner(owner_id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(250));
CREATE TABLE Car(car_id INTEGER PRIMARY KEY AUTOINCREMENT,model_no VARCHAR(250),owner_id INT,FOREIGN KEY(owner_id) REFERENCES Owner(owner_id) ON DELETE CASCADE);
                      
SELECT * FROM Owner INNER JOIN Car on Owner.owner_id==Car.owner_id;

SELECT * FROM Owner LEFT JOIN Car on Owner.owner_id==Car.owner_id;

SELECT fname AS names, Count(mid) AS movies_count FROM Actor INNER JOIN Cast ON id = pid 
                         WHERE fname LIKE 'Antonio%' GROUP BY mid LIMIT 10;
                         
SELECT fname,lname FROM Actor LEFT JOIN Cast ON id == Pid Limit 50;

SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);


FROM
	tracks
INNER JOIN albums ON albums.albumid = tracks.albumid
INNER JOIN artists ON artists.artistid = albums.artistid
WHERE
	artists.artistid = 10;
	
Q1 = '''SELECT AVG(age) FROM Player;'''

Q2 = '''SELECT match_no, play_date FROM Match WHERE audience > 50000 ORDER BY match_no ASC;'''

Q3 = '''SELECT team_id, COUNT(win_lose) AS Win FROM MatchTeamDetails WHERE win_lose = "W" GROUP BY team_id ORDER BY Win DESC, team_id ASC;'''

Q4 = '''SELECT match_no, play_date FROM Match WHERE stop1_sec > (SELECT AVG(stop1_sec) FROM Match) ORDER BY match_no DESC, play_date DESC;'''

Q5 = '''SELECT `Match`.`match_no`, `Team`.`name`, `Player`.`name` FROM MatchCaptain INNER JOIN Team on `MatchCaptain`.`team_id` = `Team`.`team_id` INNER JOIN Match on `MatchCaptain`.`match_no` = `Match`.`match_no` INNER JOIN Player on `MatchCaptain`.`captain` = `Player`.`player_id` ORDER BY `Match`.`match_no` ASC, `Team`.`name` ASC;'''

Q6 = '''SELECT match_no, `Player`.`name`, jersey_no From Match INNER JOIN Player on `Player`.`player_id` = `Match`.`player_of_match` ORDER BY match_no ASC;'''

Q7 = '''SELECT `Team`.`name` ,AVG(`Player`.`age`) AS avg_age FROM Player INNER JOIN Team on `Player`.`team_id` = `Team`.`team_id` GROUP BY `Team`.`name` HAVING AVG(`Player`.`age`) > 26 ORDER BY `Team`.`name` ASC;'''

Q8 = '''SELECT `Player`.`name`, `Player`.`jersey_no`, `Player`.`age`, COUNT(`GoalDetails`.`player_id`) AS no_of_goals FROM GoalDetails INNER JOIN Player on `Player`.`player_id` = `GoalDetails`.`player_id` GROUP BY `Player`.`player_id` HAVING `Player`.`age` <= 27 ORDER BY no_of_goals DESC,`Player`.`name` ASC;'''

Q9 = '''SELECT team_id, COUNT(goal_id)*100.0/(SELECT COUNT(goal_id) FROM GoalDetails)
        FROM GoalDetails
        GROUP BY team_id
        HAVING COUNT(goal_id) != 0;'''
        
Q10 = '''SELECT AVG(avg_scores)
         FROM
         (SELECT COUNT(goal_id) AS avg_scores
         FROM Team JOIN GoalDetails ON Team.team_id = `GoalDetails`.team_id
         GROUP BY `Team`.team_id) AS scores;'''
        
Q11 = '''SELECT player_id, name, date_of_birth
         FROM Player AS P
         WHERE NOT EXISTS(SELECT goal_id FROM GoalDetails WHERE `GoalDetails`.player_id = P.player_id)
         ORDER BY player_id ASC;'''

Q12 = '''SELECT `T`.name, `M`.match_no, audience AS audience, audience - (SELECT AVG(audience) FROM Match JOIN MatchTeamDetails ON `Match`.match_no = `MatchTeamDetails`.match_no AND T.team_id = `MatchTeamDetails`.team_id)
         FROM MatchTeamDetails JOIN Match AS M ON `MatchTeamDetails`.match_no = `M`.match_no
         JOIN Team AS T ON `MatchTeamDetails`.team_id = `T`.team_id
         ORDER BY `M`.match_no ASC;'''

	
	
Q1 = "SELECT COUNT(*) FROM Movie WHERE year BETWEEN 1981 AND 1999;"

Q2 = "SELECT AVG(rank) FROM Movie WHERE year = 1991;"
	
Q3 = "SELECT MIN(rank) FROM Movie WHERE year = 1991;"

Q4 = "SELECT fname,lname FROM Cast inner join Actor on id=pid where mid=27;"

Q5 = "SELECT COUNT(*) FROM Cast inner join Actor on id=pid WHERE fname = 'Jon' and lname = 'Dough';"

Q6 = "SELECT name FROM Movie where (year between 2003 and 2006) and name like 'Young Latin Girls%';"

Q7 = "SELECT fname, lname FROM moviedirector inner join director on did = director.id inner join movie on movie.id = mid where name like 'Star Trek%'"

Q8 = "SELECT name from cast join actor on actor.id=pid join movie on movie.id = mid inner join director WHERE (actor.fname = 'Jackie (I)' and director.fname = 'Jackie (I)') and (actor.lname = 'Chan' and director.lname = 'Chan') order by name ASC;"

Q9 = "SELECT fname,lname FROM Director INNER JOIN MovieDIRECTOR ON `Director`.`id`=did INNER JOIN Movie ON `Movie`.`id`=mid WHERE year = 2001 GROUP BY did HAVING COUNT(mid)>=4 ORDER BY fname ASC,lname DESC;"

Q10 = "SELECT gender,COUNT(gender) FROM Actor where gender = 'F' UNION SELECT gender,COUNT(gender) FROM Actor where gender = 'M';"




SELECT id,name,age,
(age - (SELECT AVG(age) FROM Student) AS variance)/variance AS variance_percentage,  
FROM Student;


SELECT s.id,s.name,s.age FROM Student AS s WHERE EXIST (SELECT e.student_id FROM Enrollment e WHERE s.id = student_id AND e.course_id = 1)


SELECT id, name, age 
FROM Student
WHERE NOT EXISTS (
    SELECT student_id 
    FROM Enrollment
    WHERE id=student_id AND course_id >= 1 AND year = 2015
);

SELECT id,name,credits
FROM Course
WHERE NOT EXISTS (
    SELECT course_id FROM Enrollment
    WHERE id != course_id);
    
    
    
    
SELECT MAX(avg_score) as max_avg_score
FROM (
-- Here we make our sub-query:
    SELECT student_id,
    AVG(score) AS avg_score
    FROM Enrollment
    GROUP BY course_id
-- End of the sub-query
) AS enroll;

SELECT SUM(avg_score) as max_avg_score
FROM (
    SELECT student_id,
    AVG(score) AS avg_score
    FROM Enrollment
    GROUP BY student_id
) AS enroll;
    
    
SELECT id,name,credits FROM Course WHERE NOT EXISTS(SELECT course_id FROM Enrollment WHERE `Course`.`id`== course_id); 
    
    
SELECT * FROM Director WHERE EXISTS (SELECT did FROM MovieDIrector INNER JOIN Movie  ON id = mid WHERE year >2000) LIMIT 20;

SELECT id,fname FROM Director WHERE NOT EXISTS (SELECT did FROM MovieDIrector INNER JOIN Movie  ON id = mid WHERE year < 2000 and did = director.id) order by director.id ASC LIMIT 20;


SELECT id,fname
FROM Director
WHERE EXISTS(
    SELECT did FROM MovieDIrector 
    INNER JOIN Movie  ON id = mid 
    WHERE year >2000) 
    AND NOT EXISTS (
        SELECT did FROM MovieDIrector 
        INNER JOIN Movie  ON id = mid 
        WHERE year < 2000 AND did = director.id) 
        order by director.id ASC;
        
 INNER JOIN Director ON MovieDirector `Movie`.`id` = did       
 INNER JOIN Director as d ON di.id = md.did and di.id = d.id
 
SELECT di.fname,(
    SELECT m.name FROM Movie AS m 
    INNER JOIN MovieDirector AS md ON md.mid = m.id 
    WHERE md.did = di.id 
    ORDER BY m.rank DESC, m.name ASC LIMIT 1) 
    FROM Director AS di limit 100;

SELECT di.fname,(
    SELECT m.name FROM Movie AS m 
    INNER JOIN MovieDirector AS md ON md.mid = m.id 
    WHERE md.did = di.id) 
    FROM Director AS di limit 100;
    
    

SELECT SUM(avg_score) AS sum_avg_score
FROM(
SELECT AVG(score) AS avg_score FROM Enrollment GROUP BY course_id HAVING avg_score > 60);

SELECT MIN(avg_score) AS sum_avg_score
FROM(
SELECT AVG(score) AS avg_score FROM Enrollment GROUP BY course_id HAVING avg_score < 60);

SELECT student_averages.student_id, student_averages.student_avg_score, course_averages.course_id, course_averages.course_avg_score 
FROM (
    SELECT student_id, AVG(score) AS student_avg_score 
    FROM Enrollment 
    GROUP BY student_id
) AS student_averages JOIN (
    SELECT course_id, AVG(score) AS course_avg_score 
    FROM Enrollment 
    GROUP BY course_id
) AS course_averages
WHERE student_averages.student_avg_score > course_averages.course_avg_score;

SELECT student_details.student_id,student_details.no_of_course,course_details.course_id,course_details.no_of_student
FROM(
SELECT student_id, COUNT(course_id) AS no_of_course 
    FROM Enrollment 
    GROUP BY student_id)
    AS student_details JOIN (
SELECT course_id,COUNT(student_id) AS no_of_student
FROM Enrollment
GROUP BY course_id)
AS course_details
WHERE no_of_course > 3;

SELECT student_id, AVG(score) as avg_score
FROM Enrollment 
GROUP BY student_id 
HAVING AVG(score)>(SELECT AVG(score)
                   FROM Enrollment);
                   
SELECT student_id, AVG(score) as avg_score
FROM Enrollment 
GROUP BY student_id 
HAVING AVG(score) < (SELECT AVG(score)
FROM Enrollment WHERE year = 2015);


SELECT COUNT(player_of_match) FROM Match
INNER JOIN MatchCaptain ON MatchCaptain.match_no = Match.match_no
INNER JOIN MatchCaptain ON MatchCaptain.captain = Player.player_id
INNER JOIN Match ON Player.player_id = Match.player_of_match;
  
  
SELECT COUNT(player_id) FROM Player
INNER JOIN MatchCaptain ON MatchCaptain.captain = Player.player_id
INNER JOIN Match ON Player.player_id = Match.player_of_match;


"""
# Q5 = """SELECT COUNT(player_id) AS no_players FROM Player 
# INNER JOIN Match ON Player.player_id = Match.player_of_match AND Player.player_id = MatchCaptain.captain
# INNER JOIN MatchCaptain ON MatchCaptain.match_no = Match.match_no;"""

Q5 = """SELECT COUNT(player_id) FROM Player
INNER JOIN MatchCaptain ON MatchCaptain.captain = Player.player_id AND MatchCaptain.match_no = Match.match_no
INNER JOIN Match ON Player.player_id = Match.player_of_match;
SELECT COUNT(DISTINCT player_id) FROM Player                                                                             
INNER JOIN MatchCaptain ON MatchCaptain.captain = Player.player_id AND MatchCaptain.match_no = Match.match_no
INNER JOIN Match ON Player.player_id = Match.player_of_match;
"""

SELECT DISTINCT(captain) FROM MatchCaptain
WHERE NOT EXISTS(SELECT player_id FROM Player INNER JOIN MatchCaptain ON Player.player_id = MatchCaptain.captain
INNER JOIN MatchCaptain ON MatchCaptain.match_no = Match.match_no
INNER JOIN Match ON Match.player_of_match = Player.player_id);
#INNER JOIN Player ON Player.player_id = MatchCaptain.captain


Q6 = """SELECT DISTINCT MatchCaptain.captain 
FROM MatchCaptain 
WHERE NOT EXISTS(SELECT player_id FROM Player INNER JOIN Match ON Player.player_id = Match.player_of_match
INNER JOIN MatchCaptain ON MatchCaptain.match_no = Match.match_no);
"""
#WHERE EXISTS(SELECT player_id FROM Player INNER JOIN MatchCaptain ON Player.player_id = MatchCaptain.captain)AND 
Q6 = """SELECT DISTINCT MatchCaptain.captain 
FROM MatchCaptain 
WHERE EXISTS(SELECT player_id FROM Player INNER JOIN MatchCaptain ON Player.player_id = MatchCaptain.captain)
AND WHERE NOT EXISTS(SELECT player_id FROM Player INNER JOIN Match ON Player.player_id = Match.player_of_match
INNER JOIN MatchCaptain ON MatchCaptain.match_no = Match.match_no);
"""
"""
n=int(input())
fib=[0,1]
f1=0
f2=1
for i in range(n):
    f3=f1+f2
    
    f1=f2
    f2=f3
    fib.append(f3)

print(fib[

include <stdio.h>
int main() {
    int n, reversedN = 0, remainder, originalN;
    scanf("%d", &n);
    m= n;
    while (n != 0) {
        remainder = n % 10;
        reversedN = reversedN * 10 + remainder;
        n /= 10;
    }

      if (originalN == reversedN)
        printf("%d is a palindrome.", originalN);
    else
        printf("%d is not a palindrome.", originalN);
    return 0;
}


select a.id,a.fname,count(distinct(md.did) from actor a inner join cast c on a.id=  =c.pid
inner join  moviedirector md on md.mid = c.mid group by a.id;

word = "qwesd werd qsdfrd ijuhg okmiq"
z = word.split()

for w in z:
if w[0]=='q' and w[-1]= d"
print(w)

select c.date,count(c.name) from country c where c.date = 12 group by c.date having c.death > 5000