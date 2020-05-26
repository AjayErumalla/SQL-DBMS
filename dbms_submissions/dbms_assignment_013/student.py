class DoesNotExist(Exception):
	pass

class MultipleObjectsReturned(Exception):
	pass

class InvalidField(Exception):
	pass

def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit()
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
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
			
	@classmethod
	def filter(cls,**kid):
		cls.li=[]
		cls.operator={'lt':'<','lte':'<=','gt':'>','gte':'>=','neq':'!=','in':'in','contain':''}
		if(len(kid))>=1:
			l=[]
			for x,y in kid.items():
				cls.a=x
				cls.b=y
				field=cls.a
				field=field.split('__')
				if field[0] not in ('name','age','score','student_id'):
					raise InvalidField 
				if(len(field))==1:
					query=" {}='{}'".format(cls.a,cls.b)
				elif field[1]=='contains':
					query=" {} like '%{}%'".format(field[0],cls.b)
				elif field[1]=='in':
					query=" {} {} {}".format(field[0],cls.operator[field[1]],tuple(cls.b))
				else:
					query="{} {} '{}'".format(field[0],cls.operator[field[1]],cls.b)
				l.append(query)
				
			x = " and ".join(tuple(l)) 
			query= "select * from student where "+x
			objj=read_data(query)
			for i in range(len(objj)):
				c=Student(objj[i][1],objj[i][2],objj[i][3])
				c.student_id=objj[i][0]
				cls.li.append(c)
			return cls.li    
			
			
"""
	@classmethod
	def filter(cls,**key):
		objects = []
		
		for key,value in key.items():
			cls.c = key
			cls.d = value
		
		e = key.split("__")
		
		if e[0] not in ('name','age','score','student_id'):
			raise InvalidField()
			
		if len(e)==1:
		    query="select * from student where {} = '{}'".format(e[0],cls.d)
		    obj = read_data(query)
		    
		elif (e[1] == 'lt'):
		    query="select * from student where {} < '{}'".format(e[0],cls.d)
		    obj = read_data(query)
		    
		elif (e[1] == 'lte'):
		    query="select * from student where {} <= '{}'".format(e[0],cls.d)
		    obj = read_data(query)
		   
		elif (e[1] == 'gt'):
		    query="select * from student where {} > '{}'".format(e[0],cls.d)
		    obj = read_data(query)
		    
		elif (e[1] == 'gte'):
		    query="select * from student where {} >= {}".format(e[0],cls.d)
		    obj = read_data(query)
		
		elif(e[1] == 'neq'):
		    query="select * from student where {}!='{}'".format(e[0],cls.d)
		    obj = read_data(query)
		    
		elif(e[1] == 'in'):
		    query="select * from student where {} in {}".format(e[0],tuple(cls.d))
		    obj = read_data(query)
		    
		elif(e[1] == "contains"):
		    query="select * from student where {} like '%{}%'".format(e[0],cls.d)
		    obj = read_data(query)
		    
		for i in range(len(obj)):
			obj1 = Student(obj[i][1],obj[i][2],obj[i][3])
			obj1.student_id = obj[i][0]
			objects.append(obj1)
			
		return objects"""

    
		
		
		 
		
