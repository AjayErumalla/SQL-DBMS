class Student:
    def __init__(self,name, age, score):
        self.student_id = None
        self.name = name
        self.age = age
        self.score = score
        
    
        import sqlite3
        conn = sqlite3.connect('studentdb.sqlite3')
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys=on;")
    #c.execute('''CREATE TABLE student_details(student_id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(200),age INT,score INT)''')
    #c.execute("INSERT INTO student_details(name,age,score) VALUES ('Naveen',33,93),('Jan',31,90)")
        conn.commit()
        
        def get(self):
            c.execute('SELECT * FROM student_details')
            data = c.fetchall()
            print(data)
            
        c.close()
        conn.close()

# def get():
#     c.execute('SELECT * FROM student_details')
#     data = c.fetchall()
#     print(data)
    
#student_1 = Student.get(student_id = 1)   
    
#get()
 