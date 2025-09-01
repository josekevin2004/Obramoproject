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
                'class': 'form-control block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
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
                'class': 'form-control block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
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
                'class': 'form-control block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
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
                'class': 'form-control block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                'placeholder': 'Informe a senha novamente',
            }
        ),
    )

