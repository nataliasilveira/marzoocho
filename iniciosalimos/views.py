import sqlite3

from django.shortcuts import render, render_to_response


def inicio(request):
    return render(request, "inicio/Inicio.html", {})


def cine_list(request):
    db = sqlite3.connect(database='Salimos.db')
    cursor = db.cursor()
    cursor.execute("Select Funiciones.Funcion from Funiciones")
    Funcion = cursor.fetchall()
    Fecha = cursor.execute("Select Funiciones.Fecha from Funiciones")
    db.close()
    return render_to_response('Cine/Cine.html', {'Funcion': Funcion}, {'Fecha': Fecha})
