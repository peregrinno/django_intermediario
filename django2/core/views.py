from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Produto

from .forms import ContatoForms
from .forms import ProdutoModelForm

# Create your views here.

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForms(request.POST or None)
     
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviada!')
            print(f'Nome: {nome}')
            print(f'Email: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForms()
        else:
            messages.error(request, 'Erro ao enviar e-mail!')

    context = {
        'form': form,
    }

    return render(request, 'contato.html', context)

def produto(request):
    if str(request.user) != 'AnonymousUser':   
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():

                form.save(commit=True)

                form = ProdutoModelForm()
            
                messages.success(request, 'Produto salvo com sucesso')
            else:
                messages.error(request, 'Erro ao salvar produto')
        else:
            form = ProdutoModelForm()

        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')

