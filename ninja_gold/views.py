# Create your views here.
from django.shortcuts import render, redirect
import random 
from time import  localtime, strftime



def index(request):
    return render (request,'core/index.html')


def process_money(request):
    # Si variable no existen en sesion se crean
    if 'log' not in request.session:
        request.session['log'] = []

    if 'jugadas' not in request.session:
        request.session['jugadas']=0

    if 'cochinito' not in request.session:
        request.session['cochinito']=0
    
    # Se aumenta contador de jugadas
    if 'jugadas' in request.session:
        request.session['jugadas']+=1
        print (request.session['jugadas'])

    
    # Se lee la opcion la variable 'opcion' del formulario y calcula valor 'juaga' segun opcion
    opc_for= request.POST['opcion']
    print(opc_for)

    if opc_for == 'granja':
        juega= random.randrange(10, 20, 1)
    
    if opc_for == 'cueva':
        juega=random.choice(range(5, 10, 1))
        
    if opc_for == 'casa':
        juega=random.randrange(2, 5, 1)    
    
    if opc_for == 'casino':
        toma_pierde= random.randrange(0, 2, 1)
        juega= random.randrange(0, 50, 1)    
        
        if toma_pierde == 0:
            juega *=1

        else:
            juega*=-1
    
    print(juega)    
    hora = strftime("a las %I:%M %p del %m-%d-%Y ", localtime())
    
    if 'cochinito' in request.session:
        
        print("hola")

        if juega > 0:
            request.session['cochinito']+=juega
            print(request.session['cochinito'])
            texto = (f"Ganas {juega} monedas en la {opc_for.upper()} a las {hora} wohooe :D")
            color = "verde"
        else:
            request.session['cochinito']+=juega
            print(request.session['cochinito'])
            texto=(f"PIERDES {juega} monedas en la {opc_for.upper()} a las {hora} :( ")
            color="rojo"
                
        # Se crea dict para enviar a plantilla en variable 'log'
        
        contexto = {
        'ptexto': texto,
        'pcolor': color
        }
        request.session['log'].append(contexto)
        request.session.save()

        print(request.session['log'])

    return redirect('/')


def reset(request):
    request.session['cochinito']= 0
    request.session['jugadas'] = 0
    request.session['log'] = []
    return redirect ("/")
