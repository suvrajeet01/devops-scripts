from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

ip="147.15.9.2"
user="suvrajeet"
password="suv1234"
dbname="Db1"

app.config['MYSQL_DATABASE_USER']= user
app.config['MYSQL_DATABASE_HOST']=ip
app.config['MYSQL_DATABASE_PASSWORD']=password
app.config['MYSQL_DATABASE_DB']=dbname

mysql=MySQL()
mysql.init_app(app)

@app.route("/data")
def MYDB_data():
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute("select *from t1")
    data=cursor.fetchall()
    return str(data)

app.run(host='0.0.0.0')
