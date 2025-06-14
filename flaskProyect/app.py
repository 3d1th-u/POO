
from flask import Flask,jsonify
from flask_mysqldb import MySQL
import MySQLdb


app= Flask(__name__)

#declaramos variables de entorno

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="3d1th"
app.config['MYSQL_DB']="dbflask"
#usar solo si hay un cambio de puerto
app.config['MYSQL_PORT']=3306 

mysql=MySQL(app)

# ruta para probar la conexion con mysql
@app.route('/DBCheck')
def DB_ckeck():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify({'status':'ok','message':'Conectado con exito'}),200
    except MySQLdb.MySQLError as e:
        return jsonify({'status':'error','message':str(e)}),500


@app.route('/')
def home():
    return 'Hola Mundo FLASK'

#ruta con parametros
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return 'Hola,'+nombre+'!'

#ruta try-catch
#esta rura maneja los errores
@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado: Error de capa 8!'

#esta ruta maneja el error 405
@app.errorhandler(405)
def metodonoP(e):
    return 'revisa el metodo de envio de tu ruta (GET o POST) !',405


#ruta doble
@app.route('/usuario')
@app.route('/usuaria')
def dobleroute():
    return 'soy el mismo recurso del servidor'

#ruta POSt
@app.route('/formulario',methods=['POST'])
def formulario():
    return 'Soy un formulario'



if __name__ == '__main__':
    app.run(port=3000,debug=True)