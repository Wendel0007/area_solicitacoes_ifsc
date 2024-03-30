from django import forms

from .models import Solicitacao, TipoSolicitacao


class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = ['tipo_solicitacao', 'descricao', 'arquivo']

    tipo_solicitacao = forms.ModelChoiceField(
        queryset=TipoSolicitacao.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Selecione um tipo'}
        ),
        error_messages={'required': 'Tipo não pode ser vazio'},
        label='Selecione um tipo'
    )

    def __init__(self, *args, **kwargs):
        super(SolicitacaoForm, self).__init__(*args, **kwargs)
        self.fields['tipo_solicitacao'].label_from_instance = lambda obj: obj.nome_completo

    descricao = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição da Solicitação'}),
        error_messages={'required': 'Descrição não pode ser vazia'},
        label='Descrição da Solicitação'
    )

    arquivo = forms.FileField(
        required=True,
        widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Selecione um arquivo'}),
        error_messages={'required': 'Arquivo não pode ser vazio'},
        label='Arquivo'
    )

    # status = forms.ChoiceField(
    #     required=True,
    #     choices=Solicitacao.STATUS_CHOICES,
    #     widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecione um status'}),
    #     error_messages={'required': 'Status não pode ser vazio'},
    #     label='Status da Solicitação'
    # )


class SolicitacaoEspecificaForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = ['status']

    status = forms.ChoiceField(
        required=True,
        choices=Solicitacao.STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecione um status'}),
        error_messages={'required': 'Alterar status não pode ser vazio'},
        label='Alterar status da Solicitação'
    )
