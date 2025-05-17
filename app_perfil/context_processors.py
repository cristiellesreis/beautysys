from .models import Perfil

def perfil_usuario(request):
    if request.user.is_authenticated:
        perfil = Perfil.objects.filter(user=request.user).first()
        return {'perfil': perfil}
    return {}
