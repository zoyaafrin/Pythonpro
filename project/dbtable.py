import pymysql
con=pymysql.connect(user='root',password='root',port=3306,database='pythonmysql')
cursor= con.cursor()
def create_table():
    try:
        query='''
        create table customer(
        id int primary key,
        name varchar (100),
        mobile bigint unique,
        balance bigint
        );
        '''
        cursor.execute(query)
    except pymysql.err.OperationalError as e:
        print(f'{e}')
def insert_record():
    query='insert into customer(id,name,mobile,balance)values(1,"afrin",9876543210,3000)'
    cursor.execute(query)
    con.commit()
# insert_record() 
def get_records():      
    query='select*from customer'
    cursor.execute(query)
    records=cursor.fetchall()
    print(records)
# get_records()   
def insert_dynamic(cid,name,mobile,bal):
    record=(cid,name,mobile,bal)
    query="insert into customer(id,name,mobile,balance)values(%s,%s,%s,%s)"
    cursor.execute(query,record)
    con.commit()