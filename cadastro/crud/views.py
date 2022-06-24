from django.shortcuts import redirect, render

from .models import Cliente, Produtos

def lista(request):
  retorno={'lista':Cliente.objects.all()}
  return render(request,"crud/lista.html",retorno)

def creat(request):
  print(request.POST)
  fullnome=request.GET['fullname']
  endereco=request.GET['endereco']
  produto=request.GET['produto']
  client=Cliente(fullnome,endereco,produto)
  client.save()
  return redirect('lista')

def adicionar(request):
  produto={'produto':Produtos.objects.all()}
  return render(request,'crud/adicionarCliente.html',produto)

