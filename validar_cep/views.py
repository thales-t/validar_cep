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
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # context = super().get_context_data(**kwargs)
        # context['publisher'] = self.object
        # return super().form_valid(form)
        # form.cleaned_data['resultado'] = "Válido"
        return self.render_to_response(self.get_context_data(form=form))


    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     error = False
    #     result = None
    #     if form.is_valid():
    #
    #         return render(request, self.template_name, {'form': form, 'result': result, 'error': error})
    #
    #     return render(request, self.template_name, {'form': form})
