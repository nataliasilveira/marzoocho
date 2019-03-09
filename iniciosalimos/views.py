import sqlite3

from django.shortcuts import render, render_to_response


def inicio(request):
    return render(request, "inicio/Inicio.html", {})


def cine_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Funiciones")
    Funciones = cursor.fetchall()
    Fecha = cursor.execute("Select Funiciones.Fecha from Funiciones")
    db.commit()
    return render_to_response('Cine/Cine.html', {'Funciones': Funciones}, {'Fecha': Fecha})


def enfmilia_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Lugares")
    Lugares = cursor.execute(
        "select Lugares.Nombre ,Lugares.Ciudad ,Lugares.Telefono, Lugares.Direccion, Lugares.Horario from Lugares")
    db.commit()
    return render_to_response('Mievento/Enfamilia/enfamilia.html', {'Lugares': Lugares})


def conamigos_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Categorias")
    Eventos = cursor.execute(
        "select Eventos.Nombre ,Eventos.Ciudad ,Eventos.Detalle, Eventos.FechaInicio, Eventos.Contacto from Eventos")
    db.commit()
    return render_to_response('Mievento/Conamigos/conamigos.html', {'Eventos': Eventos})


def ninos_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Eventos")
    Eventos = cursor.execute("select Eventos.Nombre,Eventos.Ciudad ,Eventos.Detalle, Eventos.Contacto from Eventos")
    db.commit()
    return render_to_response('Mievento/Paraninos/ninos.html', {'Eventos': Eventos})


def paseos_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Lugares")
    Lugares = cursor.execute("select Lugares.Nombre ,Lugares.Direccion, Lugares.Barrio from Lugares")
    db.commit()
    return render_to_response('Mievento/Paseos/paseos.html', {'Lugares': Lugares})


def turismo_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Lugares")
    Lugares = cursor.execute("select Lugares.Nombre ,Lugares.Direccion, Lugares.Barrio from Lugares")
    db.commit()
    return render_to_response('Mievento/LugaresTuri/turismo.html', {'Lugares': Lugares})


def airlib_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Eventos")
    Evento = cursor.execute("select Eventos.Nombre ,Eventos.Detalle, Eventos.Ciudad from Eventos")
    db.commit()
    return render_to_response('Mievento/LugaresTuri/turismo.html', {'Evento': Evento})
