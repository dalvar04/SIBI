import csv
import pandas as pd 
import numpy as np
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from neo4j import GraphDatabase
from warnings import simplefilter

simplefilter(action='ignore', category=FutureWarning)

app = Flask(__name__)
app.run('127.0.0.1', 8080, debug=True)
cors = CORS(app, resources={r'/api/v1.0/*': {'origins': '*'}})
#cross_origin(origin='*',headers=['Content-Type','Authorization'])

df = pd.read_csv(r"bdFull.csv",encoding="ISO-8859-1")

pais='Alemania'
latitud='Norte'
longitud='Oeste'
presupuesto='Bajo'
capacidad='Alto'


console.log('hola')
@app.route('localhost/api/v1.0/obtiene', methods=['GET','POST'])
def obtiene():
    print("hola")
    data = request.get_json()
    datos = []

    for value in data.items():
        datos.append(value)

    pais = datos[0]
    latitud = datos[1]
    longitud = datos[2]
    presupuesto = datos[3]
    capacidad = datos[4]

    dfPais=df[df['Pais']==pais]
    filasP=dfPais.size//8
    dfLatitud=dfPais[dfPais['Latitud']==latitud]
    filasLA=dfLatitud.size//8


    if filasLA>0:
        dfLongitud=dfLatitud[dfLatitud['Longitud']==longitud]
        filasLO=dfLongitud.size//8 
        print("-- Hay al menos un equipo que cumple la latitud")
        if filasLO>0:
            dfPresupuesto=dfLongitud[dfLongitud['Presupuesto']==presupuesto]
            filasP=dfPresupuesto.size//8
            print("-- Hay al menos un equipo que cumple la latitud y la longitud")
            if filasP>0:
                dfCapacidad=dfPresupuesto[dfPresupuesto['CapacidadEstadio']==capacidad]
                filasC=dfCapacidad.size//8
                print("-- Hay al menos un equipo que cumple la latitud, la longitud y el presupuesto")
                if filasC>1:
                    print("********************************************")
                    print("Hay más de un equipo que cumple las caracteristicas finales")
                    print(dfCapacidad['Nombre'])
                    print("********************************************")
                elif filasC<1:
                    print("********************************************")
                    print("No hay ningun equipo que cumpla todas las caracteristicas.Los siguientes cumplen todas menos la capacidad del estadio")
                    print(dfPresupuesto['Nombre'])
                    print("********************************************")
                else:
                    print("********************************************")
                    print("Hay un equipo que cumple con todas las caracteristicas")
                    print(dfCapacidad['Nombre'])
                    print("********************************************")
            else:
                print("********************************************")
                print("No hay ningun equipo que cumpla con el presupuesto.Los siguientes equipos cumplen con el pais, latitud y longitud")
                print(dfLongitud['Nombre'])
                print("********************************************")
        else:
            print("********************************************")
            print("No hay ningun equipo que cumpla con la longitud.Los siguientes equipos cumplen con el pais y la latitud")
            print(dfLatitud['Nombre'])
            print("********************************************")
    else:
        print("********************************************")
        print("No hay ningun equipo que cumpla con la latitud.Los siguientes equipos cumplen con el pais")
        print(dfPais['Nombre'])
        print("********************************************")"""
    return jsonify("A tomar por saco todo el mundoooooooooooooo, chumba, chumba, etc")

if __name__ == '__main__':
    app.run(debug=True)
