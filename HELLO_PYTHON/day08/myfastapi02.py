from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='python', charset='utf8')
 
# Connection 으로부터 Cursor 생성
#DictCursor / 연관배열/ 딕셔너리
curs = conn.cursor(pymysql.cursors.DictCursor)
 
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


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/hello", response_class=HTMLResponse)
async def root(request: Request):
    str = "패스트API겁나짜증나"
    arr = ["홍길동","전우치","이순신"]
    emps = [
        {'e_id':'1','e_name':'1','sex':'1','addr':'1'},
        {'e_id':'2','e_name':'2','sex':'2','addr':'2'},
        {'e_id':'3','e_name':'3','sex':'3','addr':'3'}
        ]

    return templates.TemplateResponse("index.html", {"request": request, "str": str,"arr":arr , "emps":emps , "rows":rows})



#uvicorn myfastapi02:app --reload