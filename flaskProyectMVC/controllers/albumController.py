from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.albumModel import *

albumsBP= Blueprint('albums',__name__)

#RUTA DE INICIO DESDE EL APP
@albumsBP.route('/')
def home():
        try:
            consultaTodo = getAll()
            
            return render_template('formulario.html', errores={}, albums=consultaTodo)
        
        except Exception as e:

            flash('Algo fallo: '+ str(e))
            return render_template('formulario.html', errores={}, albums=[])

#RUTA PARA VER LOS ELIMINADOS
@albumsBP.route('/eliminados')
def eliminados():
    try:
        eliminados = getAllDel()
        
        return render_template('eliminados.html', albums=eliminados)
    except Exception as e:
        flash('Error al consultar eliminados: ' + str(e))
        return redirect(url_for('albums.home'))
        
#RUTA DE LA CONSULTA
@albumsBP.route('/consulta')
def consulta():
    return render_template('consulta.html', albums=[])
        

#RUTA DE CONSULTAR ID
@albumsBP.route('/detalles/<int:id>')
def detalle(id):
    try:
        consultaId = getById(id)
        
        return render_template('consulta.html', album=consultaId)
    
    except Exception as e:
        print('Error al consultar id: '+str(e))
        return redirect(url_for('albums.home'))


        
#RUTA DE GUARDAR
@albumsBP.route('/guardarAlbum',methods=['POST'])
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
            insertAlbum(titulo, artista, anio)
            
            flash('El album se guardo en la BD')
            return redirect(url_for('albums.home'))
        
        except Exception as e:
            mysql.connection.rollback()
            flash('Algo fallo: '+ str(e))
            return redirect(url_for('albums.home'))
    
    return render_template('formulario.html',errores=errores)
#return render_template('consulta.html')


#RUTA PARA EDITAR(ABRE EL FORM)
@albumsBP.route('/fromUpdate/<int:id>')
def fromUpdate(id):
    try:
        consultarId = getById(id)
        
        return render_template('fromUpdate.html', album=consultarId)
    
    except Exception as e:
        print('Error al actualizar id: '+str(e))
        return redirect(url_for('albums.consulta'))


#RUTA PARA EJECUTAR LA ACTUALIZACIÓN
@albumsBP.route('/actualizarAlbum',methods=['POST'])
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
            updateAlbum(Uid, Utitulo, Uartista, Uanio)
            
            flash('El album se actualizo en la BD')
            return redirect(url_for('albums.home'))
        
        except Exception as e:
            mysql.connection.rollback()
            flash('Algo fallo: '+ str(e))
            return redirect(url_for('albums.home'))

    
    if errores:
        album = (Uid, Utitulo, Uartista, Uanio)  # recreamos la tupla que espera la plantilla
        return render_template('fromUpdate.html', errores=errores, album=album)
    
    
#RUTA DEL SOFT DELETE
@albumsBP.route('/confirmDelete/<int:id>')
def confirmDelete(id):
    try:
        consultaId = getById(id)
        
        return render_template('confirmDel.html', album=consultaId)
    except Exception as e:
        flash('Error al obtener el álbum: ' + str(e))
        
        return redirect(url_for('albums.home'))


#RUTA DE CONFIRM DELETE    
@albumsBP.route('/eliminarAlbum/<int:id>', methods=['POST'])
def eliminarAlbum(id):
    id = request.form.get('id')

    try:
        softDeleteAlbum(id)
        
        flash('Álbum fue eliminado correctamente')
        return redirect(url_for('albums.home'))
    except Exception as e:
        mysql.connection.rollback()
        flash('Hubo un error al eliminar el álbum: ' + str(e))
        return redirect(url_for('albums.home'))


#RUTA DE
