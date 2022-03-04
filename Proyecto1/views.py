from datetime import datetime
from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object): # Defino la clase Persona, dentro de esta creo un Constructor al que le doy las variables por POO.

    def __init__(self, nombre, apellido):

        self.nombre = nombre

        self.apellido = apellido


def saludo(request):    # A cada función que creamos en el archivo Views se le denomina vista. 
                        # El objetivo es devolver una respuesta donde aparezca el texto.
    p1 = Persona("Estudiante Mauricio", "Dávila")
    
    #nombre = "Mauricio"

    #apellido = "Dávila"

    ahora = datetime.now()

    temas_curso = ["Plantillas", "Modelos","Formularios","Vistas","Despliegues"]

    #doc_externo = open("E:/respaldoC/Programación/Django/ProyectosDjango/Proyecto1/Proyecto1/Plantillas/mi_plantilla.html")

    #plt = Template(doc_externo.read())

    #doc_externo.close()

    #doc_externo = loader.get_template("mi_plantilla.html")

    #ctx = Context({"nombre_pesona":p1.nombre, "apellido_persona":p1.apellido,"momento_ahora":ahora, "Temas":temas_curso})

    #domumento = doc_externo.render(ctx)

    return render(request, "mi_plantilla.html", {"nombre_pesona":p1.nombre, "apellido_persona":p1.apellido,"momento_ahora":ahora, "Temas":temas_curso})

def plantillas(request):

    fecha_actual = datetime.now()

    return render(request, "hija1.html", {"momento_ahora":fecha_actual})

def plantillasDos(request):

    fecha_actual = datetime.now()

    return render(request, "hija2.html", {"momento_ahora":fecha_actual})


def despedida(request):


    return HttpResponse("Esta vista es la función de despedida.") # segunda vista.


def dame_fecha(Request):

    fecha_actual = datetime.now()

    domumento = """
    <html>
    <body>
    <h2>
    Fecha y hora actual %s 
    </h2>
    </body>
    </html> """ % fecha_actual  # %s es un marcador de posición, se usa para marcar la posición de fecha_actual
                                # en la variable documento, dento del html.
    return HttpResponse(domumento)

def calcula_edad(request, edad, agno):

    #edad_actual = 18
    periodo = agno - 2022
    edad_futura = edad + periodo
    documento = "<html><body><h2> En el año %s tendrás %s años." %(agno, edad_futura) # se pueden usar 2 marcadores de posición
                                                                                      # sólo se debe respetar el oden.
    return HttpResponse(documento)