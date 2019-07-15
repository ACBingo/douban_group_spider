import pymysql

def Connect():
    return pymysql.connect(host='localhost',
    port=3306,
    user='root',
    database='douban',
    charset='utf8mb4'
    )

def query():
    sql_str = "SELECT * from douban"
    con = Connect()
    cur = con.cursor()
    cur.execute(sql_str)
    rows = cur.fetchall()
    cur.close()
    con.close()

    print(rows)

if __name__ == "__main__":
    query()