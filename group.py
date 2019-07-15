import pymysql
import db

class Group(object):
    def __init__(self, title, title_id, url, author, author_id, response_cnt, updated_time):
        self.title = title
        self.title_id = title_id
        self.url = url
        self.author = author
        self.author_id = author_id
        self.response_cnt = response_cnt
        self.updated_time = updated_time

    def insert(self):
        con = db.Connect()
        cur = con.cursor()
        try:
            sql_str = ("INSERT INTO douban (title, title_id, url, author, author_id, response_cnt, updated_time) "+ " VALUES('%s', '%s','%s', '%s','%s', '%s','%s')" % (self.title,self.title_id,self.url,self.author,self.author_id,self.response_cnt,self.updated_time))
            cur.execute(sql_str)
            con.commit()
        except:
            con.rollback()
            logging.exception('Insert operation error')
            raise
        finally:
            cur.close()
            con.close()

    def get():
        


