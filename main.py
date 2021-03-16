from flask import Flask, redirect, url_for, jsonify # import biblioteki flask, redirect, url_for
app = Flask(__name__)
import mysql.connector
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="baza2"
)

@app.route('/addPupil/<name>/<surname>/<pesel>/<class_name>')
def add_pupil(name, surname, pesel, class_name):
    mycursor = mydb.cursor()
    rand_id = random.randint(0, 1000)
    # new_pupil_query_values = "INSERT INTO pupil (pupil_id, name, surname, pesel, class) VALUES (" + str(rand_id) + ",'" + name + "','" + surname + "'," + str(pesel) + ",'" + class_name + "');"
    new_pupil_query = "INSERT INTO pupil (pupil_id, name, surname, pesel, class) VALUES (%s, %s, %s, %s, %s)"
    new_pupil_query_values = (rand_id, name, surname, pesel, class_name)
    mycursor.execute(new_pupil_query, new_pupil_query_values)   
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return jsonify( # zwrócenie jsona (pamiętaj o imporcie tej bibliteki)
        info="User " + name + " " + surname + " added successfully",
        responseCode=200
    )

@app.route('/addTeacher/<name>/<surname>/<pesel>/<subject>')
def addTeacher(name, surname, pesel, subject):
    mycursor = mydb.cursor()
    rand_id = random.randint(0, 1000)
    # new_pupil_query_values = "INSERT INTO pupil (pupil_id, name, surname, pesel, class) VALUES (" + str(rand_id) + ",'" + name + "','" + surname + "'," + str(pesel) + ",'" + subject + "');"
    new_teacher_query = "INSERT INTO Teacher (pupil_id, name, surname, pesel, subject) VALUES (%s, %s, %s, %s, %s)"
    new_teacher_query_values = (rand_id, name, surname, pesel, subject)
    mycursor.execute(new_teacher_query, new_teacher_query_values)   
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return jsonify( # zwrócenie jsona (pamiętaj o imporcie tej bibliteki)
        info="Teacher " + name + " " + surname + " added successfully",
        responseCode=200
    )

@app.route('/showAllPupils')
def showAllPupils():
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM PUPIL'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    return jsonify(
        info='Pupils showed',
        responseCode=200
    )


if __name__ == "__main__":
    app.run("localhost", 3000, True, {}) # odpalenie serwera (host, port, debug, options)