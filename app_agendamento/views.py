from django.shortcuts import render

def agendamento(request):
    return render(request, 'agenda/agenda.html')
