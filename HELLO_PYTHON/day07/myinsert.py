import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='python', charset='utf8')

curs = conn.cursor()
#"""세게는 여러개의 스트링이 가능하게 해주는 것(멀티라인)
sql = """insert into emp(e_id,e_name,sex,addr)
         values (%s, %s, %s, %s)"""

cnt = curs.execute(sql, ('3', '3', '3','3'))
print("cnt",cnt)
#print("cnt",cur s.rowcount)
conn.commit()
curs.close()
conn.close()