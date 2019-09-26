from django import forms
import re

class CepForm(forms.Form):
    """form que recebe o cep digitado pelo usuário"""

    cep = forms.CharField(label='Cep:', max_length=6,
                          widget=forms.TextInput(attrs={'class': 'form-control'},),
                          help_text='Digite um número de CEP válido.<br> '
                                    '1. O CEP é um número maior que 100.000 e menor que 999999<br>'
                                    '2. O CEP não pode conter nenhum nenhum dígito repetitivo alternado em pares<br>'
                                    '3. Digite somente números'
                          )
    def clean_cep(self):
        data = self.cleaned_data['cep']

        # prog = re.compile(pattern)
        # result = prog.match(string)
        #re.sub("\D", "", "aas30dsa20")
        #verificar se tem letras
        if re.search("\D", data) is not None:
            raise forms.ValidationError("Somente números!")

        #verificar se esta dentro da faixa de valores permitidos, maior que 100.000 e menor que 999999
        # data_num = float(data)
        if len(data) != 6 or data == '100000' or data == '999999':
            raise forms.ValidationError("O CEP é um número maior que 100.000 e menor que 999999!")

        #'2. O CEP não pode conter nenhum nenhum dígito repetitivo alternado em pares'
        if re.search("(\d)(?=\d\\1{1,1})", data) is not None:
            raise forms.ValidationError("O CEP não pode conter nenhum nenhum dígito repetitivo alternado em pares!")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data
