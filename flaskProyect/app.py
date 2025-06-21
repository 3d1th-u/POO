
from flask import Flask ,jsonify,render_template,request, url_for,flash,redirect
from flask_mysqldb import MySQL
import MySQLdb


app= Flask(__name__)

#declaramos variables de entorno

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="3d1th"
app.config['MYSQL_DB']="dbflask"
#usar solo si hay un cambio de puerto
#app.config['MYSQL_PORT']=3306 
app.secret_key='mysecretkey'

mysql=MySQL(app)


#ruta de inicio
@app.route('/')
def home():
    return render_template('formulario.html')

#ruta de consulta
@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

# ruta para el insert
@app.route('/guardarAlbum',methods=['POST'])
def guardar():
    
    #listas de errores
    errores={}
    
    #obtener los datos a insertar
    #inputs de la vista
    titulo= request.form.get('txtTitulo','').strip()
    artista= request.form.get('txtArtista','').strip()
    anio= request.form.get('txtAnio','').strip()
    
    
    if not titulo:
        errores['txtTitulo']='Nombre del album OBLIGATORIO'
    if not artista:
        errores['txtArtista']='Nombre del artista OBLIGATORIO'
    if not anio:
        errores['txtAnio']='Año es OBLIGATORIO'
    elif not anio.isdigit() or int(anio)< 1800 or int(anio)> 2100:
        errores['txtAnio']='Ingresa un año valido'
        
    
    
    if not errores:
    #intentamos ejecutar el insert
        try:
            cursor= mysql.connection.cursor()
            cursor.execute('insert into tb_albums(albums,artista,anio) values(%s,%s,%s)',(titulo,artista,anio))
            mysql.connection.commit()
            flash('El album se guardo en la BD')
            return redirect(url_for('home'))
        
        except:
            mysql.connection.rollback()
            flash('Algo fallo: '+ str(e))
            return redirect(url_for('home'))
        
        finally:
            cursor.close()
    
    return render_template('formulario.html',errores=errores)
#return render_template('consulta.html')


# ruta para probar la conexion con mysql
@app.route('/DBCheck')
def DB_ckeck():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify({'status':'ok','message':'Conectado con exito'}),200
    except MySQLdb.MySQLError as e:
        return jsonify({'status':'error','message':str(e)}),500



#ruta try-catch
#esta rura maneja los errores
@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado: Error de capa 8!'

#esta ruta maneja el error 405
@app.errorhandler(405)
def metodonoP(e):
    return 'revisa el metodo de envio de tu ruta (GET o POST) !',405




if __name__ == '__main__':
    app.run(port=3000,debug=True)