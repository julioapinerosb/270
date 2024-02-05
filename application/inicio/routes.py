from flask import Flask, render_template, url_for, request, make_response, redirect, Response, Blueprint, session,flash,jsonify
from . import inicio
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
from . bd import obtener_conexion
from datetime import datetime

@inicio.route('/', methods=['GET'])
@inicio.route('/inicio', methods=['GET'])
def index():

    return render_template('inicio.html')

#inicio de sesion
@inicio.route('/login', methods=['GET', 'POST'])
def login():
    conexion=obtener_conexion()
   
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        hashed_password = generate_password_hash(password,method='pbkdf2:sha256')
        

        with conexion.cursor() as cursor:
            cursor.execute('SELECT  password FROM usuarios WHERE usuario = %s',(usuario))
            result = cursor.fetchone()

            if result:
                hashed_password_from_database = result[0]
                             
                if check_password_hash(hashed_password_from_database, password):
                    session['usuario']  = usuario
                    return redirect(url_for('panel.panel'))

                
            flash("Usuario o contraseña incorrectos")
            return redirect(url_for('inicio.index')) 

                                
@inicio.route('/ingreso_usuario',methods=['GET', 'POST'])
def ingreso_usuario():
    conexion=obtener_conexion()

    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        hashed_password = generate_password_hash(password,method='pbkdf2:sha256')

        with conexion.cursor() as cursor:
            cursor.execute('INSERT INTO usuarios (usuario, password, fecha) VALUES (%s, %s,%s)', (usuario, hashed_password, datetime.now()))
            conexion.commit()
    
    flash("Usuario o contraseña incorrectos")
    return redirect(url_for('inicio.index')) 