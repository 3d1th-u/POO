from flask import Blueprint, jsonify
from app import mysql
import MySQLdb

from config import Config

internoBP= Blueprint('inter', __name__)

#RUTAS DE GESTION INTERMNA 

# ruta para probar la conexion con mysql
@internoBP.route('/DBCheck')
def DB_ckeck():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify({'status':'ok','message':'Conectado con exito'}),200
    except MySQLdb.MySQLError as e:
        return jsonify({'status':'error','message':str(e)}),500


#ruta try-catch
#esta rura maneja los errores
@internoBP.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado: Error de capa 8!'

#esta ruta maneja el error 405
@internoBP.errorhandler(405)
def metodonoP(e):
    return 'revisa el metodo de envio de tu ruta (GET o POST) !',405

