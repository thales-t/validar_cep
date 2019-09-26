from django.test import TestCase

# Create your tests here.
from validar_cep.forms import CepForm


class CepFormTests(TestCase):

    def test_verificar_faixa_valores(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        self.assertIs(CepForm.verificar_faixa_valores(50), False)
        self.assertIs(CepForm.verificar_faixa_valores(100000), False)
        self.assertIs(CepForm.verificar_faixa_valores(150000), True)
        self.assertIs(CepForm.verificar_faixa_valores(254689), True)
        self.assertIs(CepForm.verificar_faixa_valores(999999), False)
        self.assertIs(CepForm.verificar_faixa_valores(1854963), False)
