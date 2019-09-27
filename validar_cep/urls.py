from django.urls import path

from validar_cep.views import ValidarCepView

urlpatterns = [
    path('', ValidarCepView.as_view()),

]
