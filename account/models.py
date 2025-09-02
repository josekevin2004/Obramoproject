from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Modelo que estende o usuário padrão do Django para incluir
    o tipo de usuário (cliente ou profissional).
    """
    USER_TYPE_CHOICES = (
        ('client', 'Cliente'),
        ('professional', 'Profissional'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='client')

    def __str__(self):
        return f'{self.user.username} - {self.get_user_type_display()}'
