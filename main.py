import sqlite3

conn = sqlite3.connect("org1.db")
cursor = conn.cursor()

# Создание таблицы tovary
#
cursor.execute("""CREATE TABLE tovary
                 (code,name,country,originalname,manufacturer)
               """)

cursor.execute("""CREATE TABLE sales
                  (code,client,kolichestvo,summa,nomer,date)
               """)

cursor.execute("""CREATE TABLE zakupki
                  (code,client,kolichestvo,summa,nomer,date)
               """)
conn.commit()

fo =  open("org1/tovary.csv", "r", encoding="utf-8")
mas = fo.read().split("\n")
for  s in mas:
    if s == "":
        continue

    masS = s.split("::")
    #print(masS)
    tekStroka = (masS[0], masS[1],masS[2],masS[3],masS[4])
    cursor.execute("INSERT INTO tovary VALUES(?, ?, ?, ?, ?);", tekStroka)
    conn.commit()
fo.close()
print("Товары загружены")

fo =  open("org1/sales.csv", "r", encoding="utf-8")
mas = fo.read().split("\n")
for  s in mas:
    masS = s.split("::")
    tekStroka = (masS[0], masS[1],masS[2],masS[3],masS[4],masS[5])
    cursor.execute("INSERT INTO sales VALUES(?, ?, ?, ?, ?, ?);", tekStroka)
    conn.commit()
fo.close()
print("Продажи загружены")

fo =  open("org1/zakupki.csv", "r", encoding="utf-8")
mas = fo.read().split("\n")
for  s in mas:
    masS = s.split("::")
    #print(masS)
    tekStroka = (masS[0], masS[1],masS[2],masS[3],masS[4],masS[5])
    cursor.execute("INSERT INTO zakupki VALUES(?, ?, ?, ?, ?, ?);", tekStroka)
    conn.commit()
fo.close()
print("Закупки загружены")
