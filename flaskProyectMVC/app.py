from flask import Flask ,jsonify,render_template,request, url_for,flash,redirect
from flask_mysqldb import MySQL
import MySQLdb
from config import Config

app= Flask(__name__)
mysql=MySQL(app)

def create_app():
    app= Flask(__name__)
    app.config.from_object(Config)
    mysql.init_app(app)
    
    from controllers.albumController import albumsBP
    app.register_blueprint(albumsBP)
    
    return app

if __name__ == '__main__':
    app= create_app()
    app.run(port=3000,debug=True)