import pymysql as db

connection = db.connect(host='localhost',
                             user='root',
                             password='password',
                             db='paints')

query = "select * from paints.acrylic"

cursor = connection.cursor()
cursor.execute(query)
results = cursor.fetchone()

print(results)
