from app import mysql

#METODO PARA OBTENER ALBUMS ACTIVOS
def getAll():
    cursor= mysql.connection.cursor()
    cursor.execute('SELECT * FROM tb_albums WHERE estatus = 1')
    consultaTodo = cursor.fetchall()
    cursor.close()
    return consultaTodo

#METODO PARA OBTENER LOS ALBUMS ELIMINADOS
def getAllDel():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tb_albums WHERE estatus = 0')
    eliminados = cursor.fetchall()
    cursor.close()
    return eliminados

#METODO PARA OBTENER ALBUM POR ID
def getById(id):
    cursor= mysql.connection.cursor()
    cursor.execute('SELECT * FROM tb_albums WHERE id=%s',(id,))
    consultaId=cursor.fetchone()
    cursor.close()
    return consultaId

#METODO PRA INSERTAR UN ALBUM
def insertAlbum(titulo, artista, anio):
    cursor= mysql.connection.cursor()
    cursor.execute('insert into tb_albums(albums,artista,anio) values(%s,%s,%s)',(titulo,artista,anio))
    mysql.connection.commit()
    cursor.close()
    
#METODO PARA ACTUALIZAR UN ALBUM
def updateAlbum(Uid, Utitulo, Uartista, Uanio):
    cursor= mysql.connection.cursor()
    cursor.execute('UPDATE tb_albums SET albums = %s,artista = %s,anio = %s WHERE id = %s',(Utitulo, Uartista, Uanio, Uid))
    mysql.connection.commit()
    cursor.close()
    
#METODO PARA ELIMINAR ALBUM
def softDeleteAlbum(id):
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE tb_albums SET estatus = 0 WHERE id = %s', (id,))
    mysql.connection.commit()
    cursor.close()