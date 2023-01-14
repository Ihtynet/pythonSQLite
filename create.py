import sqlite3

conn = sqlite3.connect("org1.db")
cursor = conn.cursor()

# Создание таблицы tovary
#
cursor.execute("""CREATE TABLE tovary
                 (code,name,country,originalname,manufacturer)
               """)

cursor.execute("""CREATE TABLE sales
                  (code,client,kolichestvo,summa,date)
               """)

cursor.execute("""CREATE TABLE zakupki
                  (code,client,kolichestvo,summa,date)
               """)
conn.commit()