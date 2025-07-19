
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
        try:
            cursor= mysql.connection.cursor()
            cursor.execute('SELECT * FROM tb_albums WHERE estatus = 1')
            consultaTodo = cursor.fetchall()
            
            return render_template('formulario.html', errores={}, albums=consultaTodo)
        
        except Exception as e:

            flash('Algo fallo: '+ str(e))
            return render_template('formulario.html', errores={}, albums=[])
        
        finally:
            cursor.close()

#ruta de detalle
@app.route('/detalles/<int:id>')
def detalle(id):
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_albums WHERE id=%s',(id,))
        consultaId=cursor.fetchone()
        return render_template('consulta.html', album=consultaId)
    
    except Exception as e:
        print('Error al consultar id: '+str(e))
        return redirect(url_for('home'))
        
    finally:
        cursor.close()
        
        

#ruta de consulta
@app.route('/consulta')
def consulta():
    return render_template('consulta.html', albums=[])


#ruta de actualizar
@app.route('/fromUpdate/<int:id>')
def fromUpdate(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_albums WHERE id=%s',(id,))
        actualizarId = cursor.fetchone()
        return render_template('fromUpdate.html', album=actualizarId)
    
    except Exception as e:
        print('Error al actualizar id: '+str(e))
        return redirect(url_for('consulta'))
        
    finally:
        cursor.close()

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
        
        except Exception as e:
            mysql.connection.rollback()
            flash('Algo fallo: '+ str(e))
            return redirect(url_for('home'))
        
        finally:
            cursor.close()
    
    return render_template('formulario.html',errores=errores)
#return render_template('consulta.html')



# ruta para el update
@app.route('/actualizarAlbum',methods=['POST'])
def actualizar():
    
    #listas de errores
    errores={}

    #obtener los datos para actualizar
    #inputs de la vista
    Utitulo= request.form.get('txtTitulo','').strip()
    Uartista= request.form.get('txtArtista','').strip()
    Uanio= request.form.get('txtAnio','').strip()
    Uid= request.form.get('txtId')
    
    
    if not Utitulo:
        errores['txtTitulo']='Nombre del album OBLIGATORIO'
    if not Uartista:
        errores['txtArtista']='Nombre del artista OBLIGATORIO'
    if not Uanio:
        errores['txtAnio']='Año es OBLIGATORIO'
    elif not Uanio.isdigit() or int(Uanio)< 1800 or int(Uanio)> 2100:
        errores['txtAnio']='Ingresa un año valido'
        
    
    if not errores:
    #intentamos ejecutar el insert
        try:
            cursor= mysql.connection.cursor()
            cursor.execute('UPDATE tb_albums SET albums = %s,artista = %s,anio = %s WHERE id = %s',(Utitulo, Uartista, Uanio, Uid))
            mysql.connection.commit()
            flash('El album se actualizo en la BD')
            return redirect(url_for('home'))
        
        except Exception as e:
            mysql.connection.rollback()
            flash('Algo fallo: '+ str(e))
            return redirect(url_for('home'))
        
        finally:
            cursor.close()
    
    if errores:
        album = (Uid, Utitulo, Uartista, Uanio)  # recreamos la tupla que espera la plantilla
        return render_template('fromUpdate.html', errores=errores, album=album)
    
    
#RUTA PARA VER LOS ELIMINADOS
@app.route('/eliminados')
def eliminados():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_albums WHERE estatus = 0')
        eliminados = cursor.fetchall()
        return render_template('eliminados.html', albums=eliminados)
    except Exception as e:
        flash('Error al consultar eliminados: ' + str(e))
        return redirect(url_for('home'))
    finally:
        cursor.close()

    

#RUTA DEL SOFT DELETE
@app.route('/confirmDelete/<int:id>')
def confirmDelete(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_albums WHERE id=%s', (id,))
        album = cursor.fetchone()
        
        return render_template('confirmDel.html', album=album)
    except Exception as e:
        flash('Error al obtener el álbum: ' + str(e))
        
        return redirect(url_for('home'))
    finally:
        cursor.close()


@app.route('/eliminarAlbum', methods=['POST'])
def eliminarAlbum():
    id = request.form.get('id')

    try:
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE tb_albums SET estatus = 0 WHERE id = %s', (id,))
        mysql.connection.commit()
        flash('Álbum fue eliminado correctamente')
        return redirect(url_for('home'))
    except Exception as e:
        mysql.connection.rollback()
        flash('Hubo un error al eliminar el álbum: ' + str(e))
        return redirect(url_for('home'))
    finally:
        cursor.close()



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