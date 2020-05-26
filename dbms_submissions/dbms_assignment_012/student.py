class DoesNotExist(Exception):
	pass

class MultipleObjectsReturned(Exception):
	pass

class InvalidField(Exception):
	pass

def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit()
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans
 
	

class Student:
	def __init__(self, name, age, score):
		self.name = name
		self.student_id = None
		self.age = age
		self.score = score
    	   
	def save(self):
		if self.student_id == None:
			query="insert into student(name,age,score) values ('{}',{},{})".format(self.name,self.age,self.score)
			write_data(query)
			q1='select student_id from student where name="{}" and age={} and score={}'.format(self.name,self.age,self.score)
			a=read_data(q1)   
			self.student_id=a[0][0]
		else:
			sql_query="update student set name='{}',age={},score={} where student_id={}".format(self.name,self.age,self.score,self.b)
			write_data(sql_query)
			read_data(sql_query)
			
		w = "SELECT * FROM Student WHERE student_id = {}".format(self.student_id)
		obj = read_data(w)
		
		if len(obj)==0:
		    query = "insert into student(student_id,name,age,score) values ({},'{}',{},{})".format(self.student_id,self.name,self.age,self.score)
		    write_data(query)
		    
	def delete(self):
		sql_query='delete from student where student_id={}'.format(self.student_id)
		write_data(sql_query)
    
	
	@classmethod
	def get(cls,**kid):
		for x,y in kid.items():
			cls.a=x
			cls.b=y
			if str(x) not in ('name','age','score','student_id'):
				raise InvalidField 
           
			query="select * from student where {} = '{}'".format(cls.a,cls.b)
        
		obj=read_data(query)
		if len(obj)>1:
			raise MultipleObjectsReturned
		elif len(obj)==0:
			raise DoesNotExist
		elif len(obj)==1:
			c=Student(obj[0][1],obj[0][2],obj[0][3])
			c.student_id=obj[0][0]
			return c	

#stud = Student.get(student_id = 1)
#print(stud)

"""class DoesNotExist(Exception):
     pass

class MultipleObjectsReturned(Exception):
     pass

class Student:
    def __init__(self,name=None,age=None,score=None):
        self.name=name
        self.age=age
        self.student_id=None
        self.score=score

    @classmethod
    def get(cls,student_id=None,name=None,age=None,score=None):
        import sqlite3
        conn=sqlite3.connect("students.sqlite3")
        crsr=conn.cursor()
        if(age!=None):
            sql_query="Select * from student where age={}".format(age)
        if(student_id!=None):
            sql_query="Select * from student where student_id={}".format(student_id)
        if(score!=None):
            sql_query="Select * from student where score={}".format(score)
        if(name!=None):
            sql_query="Select * from student where name='{}'".format(name)
        crsr.execute(sql_query) 
        ans=crsr.fetchall()
        if(len(ans)==0):
            raise DoesNotExist
        elif(len(ans)>1):
            raise MultipleObjectsReturned
        obj=cls(ans[0][1],ans[0][2],ans[0][3])
        obj.student_id=ans[0][0]
        conn.close()
        return obj

    def delete(self):
        import sqlite3
        conn=sqlite3.connect("students.sqlite3")
        crsr=conn.cursor()
        crsr.execute("PRAGMA foreign_keys=on;") 
        sql_query="DELETE FROM student where student_id={}".format(self.student_id)
        crsr.execute(sql_query)
        conn.commit()
        conn.close()

    def save(self):
        import sqlite3
        conn=sqlite3.connect("students.sqlite3")
        crsr=conn.cursor()
        crsr.execute("PRAGMA foreign_keys=on;")
        if(self.student_id==None):
            sql_query="insert into student(student_id,name,age,score) values(null,'{}',{},{})".format(self.name,self.age,self.score)
            crsr.execute(sql_query)
            self.student_id=crsr.lastrowid
        else:
        	sql_query="Update student set name='{}',age={},score={} where student_id={}".format(self.name,self.age,self.score,self.student_id)
        	crsr.execute(sql_query)
        conn.commit()
        conn.close()
"""


