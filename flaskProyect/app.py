
from flask import Flask

app= Flask(__name__)

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


#ruta doble
@app.route('/usuario')
@app.route('/usuaria')
def dobleroute():
    return 'soy el mismo recurso del servidor'

#ruta POSt
@app.route('/formulario',methods=['GET'])
def formulario():
    return 'Soy un formulario'



if __name__ == '__main__':
    app.run(port=3000,debug=True)