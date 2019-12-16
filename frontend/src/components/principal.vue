<template>
  <v-container class="contenedor" fluid fill-height name="contenedor">
    <v-card name="tarjetaRoja">
      <div>
        <img class="imagen" src="https://s1.eestatic.com/2017/05/02/elbernabeu/futbol/Futbol_212990738_89786625_1024x576.jpg">
      </div>
      <v-layout>
        <v-flex name="flexio">
          <div class="fondo">
          </div>
          <div class="informacion">
            <div class="msj_principal">
            </div>
            <div class="selects">
              <h3> Formulario:</h3>
              <form id="formulario">
                <table style="width:100%">
                  País del equipo: <br>
                  <select id="pais" ref="pais">
                    <option selected value="no"><b>Elige una opcion</b></option>
                    <option value="España">España</option>
                    <option value="Inglaterra">Inglaterra</option>
                    <option value="Italia">Italia</option>
                    <option value="Francia">Francia</option>
                    <option value="Alemania">Alemania</option>
                    <option value="Holanda">Holanda</option>
                    <option value="Portugal">Portugal</option>
                  </select>
                  <br><br>Latitud:<br>
                  <select name="latitud" ref="latitud">
                    <option selected value="no"><b>Elige una opcion</b></option>
                    <option value="Norte">Norte</option>
                    <option value="Centro">Centro</option>
                    <option value="Sur">Sur</option>
                  </select>
                  <br><br>Longitud:<br>
                  <select name="longitud" ref="longitud">
                    <option selected value="no"><b>Elige una opción</b></option>
                    <option value="Oeste">Oeste</option>
                    <option value="Centro">Centro</option>
                    <option value="Este">Este</option>
                  </select>
                <br><br>Presupuesto del equipo:<br>
                <select name="presupuesto" ref="presupuesto">
                  <option selected value="no"><b>Elige una opción</b></option>
                  <option value="Bajo">Presupuesto bajo</option>
                  <option value="Medio">Presupuesto medio</option>
                  <option value="Alto">Presupuesto alto</option>
                </select>
                  <br><br>Capacidad del estadio:<br>
                  <select name="capacidad" ref="capacidad">
                    <option selected value="no"><b>Elige una opción</b></option>
                    <option value="Menor">Menor de 25000 espectadores</option>
                    <option value="Medio">Entre 25000 y 50000 espectadores</option>
                    <option value="Mayor">Mayor de 50000 espectadores</option>
                  </select>
              </table>
              </form>
              <!--input type="button" class= "button" onclick="getData()" value="Buscar datos"-->
              <v-card-actions>
                <div class="button">
                  <v-btn @click="getData" name="button">
                    Buscar Datos
                  </v-btn>
                </div>
              </v-card-actions>
            </div>
          </div>
        </v-flex>
      </v-layout>
    </v-card>
  </v-container>
</template>

<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
import axios from 'axios'
let config = {
  headers: {
    header1: 'Access-Control-Allow-Origin',
  }
}
export default {
  data: () => ({
    pais: '',
    latitud: '',
    longitud: '',
    presupuesto: '',
    capacidad: ''
  }),
  methods: {
    getData: function () {
      this.pais = this.$refs.pais.value
      this.latitud = this.$refs.latitud.value
      this.longitud = this.$refs.longitud.value
      this.presupuesto = this.$refs.presupuesto.value
      this.capacidad = this.$refs.capacidad.value
      this.envia()
    },
    envia: function () {
      const path = 'http://localhost:5000/api/v1.0/obtiene'
      axios.post(path, {
        country: this.pais,
        latitude: this.latitude,
        longitude: this.longitud,
        budget: this.presupuesto,
        capacity: this.capacidad
      })
        .then(function(res) {
          if(res.status==201) {
            //mensaje.innerHTML = 'El nuevo Post ha sido almacenado con id: ' + res.data.id;
            alert("oeeeoeoeoeoeoeeeeeeeeeeeeeeeeeeeeeeeoeeeeeeeeoeeeeeeeee")
          }
        })
        .catch(function(err) {
          alert(err)
        })
    }
  }
}
</script>

<style>
.titulo {
  color: rgb(255, 255, 255);
}
.msj_principal {
  margin-bottom: 10px;
}
.selects {

  color: rgb(255, 255, 255);
  margin-left: 10px;
  margin-right: auto;
  background-size: cover;
}

.informacion {
  position: relative;
  display: inline-block;
  text-align: left;
  z-index: 10;
  margin-top: 6%;
}

.imagen {
  position: absolute;
  width: 100%;
  height: 101%;
  margin-left: -50%;
  margin-top: -1%;
  z-index: -3;
}

body {
  background: #000000;
}

.fondo {
  position: absolute;
  background: #000000;
  z-index: 5;
  width: 20%;
  height: 80%;
  margin-left: 40%;
  margin-top: 4%;
  opacity: 60%;
}

.button {
  text-align: center;
  background: #049e6b;
  height: 30px;
  width: 240px;
  border-radius: 20px;
  margin-top: 20px;
  color: #ffffff;
  font-weight: bold;
  padding-top: 10px;
}

select {
  margin-top: 10px;
}
</style>
