
import requests
from django.shortcuts import render
from django.http import HttpResponse
import pymongo
import json
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Thanku@123",
  database="empdb"
)

# Create your views here.
def index(requests):

    return render(requests,"student_app/form.html",{})
def details(requests):

    firstname = requests.GET["fname"]
    lastname = requests.GET["lname"]
    sex1 = requests.GET["membership"]
    date = requests.GET["birthday"]

        # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        # mydb = myclient["testdatabase"]
        # mycol = mydb["testcollection"]
        # mydict = {"firstname": firstname, "lastname": lastname,"sex":sex1,"Date_of_birth":date}
        # x = mycol.insert_one(mydict)
    mycursor = mydb.cursor()

    sql = "INSERT INTO emp_details(firstname,lastname,sex1,date)VALUES(%s,%s,%s,%s)"
    val = (firstname,lastname,sex1,date)

    mycursor.execute(sql, val)

    mydb.commit()

    text="details saved"
    return render(requests,"student_app/msg.html",{'text':text})

def display(requests):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanku@123",
        database="empdb"
    )
    mycursor=mydb.cursor()


    mycursor.execute("SELECT * FROM  emp_details")

    myresult = mycursor.fetchall()



    list = []
    for x in myresult:
       print(x)
       list.append(x)

    print()



    #
    #
    # stud = []
    #
    # tbl = "<tr><td>firstname</td><td>lastname</td><td>sex</td><td>date_of_birth</td></tr>"
    # stud.append(tbl)
    #
    # for y in mycol.find():
    #     a = "<tr><td>%s</td>" %y["firstname"]
    #     stud.append(a)
    #     b = "<td>%s</td>" % y["lastname"]
    #     stud.append(b)
    #     c = "<td>%s</td></tr>" % y["sex"]
    #     stud.append(c)
    #     d = "<td>%s</td></tr>" % y["Date_of_birth"]
    #     stud.append(d)

    text = "DB displayed"
    return render(requests, "student_app/display.html",{'text1':list})

    # with open('student_app/test.txt', 'w') as f:
        # for data in y:
        #     # list.append(data)
        #     f.write(json.dumps(data))
        #     f.write('\n')
def search(requests):

    mycursor=mydb.cursor()
    sql="SELECT * FROM emp_details WHERE firstname=%s"
    firstname = requests.GET["fname1"]

    mycursor.execute(sql,(firstname,))
    myresult=mycursor.fetchall()
    list1=[]
    for x in myresult:
        print(x)
        list1.append(x)
        print(list1)

    # firstname1 = requests.GET["fname1"]
    # cursor = mycol.find({"firstname": "kaviya"})
    # # iterate code goes here
    # for doc in cursor:
    #     print(doc)

   # mydoc=mycol.find()
    # print(mydoc)

    # list(map(print, mydoc))

    #
    # print("hallo")
    # for x in mudoc:
    #     print(x["firstname"])



    text="search"
    return render(requests, "student_app/display.html", {'text1':list1})


def delete(requests):


    mycursor = mydb.cursor()
    sql = "DELETE FROM emp_details WHERE firstname=%s"
    firstname = requests.GET["fname2"]

    mycursor.execute(sql,(firstname,))
    mydb.commit()


    print(mycursor.rowcount, "record(s) deleted")

    msg="name Deleted"
    return render(requests, "student_app/display.html", {'text1': msg})


def update(requests):

    mycursor=mydb.cursor()
    oldname = requests.GET["fname3"]
    newname = requests.GET["fname4"]


    sql="UPDATE emp_details SET firstname=%s WHERE firstname=%s"
    value=(newname,oldname)
    # UPDATE Customers SET
    # PostalCode = 00000
    # WHERE
    # Country = 'Mexico';
    mycursor.execute(sql,value)
    mydb.commit()

    print(mycursor.rowcount, "record(s) updated")






    # print "customers" after the update:


    # mycol.update_one(myquery,new_query)
    msg = "Firstname changed"
    return render(requests, "student_app/update_msg.html", {'text1': msg})

    # mycol.update_one(myquery, newvalues)

    # myquery = {"firstname":old_firstname}













