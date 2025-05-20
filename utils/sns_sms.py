import os
import boto3
from django.conf import settings

# Para funcionar para termos de testes é necessário cadastrar um número como sand box no sns da aws
def enviar_sms(numero_destino, mensagem):
    try:
        client = boto3.client(
            'sns',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION_NAME
        )

        numero_formatado = numero_destino if numero_destino.startswith('+') else f'+{numero_destino}'
        response = client.publish(
            PhoneNumber=numero_formatado,
            Message=mensagem
        )
        return response

    except Exception as e:
        print("Erro ao enviar SMS:")
        print(f"Exceção: {e}")
        print(f"AWS_ACCESS_KEY_ID: {aws_access_key_id}")
        print(f"AWS_SECRET_ACCESS_KEY: {aws_secret_access_key}")
        print(f"AWS_REGION_NAME: {region_name}")
        print(f"Número destino: {numero_destino}")
        print(f"Mensagem: {mensagem}")
        return None