from turtle import home
from flask import  Flask
from .inicio import inicio
from .panel import panel





miApp = Flask(__name__)




#miApp.register_blueprint(inicio)
miApp.register_blueprint(inicio)
miApp.register_blueprint(panel)



#miApp.config['MAIL_SERVER']='smtp.gmail.com'
#miApp.config['MAIL_PORT'] = 465
#miApp.config['MAIL_USERNAME'] = 'mercado.maravillas.online@gmail.com'
#miApp.config['MAIL_PASSWORD'] = 'vpnvsbphgvakhqdv'
#miApp.config['MAIL_USE_TLS'] = False
#miApp.config['MAIL_USE_SSL'] = True
#mail = Mail(miApp)


miApp.secret_key='mysecretkey'
    

