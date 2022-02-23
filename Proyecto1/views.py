from django.http import HttpResponse


def saludo(request):    # A cada función que creamos en el archivo Views se le denomina vista. 
                        # El objetivo es devolver una respuesta donde aparezca el texto.

    return HttpResponse("Hola gente, esta es la primera pagian creada con Django.")

def despedida(request):

    return HttpResponse("Esta vista es la función de despedida.") # segunda vista.
