from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from validar_cep.forms import CepForm


class ValidarCepView(FormView):
    form_class = CepForm
    template_name = 'validar_cep/index.html'
    success_url = '/'