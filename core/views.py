from django.views.generic.edit import CreateView
from.models import Cliente, Cadastro
from django.urls import reverse_lazy
from django.views.generic.list import ListView

class ClienteList(ListView):
    model = Cliente
    template_name = 'files/file.html'



class CadastroCreate(CreateView):
    model = Cadastro
    fields = ['cliente','Sobrenome', 'Data_de_nascimento', 'Email', "Apelido", "Observações"]
    template_name = 'files/cadastro.html'
    success_url = reverse_lazy('listagem')

class CadastroList(ListView):
    model = Cadastro
    template_name = 'files/file.html'