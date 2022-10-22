import pymysql

e_id = "3"
e_name = "5"
sex = "5"
addr = "5"

conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='python', charset='utf8')

curs = conn.cursor()
#"""세게는 여러개의 스트링이 가능하게 해주는 것(멀티라인)
sql = f"""
    update emp 
    set
        e_name = '{e_name}',
        sex ='{sex}',
        addr = '{addr}'
    where
        e_id='{e_id}'         
 """

cnt = curs.execute(sql)
print("cnt",cnt)
#print("cnt",cur s.rowcount)
conn.commit()
curs.close()
conn.close()