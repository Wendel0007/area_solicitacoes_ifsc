import psycopg2
import psycopg2.extras
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EditarProdutosCantinaForm, ProdutosCantinaForm
from .models import ProdutosCantina


def conectaBancoTeste():
    conexao = psycopg2.connect(
        dbname='base_teste', user='postgres', password='zaq12wsxcde3', host='localhost', port='5432'
    )
    conexao.set_client_encoding('utf8')
    cursor = conexao.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    return cursor, conexao


@login_required
def painelCantina(request):
    if request.method == 'GET':
        if request.user.groups.filter(name='Administrativo').exists() or request.user.groups.filter(name='Cantina').exists():
            return render(request, 'painel_cantina/components/index.html')
        else:
            messages.error(request, "Acesso negado!")
            return redirect('dashboard')


@login_required
def NovoProdutoCantina(request):
    if request.method == 'GET':
        form = ProdutosCantinaForm()
        return render(request, 'painel_cantina/components/novo_produto.html', {'form': form})

    if request.method == 'POST':
        form = ProdutosCantinaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto Criado com sucesso')
            return redirect('listar_produto_cantina')


@login_required
def listarProdutoCantina(request):
    if request.method == 'GET':
        produtos = ProdutosCantina.objects.all()

        return render(request, 'painel_cantina/components/lista_produto.html', {'produtos': produtos})


@login_required
def EditarProdutoCantina(request, id):
    produto = get_object_or_404(ProdutosCantina, id=id)

    if request.method == 'GET':
        formulario = EditarProdutosCantinaForm(instance=produto)
        contexto = {'formulario': formulario, 'id': id}
        return render(request, 'painel_cantina/components/editar_produto.html', context=contexto)

    if request.method == 'POST':
        formulario = EditarProdutosCantinaForm(
            request.POST, files=request.FILES, instance=produto)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Produto editado com sucesso')
            return redirect('listar_produto_cantina')
        else:
            messages.error(request, 'Erro ao editar o produto')
            return redirect('listar_produto_cantina')


@login_required
def DeletarProdutoCantina(request, id):
    produto = ProdutosCantina.objects.get(id=id)
    produto.delete()
    messages.success(request, 'Produto deletado com sucesso')
    return redirect('listar_produto_cantina')
