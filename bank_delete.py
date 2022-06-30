#Delete Record :
#To delete particular record of student according to enrollment no.
import pymysql
#first create a connection string between mysql with python
#use library pymysql
try:
    conn=pymysql.connect(host='localhost',user='root',password='',
                db='bank_db')
#conn user defined object of connect
except Exception as e:
    print(e)
else:
    print("Connection Create Successfully")

#create cursor :
#create cursor for run the SQL query
cur=conn.cursor()
#cur user defined object of cursor
en=int(input("Enter ID No. to be deleted : "))
try:
    query="delete from btable where id=%s"
except Exception as e:
    print("Query Error")
else:
    cur.execute(query,en)
    print(cur.rowcount," Delete Record successfully")
    conn.commit() #to save changes permanently
finally:
    conn.close()
