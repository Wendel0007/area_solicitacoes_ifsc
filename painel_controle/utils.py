import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email_first(titulo, mensagem, email):

    html_content = render_to_string(
        'dashboard/auth/emails/email.html', {'mensagem': mensagem})
    text_content = strip_tags(html_content)
    mail = EmailMultiAlternatives(
        titulo, text_content, f'{os.getenv("EMAIL_HOST_USER")}', [email])
    mail.attach_alternative(html_content, 'text/html')
    mail.send()
