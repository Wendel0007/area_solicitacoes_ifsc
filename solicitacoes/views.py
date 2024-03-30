import pdb

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SolicitacaoEspecificaForm, SolicitacaoForm
from .models import Solicitacao, TipoSolicitacao

# pdb.set_trace()

@login_required
def painelSolicitacoes(request):

    context = {
        'solicitacoesUser': Solicitacao.objects.filter(user=request.user),
    }

    return render(request, 'solicitacoes/index.html', context=context)


@login_required
def novaSolicitacao(request):
    if request.method == 'POST':
        form = SolicitacaoForm(request.POST, request.FILES)
        if form.is_valid():
            formSolicitacao = form.save(commit=False)
            formSolicitacao.user = request.user
            formSolicitacao.save()

            messages.success(request, 'Solicitação enviada com sucesso!')
            return redirect('painelSolicitacoes')
        else:
            messages.error(request, f'Solicitação não enviada: {form.errors}')
            return redirect('novaSolicitacao')

    context = {
        'form': SolicitacaoForm(),
        'tipoSolicitacoes': TipoSolicitacao.objects.all(),
    }

    return render(request, 'solicitacoes/novaSolicitacao.html', context=context)


@login_required
def painelAprovacaoSolicitacoes(request):

    context = {
        'solicitacoes': Solicitacao.objects.all().order_by('-id'),
    }

    return render(request, 'solicitacoes/painelAprovacaoSolicitacoes.html', context=context)

@login_required
def aprovacaoSolicitacao(request, id):

    if request.method == 'POST':
        solicitacao = get_object_or_404(Solicitacao, id=id)
        form = SolicitacaoEspecificaForm(request.POST, instance=solicitacao)
        if form.is_valid():
            formSolicitacao = form.save(commit=False)
            formSolicitacao.save()

            messages.success(request, 'Solicitação atualizada com sucesso!')
            return redirect('painelAprovacaoSolicitacoes')
        else:
            messages.error(request, f'Solicitação não atualizada: {form.errors}')
            return redirect('aprovacaoSolicitacao', id=id)

    context = {
        'form': SolicitacaoEspecificaForm(),
        'solicitacao': Solicitacao.objects.filter(id=id).first(),
    }

    return render(request, 'solicitacoes/aprovacaoSolicitacao.html', context=context)


@login_required
def deletarSolicitacao(request, id):
    produto = Solicitacao.objects.get(id=id)
    produto.delete()
    messages.success(request, 'Solicitação deletada com sucesso')
    return redirect('painelAprovacaoSolicitacoes')