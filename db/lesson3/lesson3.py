import sqlite3 as sq

with sq.connect('db_3.db') as con:
    cur = con.cursor()

    cur.execute('''
    SELECT * 
    FROM T1
    ORDER BY FName
    LIMIT 2, 5
    ''')
    # res = cur.fetchall()
    # print(res)
    # for res in cur:
    #     print(res)
    res = cur.fetchone()
    res2 = cur.fetchmany(2)
    print(res)
    print(res2)