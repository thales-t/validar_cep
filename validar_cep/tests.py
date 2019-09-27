from django.test import TestCase

# Create your tests here.
from validar_cep.forms import CepForm


class CepFormTests(TestCase):

    def test_verificar_faixa_valores(self):
        """
        verificar_faixa_valores() que recebe um int e verifica se O CEP é um número maior que
        100.000 e menor que 999999. Retorna True se o cep estiver dentro das faixa de valores
        permitidos, False senão estiver
        """
        self.assertIs(CepForm.verificar_faixa_valores(50), False)
        self.assertIs(CepForm.verificar_faixa_valores(100000), False)
        self.assertIs(CepForm.verificar_faixa_valores(150000), True)
        self.assertIs(CepForm.verificar_faixa_valores(254689), True)
        self.assertIs(CepForm.verificar_faixa_valores(999999), False)
        self.assertIs(CepForm.verificar_faixa_valores(1854963), False)

    def test_verificar_digito_repetitivo_alternado(self):
        """
        verificar_digito_repetitivo_alternado() que recebe uma string e verifica se O CEP não
        contem nenhum dígito repetitivo alternado em pares. Retorna True se o cep não conter
        nenhum dígito repetitivo alternado em pares, False caso conter
        """
        self.assertIs(CepForm.verificar_digito_repetitivo_alternado('121426'), False)
        self.assertIs(CepForm.verificar_digito_repetitivo_alternado('523563'), True)
        self.assertIs(CepForm.verificar_digito_repetitivo_alternado('552523'), False)
        self.assertIs(CepForm.verificar_digito_repetitivo_alternado('112233'), True)

    def test_verificar_se_digito(self):
        """ Verifica se contém somente dígitos"""
        self.assertIs('523563'.isdigit(), True)
        self.assertIs('523.1'.isdigit(), False)
        self.assertIs('523,1'.isdigit(), False)

    def test_gerar_mensagem_erro(self):
        """
        gerar_mensagem_erro() que recebe uma string(CEP) que contém um ou mais dígitos repetitivos alternados
        em pares, então gera a mensagem de erro a ser mostrada para o usuário destacando os pares alternados
        repetitivos encontrados. Retorna String, com a mensagem de erro a ser mostrada ao usuário
        """
        self.assertEqual(CepForm.gerar_mensagem_erro('121426'),
                         'O CEP não pode conter nenhum nenhum dígito repetitivo alternado em pares!'
                         '<br><span style="color: blue">1</span>2<span style="color: blue">1</span>426')
        self.assertEqual(CepForm.gerar_mensagem_erro('523563'),
                         'O CEP não pode conter nenhum nenhum dígito repetitivo alternado em pares!')
        self.assertEqual(CepForm.gerar_mensagem_erro('552523'),
                         'O CEP não pode conter nenhum nenhum dígito repetitivo alternado em pares!'
                         '<br>5<span style="color: blue">5</span>2<span style="color: blue">5</span>23'
                         '<br>55<span style="color: blue">2</span>5<span style="color: blue">2</span>3')
        self.assertEqual(CepForm.gerar_mensagem_erro('112233'),
                         'O CEP não pode conter nenhum nenhum dígito repetitivo alternado em pares!')
