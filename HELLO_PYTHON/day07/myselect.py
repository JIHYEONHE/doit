import pymysql
 
# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='python', charset='utf8')
 
# Connection 으로부터 Cursor 생성
curs = conn.cursor()
 
# SQL문 실행
sql = "select * from emp"
curs.execute(sql) #커서는 자바로 치면 statement와 같음
 
# 데이타 Fetch
rows = curs.fetchall()
print(rows)     # 전체 rows

#커서 닫기
curs.close() 
# Connection 닫기
conn.close()
