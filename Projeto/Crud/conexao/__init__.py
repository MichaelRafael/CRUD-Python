import mysql.connector


connection = mysql.connector.connect(host='localhost', user='root', password='', database='revisando')
cursor = connection.cursor(dictionary=True)
