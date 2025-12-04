#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View

from tripadvisor.forms import AtracaoForm
from tripadvisor.models import Atracao


# Talvez mais tarde será usado
# class UserCreateViewGeneric(CreateView):
#     model = User
#     form_class = UserCreationForm
#     template_name = 'reporter/create_simple.html'
#     #success_url = reverse_lazy('')


# Inicio: GERENCIAMENTO DE ATRAÇÃO
class AtracaoListView(LoginRequiredMixin, PermissionRequiredMixin,View):
    permission_required = 'tripadvisor.atracao_list'
    login_url = reverse_lazy('accounts:login')

    @staticmethod
    def get(request):
        lista_atracoes = Atracao.objects.all()

        lista_reporters = {
            'lista_atracoes': lista_atracoes,
        }

        return render(request, 'atracao/list.html', lista_reporters)


class AtracaoDetailsView(View):
    login_url = reverse_lazy('account:login')

    @staticmethod
    def get(request, pk):
        atracao = Atracao.objects.get(id=pk)
        context = {
            'atracao': atracao,
        }
        return render(request, 'atracao/read.html', context)


class AtracaoDeleteView(View):
    @staticmethod
    def get(request, pk):
        atracao = get_object_or_404(Atracao, pk=pk)

        context = {
            'atracao': atracao,
        }

        return render(request, "atracao/delete.html", context)

    @staticmethod
    def post(request, pk):
        atracao = get_object_or_404(Atracao, pk=pk)

        try:
            v_atracao_id = request.POST.get("atracao_id", None)
            print(v_atracao_id)
            if int(v_atracao_id) == pk:
                atracao.delete()
                return redirect('tripadvisor:atracao_list' )

            else:
                print('Recusou a deletar, pk do objeto não bate com o pk do POST')

        except Exception as e:
            print("Erro")
            print(e)
            context = {
                'atracao': atracao,
            }
            return render(request, "atracao/delete.html", context)
        return redirect('tripadvisor:atracao_list')


class AtracaoCreateView(View):

    @staticmethod
    def get(request):
        form = AtracaoForm()
        context = {
            'form': form
        }
        return render(request, 'atracao/create_simple.html', context)

    @staticmethod
    def post(request):

        form = AtracaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tripadvisor:atracao_list')

        context = {
            'form': form
        }
        return render(request, 'atracao/create_simple.html', context)


class AtracaoUpdateView(View):

    @staticmethod
    def get(request, pk):
        atracao = get_object_or_404(Atracao, pk=pk)
        form = AtracaoForm(instance=atracao)
        context = {
            'form': form,
            'atracao': atracao,
        }

        return render(request, 'atracao/update.html', context)

    @staticmethod
    def post(request, pk):
        atracao = get_object_or_404(Atracao, pk=pk)

        form = AtracaoForm(request.POST, instance=atracao)

        if form.is_valid():
            form.save()
            return redirect('tripadvisor:atracao_list')

        context = {
            'form': form,
            'atracao': atracao,
        }
        return render(request, 'atracao/update.html', context)
# Fim: GERENCIAMENTO DE ATRAÇÃO