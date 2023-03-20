import sqlite3
import os
import time
import math


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = 'SELECT * FROM mainmenu'
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Ошибка чтения из базы данных')
        return []

    def get_post(self, post_id):
        sql = f'SELECT c.category_title, p.id, p.title, p.short_text, p.text, p.time, a.author_name FROM posts as p, category as c,' \
              f' author as a WHERE  a.id == p.author AND c.id = p.category AND p.id={post_id}'
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchone()
            if res:
                return res
        except IOError:
            print('Ошибка чтения из базы данных')
        return []

    def get_all_posts(self):
        sql = f'SELECT * FROM posts as p, category as c, author as a WHERE  a.id == p.author AND c.id = p.category'
        try:
            
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res

        except IOError:
            print('Ошибка чтения из базы данных')
        return []
    
    def add_author(self, name):
        try:
            sql = f'SELECT * FROM author WHERE author_name=="{name}"'
            self.__cur.execute(sql)
            res = self.__cur.fetchone()
            if res:
                print(res)
                print('false')
                return True
            else:
                self.__cur.execute('INSERT INTO author VALUES(NULL, ?)', (f'{name}',))
                self.__db.commit()
                print('true')
        except sqlite3.Error as e:
            print('Ошибка добавления статьи в базу данных:' + str(e))
            return False
        return True

    def get_my_post(self, username):
        sql = f'SELECT c.category_title, p.id, p.title, p.short_text, p.text, p.time, a.author_name FROM posts as p, category as c,' \
              f' author as a WHERE  a.id == p.author AND c.id = p.category AND a.author_name="{username}"'
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Ошибка чтения из базы данных')
        return []
       

    def add_post(self, title, category, author, short_text, text):
        try:
            self.__cur.execute(f'SELECT * FROM category WHERE category_title="{category}"')
            (cat_id, cat_title) = self.__cur.fetchone()
            print(cat_id)
            self.__cur.execute(f'SELECT * FROM author WHERE author_name="{author}"')
            (name_id, name)= self.__cur.fetchone()
            tm = math.floor(time.time())
            self.__cur.execute('INSERT INTO posts VALUES(NULL, ?, ?, ?, ?, ?,?,?)', (cat_id, title, short_text, text, '1', name_id, tm ))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления статьи в базу данных:' + str(e))
            return False
        return True