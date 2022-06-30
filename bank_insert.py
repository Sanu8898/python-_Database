#Inserting

import pymysql
try:
    conn=pymysql.connect(host="localhost",user="root",password="",
                                        db="bank_db")
except Exception as e:
    print(e)

else:
    print("Connection created successfully")

id=int(input("Enter Id No :"))
name=input("Enter Name of Customer:")
deposit=int(input("Enter Deposit Amount :"))
ac=input("Enter Account type :")
query="INSERT into btable  values(%s,%s,%s,%s)"
val=(id,name,deposit,ac)
cur=conn.cursor()
try:
    cur.execute(query,val)
except Exception as e:
    print("Querry Error")
else:
    print("Record inserted")
    conn.commit()
    conn.close()
