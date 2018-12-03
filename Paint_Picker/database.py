import pymysql as db

connection = db.connect(host='localhost',
                             user='root',
                             password='password',
                             db='paints')


def rbg(self):
  query = "select rbg from paints.acrylic"
  cursor = connection.cursor()
  cursor.execute(query)
  results = cursor.fetchall()
  return results

def retreive_colors(self, rbg):
  ans = []
  for color in rbg:
    query = "select paint_name,paint)link from paints.acrylic where rbg =" + color
    cursor = connection.cursor()
    cursor.execute(query)
    ans.append(cursor.fetchone())
  return results

