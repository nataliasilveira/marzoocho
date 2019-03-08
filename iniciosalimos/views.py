import sqlite3
from django.shortcuts import render, render_to_response


def inicio(request):
    return render(request, "inicio/Inicio.html", {})


def cine_list(request):
    db = sqlite3.connect(database='Salimos.db')
    cursor = db.cursor()
    cursor.execute("Select   Funcion, Fecha, Hora from Funiciones")
    llamarcine = cursor.fetchall()
    db.close()
    return render_to_response('Cine/Cine.html', {'llamarcine': llamarcine})
