from django import forms
import re

from django.utils.safestring import mark_safe


class CepForm(forms.Form):
    """form que recebe o cep digitado pelo usuário"""

    cep = forms.CharField(label='Cep:', max_length=6,
                          widget=forms.TextInput(attrs={'class': 'form-control'}, ),
                          help_text='Digite um número de CEP válido.<br> '
                                    '1. O CEP é um número maior que 100.000 e menor que 999999<br>'
                                    '2. O CEP não pode conter nenhum dígito repetitivo alternado em pares<br>'
                                    '3. Somente dígitos'
                          )
    pattern = re.compile('(\d)(?=\d\\1{1,1})')

    @staticmethod
    def verificar_faixa_valores(cep):
        """
        Recebe um int(CEP) e verifica se O CEP é um número maior que 100.000 e menor que 999999
        :return: True se o cep estiver dentro das faixa de valores permitidos, False senão estiver
        """
        if cep <= 100000 or cep >= 999999:
            return False
        else:
            return True

    @staticmethod
    def verificar_digito_repetitivo_alternado(cep):
        """
        Recebe uma string(CEP) e verifica se o CEP não contém nenhum dígito repetitivo alternado em pares
        :return: True se o cep não conter nenhum dígito repetitivo alternado em pares, False caso conter
        """
        if CepForm.pattern.search(cep) is None:
            return True
        else:
            return False

    @staticmethod
    def gerar_mensagem_erro(cep):
        """
        Recebe uma string(CEP) que contém um ou mais dígitos repetitivos alternados em pares, então
        gera a mensagem de erro a ser mostrada para o usuário destacando os pares alternados repetitivos encontrados.
        :return: String, com a mensagem de erro a ser mostrada ao usuário
        """
        mens_erro = 'O CEP não pode conter nenhum nenhum dígito repetitivo alternado em pares!'
        for match in CepForm.pattern.finditer(cep):
            mens_erro += '<br>%s<span style="color: blue">%s</span>%s<span style="color: blue">%s</span>%s' % (
                match.string[:match.start()], match.string[match.start()],
                match.string[match.start() + 1], match.string[match.start() + 2],
                match.string[match.start() + 3:] if len(match.string) > match.start() + 3 else '')
        return mens_erro


    def clean_cep(self):
            """
            Verifica se o valor informado é um CEP válido
            :return: O valor do CEP, se este for um valor válido, caso contrário da um raise forms.ValidationError,
                     retornando a mensagem de errro.
            """
            data = self.cleaned_data['cep']

            # verificar se só contem dígitos
            if data.isdigit() is False:
                raise forms.ValidationError("Somente números inteiros!")

            # verificar se esta dentro da faixa de valores permitidos, maior que 100.000 e menor que 999999
            if CepForm.verificar_faixa_valores(int(data)) is False:
                raise forms.ValidationError("O CEP é um número maior que 100.000 e menor que 999999!")

            # 'O CEP não pode conter nenhum nenhum dígito repetitivo alternado em pares'
            if CepForm.verificar_digito_repetitivo_alternado(data) is False:
                raise forms.ValidationError(mark_safe(CepForm.gerar_mensagem_erro(data)))

            return data
