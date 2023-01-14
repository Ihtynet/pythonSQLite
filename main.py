import sqlite3

conn = sqlite3.connect("org1.db")
cursor = conn.cursor()


"""fo =  open("org1/tovary.csv", "r", encoding="utf-8")
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


fo =  open("org1/sales.csv", "r", encoding="utf-8")
mas = fo.read().split("\n")
for  s in mas:
    masS = s.split("::")
    tekStroka = (masS[0], masS[1],masS[2],masS[3],masS[4])
    cursor.execute("INSERT INTO sales VALUES(?, ?, ?, ?, ?);", tekStroka)
    conn.commit()
fo.close()"""

fo =  open("org1/zakupki.csv", "r", encoding="utf-8")
mas = fo.read().split("\n")
for  s in mas:
    masS = s.split("::")
    #print(masS)
    tekStroka = (masS[0], masS[1],masS[2],masS[3],masS[4])
    cursor.execute("INSERT INTO zakupki VALUES(?, ?, ?, ?, ?);", tekStroka)
    conn.commit()
fo.close()

