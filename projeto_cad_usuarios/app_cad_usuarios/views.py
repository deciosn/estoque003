from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.tipo = request.POST.get('tipo')
    novo_usuario.valor = request.POST.get('valor')
    novo_usuario.cor = request.POST.get('cor')
    novo_usuario.gen = request.POST.get('gen')
    novo_usuario.forn = request.POST.get('forn')
    novo_usuario.save()
    #exibir todos os usuarios cadastrados em uma nova pagina
    
    usuarios = {
        'usuarios' : Usuario.objects.all()
    }
    
    return render(request,'usuarios/usuarios.html',usuarios)