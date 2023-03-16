import psycopg2
import pandas as pd
import matplotlib as plt
con = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='Gardik',
    host='127.0.0.1',
port='5432')

cur = con.cursor()
cur.execute('SELECT * FROM book1')
rows = cur.fetchall()
print(rows)
lstrows = []
for row in rows:
    lstrows.append(list(row))
print(lstrows)
con.close
df = pd.DataFrame(lstrows, columns=['book_id', 'title', 'price', 'amount', 'new_price', 'autor_id'])
print(df)
df.plot.bar('title', 'amount')
df.plot.bar('title', 'price')
