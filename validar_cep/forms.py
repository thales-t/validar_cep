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

    def verificar_faixa_valores(cep):
        """
        Recebe um int(CEP) e verifica se O CEP é um número maior que 100.000 e menor que 999999
        :return: True se o cep estiver dentro das faixa de valores permitidos, False senão estiver
        """
        if cep <= 100000 or cep >= 999999:
            return False
        else: return True

    # def verificar_somente_numero(cep):
    #     """
    #         Recebe uma string(CEP) e verifica se é um número inteiro
    #     :return: True se o cep só conter um número inteiro, False caso contrário
    #     """
    #     if re.search("\D", cep) is not None:
    #         return False
    #     else: return True

    def verificar_digito_repetitivo_alternado(cep):
        """
        Recebe uma string(CEP) e verifica se O CEP não contem nenhum dígito repetitivo alternado em pares
        :return: True se o cep não conter nenhum dígito repetitivo alternado em pares, False caso conter
        """
        if re.search("(\d)(?=\d\\1{1,1})", cep) is not None:
            return False
        else: return True

    def clean_cep(self):
        """
        Verifica se o valor informado é um CEP válido
        :return: O valor do CEP, se este for um valor válido, caso contrário da um raise forms.ValidationError,
                 retornando a mensagem de errro.
        """
        data = self.cleaned_data['cep']

        # prog = re.compile(pattern)
        # result = prog.match(string)
        # re.sub("\D", "", "aas30dsa20")
        #re.search("\D", data) is not None

        # verificar se só contem dígitos
        if data.isdigit() is False:
            raise forms.ValidationError("Somente números inteiros!")

        # verificar se esta dentro da faixa de valores permitidos, maior que 100.000 e menor que 999999
        # data_num = int(data)
        if CepForm.verificar_faixa_valores(int(data)):
            raise forms.ValidationError("O CEP é um número maior que 100.000 e menor que 999999!")

        # '2. O CEP não pode conter nenhum nenhum dígito repetitivo alternado em pares'
        if CepForm.verificar_digito_repetitivo_alternado(data) is False:
            mens_erro = 'O CEP não pode conter nenhum nenhum dígito repetitivo alternado em pares!'
            for match in re.finditer("(\d)(?=\d\\1{1,1})", data):
                mens_erro += '<br> %s<span style="color: blue" >%s</span>%s<span style="color: blue" >%s</span>%s' % (
                match.string[:match.start()],  match.string[match.start()],
                match.string[match.start()+1], match.string[match.start()+2],
                match.string[match.start() + 3:] if len(match.string) > match.start() + 3 else '')


                # cep = '%s<span style="color: %s" >%s</span>%s' % (
                # match.string[:match.start()+2], cor, match.string[match.start()+2], match.string[match.start() + 3:])

            raise forms.ValidationError(mark_safe(mens_erro))

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data
