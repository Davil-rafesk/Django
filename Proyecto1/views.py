from datetime import datetime
from django.http import HttpResponse


def saludo(request):    # A cada función que creamos en el archivo Views se le denomina vista. 
                        # El objetivo es devolver una respuesta donde aparezca el texto.

    domumento = """
    <html>
    <body>
    <h1>
    Hola gente, esta es la primera página creada con Django.
    </h1>
    </body>
    </html>
    """


    return HttpResponse(domumento)

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