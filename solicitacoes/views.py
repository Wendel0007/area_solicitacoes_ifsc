from django.shortcuts import render


def painelSolicitacoes(request):

    return render(request, 'solicitacoes/index.html')
