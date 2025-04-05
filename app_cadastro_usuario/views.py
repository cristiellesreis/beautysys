from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

class CadastroView(View):
    def get(self, request):
        return render(request, "cadastro_usuario/cadastro.html")

    def post(self, request):
        usuario = request.POST.get("usuario")
        email = request.POST.get("email")
        email_confirm = request.POST.get("emailconfirm")
        senha = request.POST.get("senha")
        senha_confirm = request.POST.get("senhaconfirm")
        tipo_usuario = request.POST.get("tipo")  # cliente, funcionario, administrador

        if email != email_confirm or senha != senha_confirm:
            return render(request, "cadastro_usuario/cadastro.html", {
                "error": "Email ou senha não conferem."
            })

        if User.objects.filter(username=usuario).exists():
            return render(request, "cadastro_usuario/cadastro.html", {
                "error": "Nome de usuário já está em uso."
            })

        if User.objects.filter(email=email).exists():
            return render(request, "cadastro_usuario/cadastro.html", {
                "error": "Email já cadastrado."
            })

        user = User.objects.create_user(username=usuario, email=email, password=senha)
        grupo = Group.objects.filter(name=tipo_usuario.capitalize()).first()

        if grupo:
            user.groups.add(grupo)

        return redirect("login")


class LoginView(View):
    def get(self, request):
        return render(request, "cadastro_usuario/login.html")

    def post(self, request):
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        user = User.objects.filter(email=email).first()

        if user:
            user = authenticate(request, username=user.username, password=senha)
            if user:
                login(request, user)
                return redirect("home")

        return render(request, "cadastro_usuario/login.html", {
            "error": "Email ou senha inválidos."
        })


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
