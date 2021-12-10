import mysql.connector
from hashlib import md5
from time import time
import string
import random
import time
from datetime import datetime



conn = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', port=3306, database='mydatabase', auth_plugin='mysql_native_password')

cursor = conn.cursor()

sql ='''CREATE TABLE IF NOT EXISTS PRODUCT_TYPE(
   PRODUCT_ID INT,
   PRODUCT_NAME CHAR(20),
   BARCODE CHAR(10),
   DATE_TIME DATETIME,
   QUANTITY INT,
   TEMPERATURE INT
)'''
cursor.execute(sql)

count=0
PRODUCT_ID=[]
PRODUCT_NAME=[]
BARCODE=[]
DATE_TIME=[]
QUANTITY=[]
TEMPERATURE=[]
param_list=[]
for i in range(0,50000):
    PRODUCT_ID.append(str(random.randint(1,50)))
    TEMPERATURE.append(str(random.randint(1,100)))
    QUANTITY.append(str(random.randint(1,100)))

def randomDate(start, end):
    frmt = '%d-%m-%Y %H:%M:%S'

    stime = time.mktime(time.strptime(start, frmt))
    etime = time.mktime(time.strptime(end, frmt))

    ptime = stime + random.random() * (etime - stime)
    dt = datetime.fromtimestamp(time.mktime(time.localtime(ptime)))
    return str(dt)
for i in range(0,50000):
    N=6
    DATE_TIME.append(randomDate("20-01-2018 13:30:00", "23-01-2021 04:50:34"))
    PRODUCT_NAME.append(''.join(random.choices(string.ascii_uppercase+string.digits, k=N)))
    BARCODE.append(''.join(random.choices(string.ascii_uppercase+string.digits, k=N)))
    count+=1
    param_list.append(' '.join(PRODUCT_ID+PRODUCT_NAME+BARCODE+DATE_TIME+QUANTITY+TEMPERATURE))
    
sql = "INSERT INTO PRODUCT_TYPE(PRODUCT_ID, PRODUCT_NAME, BARCODE, DATE_TIME, QUANTITY, TEMPERATURE) VALUES(%s,%s,%s,%s,%s,%s)"
cnt=0
for param in param_list:
    values = (PRODUCT_ID[cnt],PRODUCT_NAME[cnt],BARCODE[cnt],DATE_TIME[cnt],QUANTITY[cnt],TEMPERATURE[cnt] )
    cursor.execute(sql, values)
    cnt+=1
conn.commit()

conn.close()
