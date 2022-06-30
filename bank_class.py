import pymysql
class btable:
    def __init__(self):
        try:
            self.__conn=pymysql.connect(host="localhost",user="root",password="",
                                        db="bank_db")
        except Exception as e:
            print(e)

        else:
            print("Connection created successfully")
    def __del__(self):
        pass
#creating object
b1=btable()
del b1
