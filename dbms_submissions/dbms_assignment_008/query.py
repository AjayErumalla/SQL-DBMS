Q1 = """SELECT id,fname
FROM Director
WHERE EXISTS(
    SELECT did FROM MovieDIrector 
    INNER JOIN Movie  ON id = mid 
    WHERE Movie.year >2000 AND did = Director.id) 
    AND NOT EXISTS (
        SELECT did FROM MovieDirector 
        INNER JOIN Movie  ON id = mid 
        WHERE Movie.year < 2000 AND did = Director.id) 
        ORDER BY Director.id ASC;"""
        
Q2 = """SELECT di.fname,(
    SELECT m.name FROM Movie AS m 
    INNER JOIN MovieDirector AS md ON md.mid = m.id 
    WHERE md.did = di.id 
    ORDER BY m.rank DESC, m.name ASC LIMIT 1) 
    FROM Director AS di limit 100;"""
    
Q3  = """SELECT *
FROM Actor
WHERE NOT EXISTS (
    SELECT pid FROM Cast 
    INNER JOIN Movie ON Movie.id = mid
    WHERE pid == Actor.id AND year BETWEEN 1990 AND 2000)
    ORDER BY Actor.id DESC LIMIT 100;"""