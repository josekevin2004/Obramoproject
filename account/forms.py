from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(
        label='Usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Informe o seu nome de usuário'
            }
        ),
    )
    password = forms.CharField(
       label='Senha',
       required=True,
       max_length=80,
       widget=forms.PasswordInput(
           attrs={
               'class': 'form-control',
               'placeholder': 'Informe a sua senha',   
           }
       ),
   )


class RegisterForm(forms.Form):
   login = forms.CharField(
       label='Usuário',
       required=True,
       max_length=100,
       widget=forms.TextInput(
           attrs={
               'class': 'form-control',
               'placeholder': 'Ex: mariaFernanda'
           }
       ),
   )
   email = forms.EmailField(
        label='E-mail',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: mariaFernanda@gmail.com',
            }
        ),
   )
   password = forms.CharField(
       label='Senha',
       required=True,
       max_length=80,
       widget=forms.PasswordInput(
           attrs={
               'class': 'form-control',
               'placeholder': 'Informe a sua senha',   
           }
       ),
   )
   reverter_password = forms.CharField(
       label='Confirme a senha',
       required=True,
       max_length=80,
       widget=forms.PasswordInput(
           attrs={
               'class': 'form-control',
               'placeholder': 'Informe a senha novamente',
           }
       ),
    )