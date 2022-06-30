#Searching
import pymysql
try:
    conn=pymysql.connect(host="localhost",user="root",password="",
                                        db="bank_db")
except Exception as e:
    print(e)

else:
    print("Connection created successfully")
#creating cursor
cur=conn.cursor()
id=int(input("Enter Id No to be Searcherd :"))
query="select * from btable where id=%s"
try:
    cur.execute(query,id)
except Exception as e:
    print("Query Error")
else:
    result=cur.fecthall()
    for row in result:
        for col in row:
            print(col)
        print()
finally:
    conn.close()

