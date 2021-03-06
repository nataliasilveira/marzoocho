import sqlite3

from django.shortcuts import render, render_to_response


def inicio(request):
    return render(request, "inicio/Inicio.html", {})


def cine_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Funiciones")
    Funciones = cursor.fetchall()
    db.commit()
    return render_to_response('Cine/Cine.html', {'Funciones': Funciones})

def festi_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Eventos where IdCategoria=4")
    Festivales = cursor.fetchall()
    db.commit()
    return render_to_response('Festivales/Festivales.html', {'Festivales': Festivales})

def crio_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Eventos where IdCategoria=1")
    Criollas = cursor.fetchall()
    db.commit()
    return render_to_response('Criollas/Criollas.html', {'Criollas': Criollas})   

def gastro_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Lugares where IdCategoria=2")
    Gastronomia = cursor.fetchall()
    db.commit()
    return render_to_response('Gastronomia/Gastronomia.html', {'Gastronomia': Gastronomia})

def teatro_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Lugares where IdCategoria=5")
    Teatros = cursor.fetchall()
    db.commit()
    return render_to_response('Teatros/Teatros.html', {'Teatros': Teatros})

def toques_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Eventos where IdCategoria=6")
    Toques = cursor.fetchall()
    db.commit()
    return render_to_response('Toques/Toques.html', {'Toques': Toques})

def boli_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Lugares where IdCategoria=8")
    Boliches = cursor.fetchall()
    db.commit()
    return render_to_response('Boliches/Boliches.html', {'Boliches': Boliches})

def artdep_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Eventos where IdCategoria=10")
    Artdep = cursor.fetchall()
    db.commit()
    return render_to_response('Artdep/Artdep.html', {'Artdep': Artdep})

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
    #cursor.execute("Select * from Eventos")
    Evento = cursor.execute("select Eventos.Nombre ,Eventos.Detalle, Eventos.Ciudad from Eventos")
    db.commit()
    return render_to_response('Mievento/LugaresTuri/turismo.html', {'Evento': Evento})

def montevideo_inicio_list(request):
    return render_to_response('Departamentos/Montevideo_inicio.html')

def montevideo_eventos_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    #cursor.execute("Select * from Eventos")
    Montevideo = cursor.execute("select eventos.nombre nombre , eventos.detalle detalle,eventos.ciudad ciudad from Eventos where eventos.IdDepartamento=10")
    db.commit()
    return render_to_response('Departamentos/Montevideo_eventos.html', {'Montevideo': Montevideo})

def montevideo_lugares_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    #cursor.execute("Select * from Eventos")
    Montevideo = cursor.execute("select * from lugares where iddepartamento=10")
    db.commit()
    return render_to_response('Departamentos/Montevideo_lugares.html', {'Montevideo': Montevideo})
