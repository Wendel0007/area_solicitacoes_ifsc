# upload_utils.py

def upload_to(instance, filename):
    return f'static/solicitacoes/arquivo/{instance.user.perfil.matricula}/{filename}'
