import sqlite3 as sq

# cars = [
#     ('BMV', 54000),
#     ('Chevrolet', 56000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]

# with sq.connect('cars.db') as con:
#     cur = con.cursor()
#     cur.execute('''
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#
#     )
#     ''')

# cur.execute("INSERT INTO cars VALUES(1, 'Renault', 20000)")
# cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
# cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
# cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
# cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")

# for car in cars:
#     cur.execute('INSERT INTO cars VALUES(null, ?, ?)', car)

# cur.executemany('INSERT INTO cars VALUES(null, ?, ?)', cars)

# cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

# cur.executescript('''
# DELETE FROM cars WHERE model LIKE 'B%';
# UPDATE cars SET price = price + 100;
# ''')

# com.commit()
# con.close()

# con = None
# try:
#     con = sq.connect('cars.db')
#     cur = con.cursor()
#     cur.executescript('''
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 20000);
#     UPDATE cars SET price = price + 100;
#     ''')
#     con.commit()
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print(f'Ошибка выполнения запроса {e}')
# finally:
#     if con:
#
#         con.close()


# with sq.connect('cars.db') as con:
#     con.row_factory  = sq.Row
#     cur = con.cursor()
#     cur.execute('''
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#
#     )
#     ''')
#
#     cur.execute('SELECT model, price FROM cars')
#     # rows = cur.fetchall()
#     # rows = cur.fetchone()
#     # rows = cur.fetchmany(5)
#     # print(rows)
#     # for res in cur:
#     #     print(res)
#
#     for res in cur:
#         print(res['model'], res['price'])

# def read_ava(n):
#     try:
#         with open(f'avatars/{n}.png', 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# with sq.connect('cars.db') as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#
#     cur.executescript('''
#     CREATE TABLE IF NOT EXISTS users(
#         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         ava BLOB
#     )
#     ''')
#     img = read_ava(1)
#     if img:
#         binary = sq.Binary(img)
#         cur.execute('INSERT INTO users VALUES (?, ?)', (1, binary))

# with sq.connect('cars.db') as con:
#     cur = con.cursor()
#
#     with open('sql_dump.sql', 'w') as f:
#         for sql in con.iterdump():
#             f.write(sql)


with sq.connect('cars.db') as con:
    cur = con.cursor()

    with open('sql_dump.sql', 'r') as f:
        sql = f.read()
        cur.executescript(sql)
