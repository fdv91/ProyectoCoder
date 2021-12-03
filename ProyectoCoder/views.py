from AppCoder.models import Curso
from django.http import HttpResponse

def curso(self):

    curso = Curso(nombre="Desarrollow Web", camada="19881")
    curso.save()
    documentoDeTexto= f"--->Curso: {curso.nombre} Camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)