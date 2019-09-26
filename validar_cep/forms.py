from django import forms
import re

from django.utils.safestring import mark_safe


class CepForm(forms.Form):
    """form que recebe o cep digitado pelo usuário"""

    cep = forms.CharField(label='Cep:', max_length=6,
                          widget=forms.TextInput(attrs={'class': 'form-control'}, ),
                          help_text='Digite um número de CEP válido.<br> '
                                    '1. O CEP é um número maior que 100.000 e menor que 999999<br>'
                                    '2. O CEP não pode conter nenhum nenhum dígito repetitivo alternado em pares<br>'
                                    '3. Digite somente números'
                          )

    def clean_cep(self):
        data = self.cleaned_data['cep']

        # prog = re.compile(pattern)
        # result = prog.match(string)
        # re.sub("\D", "", "aas30dsa20")
        # verificar se tem letras
        if re.search("\D", data) is not None:
            raise forms.ValidationError("Somente números!")

        # verificar se esta dentro da faixa de valores permitidos, maior que 100.000 e menor que 999999
        data_num = int(data)
        if data_num <= 100000 or data_num >= 999999:
            raise forms.ValidationError("O CEP é um número maior que 100.000 e menor que 999999!")

        # '2. O CEP não pode conter nenhum nenhum dígito repetitivo alternado em pares'
        if re.search("(\d)(?=\d\\1{1,1})", data) is not None:
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
