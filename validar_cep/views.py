from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from validar_cep.forms import CepForm


class ValidarCepView(FormView):
    """
    View que retorna a página com o form, onde o usuário digita o cep
    """
    form_class = CepForm
    template_name = 'validar_cep/index.html'
    success_url = '/'

    def form_valid(self, form):
        #colocando o form no contexto
        return self.render_to_response(self.get_context_data(form=form))