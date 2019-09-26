from django.urls import path

from validar_cep.views import ValidarCepView

urlpatterns = [
    # path('', views.index, name='index'),
    path('', ValidarCepView.as_view()),

]
