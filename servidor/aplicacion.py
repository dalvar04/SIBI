import csv
import pandas as pd 
import numpy as np
from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

df = pd.read_csv(r"bdFull.csv",encoding="ISO-8859-1")

pais='Alemania'
latitud='Norte'
longitud='Oeste'
presupuesto='Bajo'
capacidad='Alto'
mensaje='mensaje'
equipo=[]

@app.route('/api/v1.0/obtiene', methods=['GET','POST'])
def obtiene():
    data = request.get_json()
    datos = []

    for value in data.items():
        datos.append(value)

    pais = datos[0][1]
    latitud = datos[1][1]
    longitud = datos[2][1]
    presupuesto = datos[3][1]
    capacidad = datos[4][1]


    dfPais=df[df['Pais']==pais]
    filasP=dfPais.size//8
    dfLatitud=dfPais[dfPais['Latitud']==latitud]
    filasLA=dfLatitud.size//8
  
    if filasLA>0:
        dfLongitud=dfLatitud[dfLatitud['Longitud']==longitud]
        filasLO=dfLongitud.size//8 
        print("-- Hay al menos un equipo que cumple la latitud") 
        mensaje="-- Hay al menos un equipo que cumple la latitud"
        if filasLO>0:
            dfPresupuesto=dfLongitud[dfLongitud['Presupuesto']==presupuesto]
            filasP=dfPresupuesto.size//8
            print("-- Hay al menos un equipo que cumple la latitud y la longitud")
            mensaje="-- Hay al menos un equipo que cumple la latitud y la longitud"
            if filasP>0:
                dfCapacidad=dfPresupuesto[dfPresupuesto['CapacidadEstadio']==capacidad]
                filasC=dfCapacidad.size//8
                print("-- Hay al menos un equipo que cumple la latitud, la longitud y el presupuesto")
                mensaje="-- Hay al menos un equipo que cumple la latitud, la longitud y el presupuesto"
                if filasC>1:
                    print("********************************************")
                    print("Hay más de un equipo que cumple las caracteristicas finales")
                    mensaje="Hay más de un equipo que cumple las caracteristicas finales"
                    print(dfCapacidad['Nombre'])
                    equipo=dfCapacidad['Nombre'].tolist()
                    print("********************************************")
                elif filasC<1:
                    print("********************************************")
                    print("No hay ningun equipo que cumpla todas las caracteristicas.Los siguientes cumplen todas menos la capacidad del estadio")
                    mensaje="No hay ningun equipo que cumpla todas las caracteristicas.Los siguientes cumplen todas menos la capacidad del estadio"
                    print(dfPresupuesto['Nombre'])
                    equipo=dfPresupuesto['Nombre'].tolist()
                    print("********************************************")
                else:
                    print("********************************************")
                    print("Hay un equipo que cumple con todas las caracteristicas")
                    mensaje="Hay un equipo que cumple con todas las caracteristicas"
                    print(dfCapacidad['Nombre'])
                    equipo = dfCapacidad['Nombre'].tolist()
                    print("********************************************")
            else:
                print("********************************************")
                print("No hay ningun equipo que cumpla con el presupuesto.Los siguientes equipos cumplen con el pais, latitud y longitud")
                mensaje="No hay ningun equipo que cumpla con el presupuesto.Los siguientes equipos cumplen con el pais, latitud y longitud"
                print(dfLongitud['Nombre'])
                equipo=dfLongitud['Nombre'].tolist()
                print("********************************************")
        else:
            print("********************************************")
            print("No hay ningun equipo que cumpla con la longitud.Los siguientes equipos cumplen con el pais y la latitud")
            mensaje="No hay ningun equipo que cumpla con la longitud.Los siguientes equipos cumplen con el pais y la latitud"
            print(dfLatitud['Nombre'])
            equipo=dfLatitud['Nombre'].tolist()
            print("********************************************")
    else:
        print("********************************************")
        print("No hay ningun equipo que cumpla con la latitud.Los siguientes equipos cumplen con el pais")
        mensaje="No hay ningun equipo que cumpla con la latitud.Los siguientes equipos cumplen con el pais"
        print(dfPais['Nombre'])
        equipo=dfPais['Nombre'].tolist()
        print("********************************************")
    return jsonify(mensaje=mensaje, recomendacion=equipo)

if __name__ == "__main__":
    app.run()