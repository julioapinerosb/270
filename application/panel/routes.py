from flask import Flask, render_template, url_for, request, make_response, redirect, Response, Blueprint, session
from . import panel
import pymysql
from . bd import obtener_conexion

@panel.route('/panel')
def panel():
    
    print('ojo')

    return render_template('panel.html') 



