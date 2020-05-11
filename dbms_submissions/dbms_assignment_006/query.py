Q1 = "SELECT fname,lname FROM Actor INNER JOIN Cast ON id = pid WHERE mid = 12148;"

Q2 = "SELECT COUNT(pid) FROM Actor INNER JOIN Cast ON id = pid WHERE fname = 'Harrison (I)' AND lname = 'Ford';"

Q3 = "SELECT DISTINCT pid FROM Cast INNER JOIN Movie ON id = mid WHERE name LIKE 'Young Latin Girls%';"

Q4 = "SELECT COUNT(DISTINCT pid) FROM Cast INNER JOIN Movie ON id == mid WHERE year BETWEEN 1990 AND 2000;"  






# FROM ((Orders
# INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
# INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID); 