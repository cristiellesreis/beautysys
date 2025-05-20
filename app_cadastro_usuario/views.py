from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from app_perfil.models import Perfil


class CadastroView(View):
    def get(self, request):
        return render(request, "cadastro_usuario/cadastro.html")

    def post(self, request):
        form = {
            "usuario": request.POST.get("usuario"),
            "email": request.POST.get("email"),
            "emailconfirm": request.POST.get("emailconfirm"),
            "senha": request.POST.get("senha"),
            "senhaconfirm": request.POST.get("senhaconfirm"),
        }
        usuario = request.POST.get("usuario")
        email = request.POST.get("email")
        email_confirm = request.POST.get("emailconfirm")
        senha = request.POST.get("senha")
        senha_confirm = request.POST.get("senhaconfirm")

        if email != email_confirm or senha != senha_confirm:
            messages.error(request, 'Email ou senha não conferem.')
            return render(request, "cadastro_usuario/cadastro.html", {"form": form})

        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'Nome de usuário já está em uso.')
            return render(request, "cadastro_usuario/cadastro.html", {"form": form})

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado.')
            return render(request, "cadastro_usuario/cadastro.html", {"form": form})

        user = User.objects.create_user(username=usuario, email=email, password=senha)
        Perfil.objects.create(
            user=user,
            nome_salao="Meu Salão",
            telefone="",
            cnpj="",
            endereco="",
            cidade="",
            estado="",
            cep="",
            imagem="",
        )
        return redirect("login")


class LoginView(View):
    def get(self, request):
        if not request.user.is_authenticated and 'next' in request.GET:
            messages.warning(request, "Você não está logado.")
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

        messages.error(request,'Email ou senha inválidos.')

        return render(request, "cadastro_usuario/login.html")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
