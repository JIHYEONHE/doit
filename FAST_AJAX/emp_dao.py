import pymysql
class EmpDao:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='python', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

        
    def selects(self):
        sql = "select e_id,e_name,sex,addr from emp"
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        return rows
    
    def select(self, e_id):
        sql = f"""
            select 
                e_id,
                e_name,
                sex,
                addr 
            from 
                emp 
            where 
                e_id='{e_id}'
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        return rows[0]
    
    def insert(self, e_id, e_name, sex, addr):
        sql = f"""insert into emp
            (e_id,e_name,sex,addr)
            values
            ('{e_id}','{e_name}','{sex}','{addr}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit() # commit을 꼭해줘야한다 insert시에
        return cnt
    
    def update(self, e_id,e_name,sex,addr):
        sql = f"""
            update emp
            set e_name='{e_name}',
                sex='{sex}',
                addr='{addr}'
            where
                e_id= '{e_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self, e_id):
        sql = f"""
            delete
            from emp
                
            where
                e_id= '{e_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    
    def __del__(self):
        self.curs.close()
        self.conn.close()

if __name__ == '__main__':
    ed = EmpDao()
    # cnt = ed.update('3','4','4','4')
    # print(cnt)
    cnt = ed.delete('3')
    print(cnt)
    
    
    
    
    
    